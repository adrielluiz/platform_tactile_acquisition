#include <stdint.h>
#include <stdbool.h>
#include "cbuf.h"

#define UTIL_CBUF_INC(v,mv)   ((((v) + 1) >= (mv)) ? 0 : (v) + 1)

cbuf_status_t cbuf_init(cbuf_t *cb)
{
	return cbuf_flush(cb);
}

cbuf_status_t cbuf_flush(cbuf_t *cb)
{
	
	cb->prod = cb->cons = 0;

	return UTIL_CBUF_OK;
}

cbuf_status_t cbuf_get(cbuf_t *cb, uint8_t *c)
{
	if(cb->cons == cb->prod)
		return UTIL_CBUF_EMPTY;

	*c = cb->buffer[cb->cons];
	cb->cons = UTIL_CBUF_INC(cb->cons,cb->size);

	return UTIL_CBUF_OK;
}

cbuf_status_t cbuf_put(cbuf_t *cb, uint8_t c)
{
	uint16_t next_prod = UTIL_CBUF_INC(cb->prod,cb->size);

	if(next_prod == cb->cons)
		return UTIL_CBUF_FULL;

	cb->buffer[cb->prod] = c;
	cb->prod = next_prod;

	return UTIL_CBUF_OK;
}

#if 0
int16_t cbuf_find_str(cbuf_t *cb, uint8_t *str, uint16_t len, uint16_t *nb, uint32_t tmrout_ms)
{
	uint16_t n_match = 0;
	uint8_t c;
	uint32_t tmr = hw_time_get();

	*nb = 0;
	do
	{
		if(cbuf_get(cb,&c) == UTIL_CBUF_OK)
		{
			*nb = *nb + 1;
			if(str[n_match] == c)
				n_match++;
			else
				n_match = 0;

			if(n_match >= len)
				return 0;		
		}
	} while (hw_time_elapsed(tmr,hw_time_get()) < tmrout_ms);

	return -1;
}

int16_t cbuf_find_multi_str(cbuf_t *cb, cbuf_str_t *str_list, uint16_t len_list, uint32_t tmrout_ms)
{
	uint16_t n;
	uint8_t c;
	uint32_t tmr = hw_time_get();

	for(n = 0; n < len_list ; n++)
		str_list[n].n_match = 0;

	do
	{
		if(cbuf_get(cb,&c) == UTIL_CBUF_OK)
		{
			for(n = 0; n < len_list ; n++)
			{
				if(str_list[n].str[str_list[n].n_match] == c)
					str_list[n].n_match++;
				else
					str_list[n].n_match = 0;

				if(str_list[n].n_match >= str_list[n].len)
					return n;
			}
		}
	} while (hw_time_elapsed(tmr,hw_time_get()) < tmrout_ms);

	return -1;	
}

int16_t cbuf_get_str_until_find(cbuf_t *cb, uint8_t *buf, uint16_t *buf_len,
                                     uint8_t *str, uint16_t len, uint32_t tmrout_ms)
{
	uint16_t n_match = 0;
	uint8_t c;
	uint32_t tmr = hw_time_get();
	uint16_t p = 0;

	if(*buf_len == 0)
		return -1;

	do
	{
		if(cbuf_get(cb,&c) == UTIL_CBUF_OK)
		{
			buf[p++] = c;
			if(p >= *buf_len)
				return 1;
			
			if(str[n_match] == c)
				n_match++;
			else
				n_match = 0;

			if(n_match >= len)
			{
				*buf_len = p;
				return 0;
			}
		}
	} while (hw_time_elapsed(tmr,hw_time_get()) < tmrout_ms);

	*buf_len = p;
	return -1;
}

cbuf_status_t cbuf_get_tmrout(cbuf_t *cb, uint8_t *c, uint32_t tmrout_ms)
{
	uint32_t tmr = hw_time_get();
	
	while (hw_time_elapsed(tmr,hw_time_get()) < tmrout_ms)
	{
		if(cb->cons == cb->prod)
			continue;
		else
			break;
	}
	
	if(cb->prod == cb->cons)
		return UTIL_CBUF_EMPTY;

	*c = cb->buffer[cb->cons];
	cb->cons = UTIL_CBUF_INC(cb->cons,cb->size);

	return UTIL_CBUF_OK;
}

int16_t cbuf_get_str(cbuf_t *cb, uint8_t *buf, uint16_t *buf_len, uint32_t tmrout_ms)
{
	uint8_t c;
	uint32_t tmr = hw_time_get();
	uint16_t p = 0;

	if(*buf_len == 0)
		return -1;

	do
	{
		if(cbuf_get(cb,&c) == UTIL_CBUF_OK)
		{
			buf[p++] = c;
			if(p >= *buf_len)
				return 1;			
		}
	} while (hw_time_elapsed(tmr,hw_time_get()) < tmrout_ms);

	*buf_len = p;
	return -1;
}

cbuf_status_t cbuf_get_beg(cbuf_t *cb, uint8_t *c, uint16_t *cons)
{
	if(*cons == cb->prod)
		return UTIL_CBUF_EMPTY;

	*c = cb->buffer[*cons];
	*cons = UTIL_CBUF_INC(*cons,cb->size);

	return UTIL_CBUF_OK;
}

cbuf_status_t cbuf_get_end(cbuf_t *cb,  uint16_t *cons)
{
	cb->cons = *cons;

	return UTIL_CBUF_OK;
}

int16_t cbuf_get_str_on_buffer_beg(cbuf_t *cb, uint16_t *cons, uint8_t **buf, uint16_t *buf_len, uint32_t tmrout_ms)
{
	uint8_t c;
	uint32_t tmr = hw_time_get();
	uint16_t p = 0;
	*cons = cb->cons;

	if(buf_len == 0)
	{
		*buf_len = 0;
		return -1;
	}

	// starting position
	*buf = &cb->buffer[*cons];

	do
	{
		if(cbuf_get_beg(cb,&c,cons) == UTIL_CBUF_OK)
		{
			if(++p >= *buf_len)
				return 1;			
		}
	} while (hw_time_elapsed(tmr,hw_time_get()) < tmrout_ms);

	*buf_len = p;
	return -1;
}

int16_t cbuf_get_str_on_buffer_end(cbuf_t *cb, uint16_t *cons)
{
	return cbuf_get_end(cb,cons);
}

#endif

#if 0
cbuf_t tst;
uint8_t tst_area[AT_CBUF_MAX];
cbuf_str_t list[3];

void hw_cbuf_test(void)
{
	cbuf_init(&tst,tst_area,AT_CBUF_MAX);

	cbuf_put(&tst,'a');
	cbuf_put(&tst,'b');
	cbuf_put(&tst,'c');
	cbuf_put(&tst,'O');
	cbuf_put(&tst,'K');
	cbuf_put(&tst,'\r');
	cbuf_put(&tst,'\n');
	cbuf_put(&tst,'e');
	cbuf_put(&tst,'f');
	cbuf_put(&tst,'g');

	// cbuf_find_str(&tst,(uint8_t*)"OK1\r\n",4,2000);

	list[0].str = (uint8_t *) "OK1\r\n";
	list[0].len = 5;
	list[1].str = (uint8_t *) "OK\r\n";
	list[1].len = 4;

	cbuf_find_multi_str(&tst,list,2,2000);
	
}
#endif

