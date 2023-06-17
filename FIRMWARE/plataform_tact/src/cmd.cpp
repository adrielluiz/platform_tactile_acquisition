#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <ctype.h>
#include <stdalign.h>
#include "cmd.h"
#include "app.h"
#include "mpu.h"

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
#define CMD_PRINTF_INT_SIZE  64
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
static bool cmd_set_speed_handler(uint32_t argc, uint8_t *argv[]);
static bool cmd_get_speed_handler(uint32_t argc, uint8_t *argv[]);
static bool cmd_set_pos_handler(uint32_t argc, uint8_t *argv[]);
static bool cmd_get_pos_handler(uint32_t argc, uint8_t *argv[]);
static bool cmd_get_mpu_handler(uint32_t argc, uint8_t *argv[]);
static bool cmd_set_delay_handler(uint32_t argc, uint8_t *argv[]);
static bool cmd_get_delay_handler(uint32_t argc, uint8_t *argv[]);
static bool cmd_get_fsr_handler(uint32_t argc, uint8_t *argv[]);


const cmd_entry_t cmd_list[] =
{
	CMD_INIT("help","show available commands","help; help command",cmd_default_handler,cmd_default_handler,cmd_run_help_handler),
	CMD_INIT("mode","get/set operation mode (idle,run1)","set mode run1",cmd_set_mode_handler,cmd_get_mode_handler,cmd_default_handler),
	CMD_INIT("speed","get/set motor (1-2) speed (1-200) m/s","set speed 1 70",cmd_set_speed_handler,cmd_get_speed_handler,cmd_default_handler),
	CMD_INIT("position","get/set motor (1-2) position (0-50000) mm","set position 1 50000",cmd_set_pos_handler,cmd_get_pos_handler,cmd_default_handler),
	CMD_INIT("mpu","get mpu","get mpu",cmd_default_handler,cmd_get_mpu_handler,cmd_default_handler),
	CMD_INIT("read_delay","get/set read_delay (1-5000) ms","set read_delay 100",cmd_set_delay_handler,cmd_get_delay_handler,cmd_default_handler),
	CMD_INIT("fsr","get fsr","get fst",cmd_default_handler,cmd_get_fsr_handler,cmd_default_handler),	
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

static bool cmd_convert_int(uint8_t *data, int32_t *val, int32_t min_val, int32_t max_val)
{
	bool status = false;

	if(sscanf((char *)data,"%d",(int *)val) == 1)
	{
		if(*val >= min_val && *val <= max_val)
			status = true;
	}

	return status;
}

static bool cmd_set_mode_handler(uint32_t argc, uint8_t *argv[])
{
	bool status = false;
	char buffer[CMD_PRINTF_INT_SIZE];

	if(argc == 1)
	{
		if(strncmp((char *)argv[0],"idle",4) == 0)
		{
			app_set_mode(APP_MODE_IDLE);
			status = true;
		}
	}
	else if(argc == 3)
	{
		uint32_t flag_motors = 0;
		uint32_t flag_mpu = 0;

		if(strncmp((char *)argv[0],"read",4) == 0)
		{
			if(cmd_convert_uint(argv[1],&flag_motors,0,1) && cmd_convert_uint(argv[2],&flag_mpu,0,1))
			{
				app_set_mode(APP_MODE_READ);
				app_set_read(flag_motors,flag_mpu);
				status = true;				
			}
		}
	}

	if(status)
	{
		snprintf(buffer,CMD_PRINTF_INT_SIZE-1,"ok\n");
		CMD_ADD_MSG(buffer);
	}

	return status;
}

static bool cmd_get_mode_handler(uint32_t argc, uint8_t *argv[])
{
	bool status = false;

	if(argc == 0)
	{
		char *modes[] = { "idle", "read"};

		app_mode_t mode = app_get_mode();
		CMD_ADD_MSG(modes[mode]);
		CMD_ADD_MSG("\n");
		status = true;
	}

	return status;
}

static bool cmd_set_speed_handler(uint32_t argc, uint8_t *argv[])
{
	bool status = false;

	if(argc == 2)
	{
		char buffer[CMD_PRINTF_INT_SIZE];
		uint32_t val1 = 0;
		uint32_t val2 = 0;

		if(cmd_convert_uint(argv[0],&val1,1,2) && cmd_convert_uint(argv[1],&val2,1,200))
		{
			app_set_motor_speed(val1,val2);

			snprintf(buffer,CMD_PRINTF_INT_SIZE-1,"ok\n");
			CMD_ADD_MSG(buffer);

			status = true;
		}
	}

	return status;
}

static bool cmd_get_speed_handler(uint32_t argc, uint8_t *argv[])
{
	bool status = false;

	if(argc == 1)
	{
		uint32_t  val = 0;
		int speed = 0;

		if(cmd_convert_uint(argv[0],&val,1,2))
		{
			char buffer[CMD_PRINTF_INT_SIZE];

			speed = app_get_motor_speed(val);

			snprintf(buffer,CMD_PRINTF_INT_SIZE-1,"speed %d\n",speed);
			CMD_ADD_MSG(buffer);

			status = true;
		}

	}

	return status;
}

static bool cmd_set_pos_handler(uint32_t argc, uint8_t *argv[])
{
	bool status = false;

	if(argc == 2)
	{
		char buffer[CMD_PRINTF_INT_SIZE];
		uint32_t val1 = 0;
		int32_t val2 = 0;

		if(cmd_convert_uint(argv[0],&val1,1,2) && cmd_convert_int(argv[1],&val2,-50000,50000))
		{
			app_set_motor_pos(val1,val2);

			snprintf(buffer,CMD_PRINTF_INT_SIZE-1,"ok\n");
			CMD_ADD_MSG(buffer);

			status = true;
		}
		else if(cmd_convert_uint(argv[0],&val1,1,2) && (strncmp((char *)argv[1],"home",4) == 0))
		{
			app_set_motor_pos_home(val1);

			snprintf(buffer,CMD_PRINTF_INT_SIZE-1,"ok\n");
			CMD_ADD_MSG(buffer);

			status = true;

		}
	}

	return status;
}

static bool cmd_get_pos_handler(uint32_t argc, uint8_t *argv[])
{
	bool status = false;

	if(argc == 1)
	{
		uint32_t  val = 0;
		int position = 0;

		if(cmd_convert_uint(argv[0],&val,1,2))
		{
			char buffer[CMD_PRINTF_INT_SIZE];

			position = app_get_motor_pos(val);

			snprintf(buffer,CMD_PRINTF_INT_SIZE-1,"position %d\n",position);
			CMD_ADD_MSG(buffer);

			status = true;
		}

	}

	return status;
}

static bool cmd_get_mpu_handler(uint32_t argc, uint8_t *argv[])
{
	bool status = false;

	if(argc == 0)
	{
		mpu_data_t* mpu_data;

		char buffer[CMD_PRINTF_INT_SIZE];

		mpu_data = app_get_mpu();

		snprintf(buffer,CMD_PRINTF_INT_SIZE-1,"mpu  %d %d %d %d %d %d %d\n",mpu_data->AcX, mpu_data->AcY, mpu_data->AcZ, mpu_data->Tmp,
														  mpu_data->GyX, mpu_data->GyY, mpu_data->GyZ);
		CMD_ADD_MSG(buffer);

		status = true;
	}

	return status;
}

static bool cmd_set_delay_handler(uint32_t argc, uint8_t *argv[])
{
	bool status = false;

	if(argc == 1)
	{
		char buffer[CMD_PRINTF_INT_SIZE];
		uint32_t val = 0;

		if(cmd_convert_uint(argv[0],&val,1,5000))
		{
			app_set_read_delay_ms(val);

			snprintf(buffer,CMD_PRINTF_INT_SIZE-1,"ok\n");
			CMD_ADD_MSG(buffer);

			status = true;
		}
	}

	return status;
}

static bool cmd_get_delay_handler(uint32_t argc, uint8_t *argv[])
{
	bool status = false;

	if(argc == 0)
	{
		uint32_t  val = 0;
		char buffer[CMD_PRINTF_INT_SIZE];

		val = app_get_read_delay_ms();

		snprintf(buffer,CMD_PRINTF_INT_SIZE-1,"read_delay %d\n",val);
		CMD_ADD_MSG(buffer);

		status = true;
	}

	return status;
}


static bool cmd_get_fsr_handler(uint32_t argc, uint8_t *argv[])
{
	bool status = false;

	if(argc == 0)
	{
		uint32_t  val = 0;
		char buffer[CMD_PRINTF_INT_SIZE];

		val = app_get_fsr();

		snprintf(buffer,CMD_PRINTF_INT_SIZE-1,"fsr %d\n",val);
		CMD_ADD_MSG(buffer);

		status = true;
	}

	return status;
}