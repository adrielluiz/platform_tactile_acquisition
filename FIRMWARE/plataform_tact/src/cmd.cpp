#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <ctype.h>
#include <stdalign.h>
#include "cmd.h"
#include "app.h"

#define CMD_MAX_ARGS 10

#define CMD_INIT(n,h,e,s,g,r) {	\
	.name = (uint8_t*) (n), 	\
	.help = (uint8_t *)(h), 	\
	.example = (uint8_t *)(e), 	\
	.name_size = sizeof(n)-1, 	\
	.set = (s), 				\
	.get = (g), 				\
	.run = (r) }

#define CMD_TWIN_MAX_TIME_MS (60*60*1000) // 1h
#define CMD_PRINTF_INT_SIZE  32
#define CMD_ADD_MSG(m) app_uc2usb_rx_cbk((uint8_t *)(m), strlen((char *)(m)));

typedef bool (*cmd_handler_t)(uint32_t argc, uint8_t *argv[]);

typedef struct cmd_entry_s
{
	const uint8_t * const name;
	const uint8_t * const help;
	const uint8_t * const example;
	uint8_t name_size;
	cmd_handler_t set;
	cmd_handler_t get;
	cmd_handler_t run;
} cmd_entry_t;

static bool cmd_run_help_handler(uint32_t argc, uint8_t *argv[]);
static bool cmd_default_handler(uint32_t argc, uint8_t *argv[]);
static bool cmd_set_mode_handler(uint32_t argc, uint8_t *argv[]);
static bool cmd_get_mode_handler(uint32_t argc, uint8_t *argv[]);
static bool cmd_set_addr_handler(uint32_t argc, uint8_t *argv[]);
static bool cmd_get_addr_handler(uint32_t argc, uint8_t *argv[]);

const cmd_entry_t cmd_list[] =
{
	CMD_INIT("help","show available commands","help; help command",cmd_default_handler,cmd_default_handler,cmd_run_help_handler),
	CMD_INIT("mode","get/set operation mode (idle,run1)","set mode run1",cmd_set_mode_handler,cmd_get_mode_handler,cmd_default_handler),
	CMD_INIT("addr","get/set zigbee short address (0-65535)","set addr 123",cmd_set_addr_handler,cmd_get_addr_handler,cmd_default_handler),
};

uint32_t cmd_parse_args(uint8_t * const cmdline, uint32_t size, uint32_t *argc, uint8_t *argv[], uint32_t max_args)
{
    uint32_t n, m;

    n = m = 0;
    *argc = 0;

    while(cmdline[n] != '\0')
    {
        // remove initial spaces, if any
        while(isspace(cmdline[n]) && n < size)
            cmdline[n++] = '\0';

        // save where command/arguments starts
        m = n;

        // find end of command/parameters
        while(!isspace(cmdline[n]) && (n < size) && (cmdline[n] != '\0'))
            n++;

        // check end of string was reached, number of arguments reached or if we have an empty command
        if((n >= size) || (*argc >= max_args) || (m == n))
            break;

        // save command/arguments
        argv[*argc] = cmdline + m;
        *argc += 1;
    }

    // invalidate non used arguments
    for(n = *argc ; n < max_args ; n++)
        argv[n] = (uint8_t*)'\0';

    return *argc;
}

static bool cmd_proc_internal(uint8_t * const cmdline, uint32_t size)
{
	uint32_t argc;
	static uint8_t *argv[CMD_MAX_ARGS];

	if(cmd_parse_args(cmdline,size,&argc,(uint8_t **)argv,CMD_MAX_ARGS))
	{
		uint32_t offset = 0;
		bool is_get = strncmp((char *)argv[0],"get",3) == 0;
		bool is_set = strncmp((char *)argv[0],"set",3) == 0;

		// [set|get] command arg1 arg2 ... (offset 1)
		// or
		// command arg1 arg2 ... (offset 0)
		if(is_get || is_set)
		{
			if((argc < 3 && is_set) || (argc < 2 && is_get))
				return false;

			offset = 1;
		}

		for(uint32_t cmd_idx = 0 ; cmd_idx <  sizeof(cmd_list)/sizeof(cmd_list[0]) ; cmd_idx++)
		{
			if(strncmp((char *)argv[offset],(char *)cmd_list[cmd_idx].name,cmd_list[cmd_idx].name_size) == 0)
			{
				if(is_set)
					return cmd_list[cmd_idx].set(argc-(offset+1),&argv[(offset+1)]);
				else if(is_get)
					return cmd_list[cmd_idx].get(argc-(offset+1),&argv[(offset+1)]);
				else
					return cmd_list[cmd_idx].run(argc-(offset+1),&argv[(offset+1)]);
			}
		}
	}

	return false;
}

void cmd_proc(uint8_t * const cmdline, uint32_t size)
{
	if(cmd_proc_internal(cmdline,size) == false)
	{
		CMD_ADD_MSG("invalid command\n");
	}
}

static bool cmd_default_handler(uint32_t argc, uint8_t *argv[])
{
	return false;
}

static bool cmd_run_help_handler(uint32_t argc, uint8_t *argv[])
{
	bool status = false;

	if(argc == 0)
	{
		CMD_ADD_MSG("help: available commands\n");

		for(uint32_t cmd_idx = 0 ; cmd_idx <  sizeof(cmd_list)/sizeof(cmd_list[0]) ; cmd_idx++)
		{
			CMD_ADD_MSG("- ");
			CMD_ADD_MSG(cmd_list[cmd_idx].name);
			CMD_ADD_MSG("\n");
		}

		status = true;
	}
	else if(argc == 1)
	{
		for(uint32_t cmd_idx = 0 ; cmd_idx <  sizeof(cmd_list)/sizeof(cmd_list[0]) ; cmd_idx++)
		{
			if(strncmp((char *)argv[0],(char *)cmd_list[cmd_idx].name,cmd_list[cmd_idx].name_size) == 0)
			{
				CMD_ADD_MSG(cmd_list[cmd_idx].help);
				CMD_ADD_MSG("\nexample: ");
				CMD_ADD_MSG(cmd_list[cmd_idx].example);
				CMD_ADD_MSG("\n");

				status = true;
				break;
			}
		}
	}

	return status;
}

static bool cmd_set_mode_handler(uint32_t argc, uint8_t *argv[])
{
	bool status = false;

	if(argc == 1)
	{
		if(strncmp((char *)argv[0],"idle",4) == 0)
		{
			app_set_mode(APP_MODE_IDLE);
			status = true;
		}
		else if(strncmp((char *)argv[0],"run1",4) == 0)
		{
			app_set_mode(APP_MODE_RUN1);
			status = true;
		}
	}

	return status;
}

static bool cmd_get_mode_handler(uint32_t argc, uint8_t *argv[])
{
	bool status = false;

	if(argc == 0)
	{
		char *modes[] = { "idle", "run1"};

		app_mode_t mode = app_get_mode();
		CMD_ADD_MSG(modes[mode]);
		CMD_ADD_MSG("\n");
		status = true;
	}

	return status;
}

static bool cmd_convert_uint(uint8_t *data, uint32_t *val, uint32_t min_val, uint32_t max_val)
{
	bool status = false;

	if(sscanf((char *)data,"%u",(unsigned int *)val) == 1)
	{
		if(*val >= min_val && *val <= max_val)
			status = true;
	}

	return status;
}

static bool cmd_set_addr_handler(uint32_t argc, uint8_t *argv[])
{
	bool status = false;

	if(argc == 1)
	{
		uint32_t val = 0;

		if(cmd_convert_uint(argv[0],&val,0,0xffff))
		{
			status = true;
		}
	}

	return status;
}

static bool cmd_get_addr_handler(uint32_t argc, uint8_t *argv[])
{
	bool status = false;

	if(argc == 0)
	{
		char buffer[CMD_PRINTF_INT_SIZE];

    	snprintf(buffer,CMD_PRINTF_INT_SIZE-1,"addr %u\n",10);
		CMD_ADD_MSG(buffer);

		status = true;
	}

	return status;
}
