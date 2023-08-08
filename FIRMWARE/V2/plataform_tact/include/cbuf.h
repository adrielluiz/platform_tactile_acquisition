
#pragma once

#ifdef __cplusplus
extern "C" {
#endif

typedef enum cbuf_status_s
{
    UTIL_CBUF_OK = 0,
    UTIL_CBUF_FULL,
    UTIL_CBUF_EMPTY,
	UTIL_CBUF_TMROUT,
} cbuf_status_t;

typedef struct cbuf_str_e
{
	uint8_t *str;
	uint16_t len;
	uint16_t n_match;	
} cbuf_str_t;

typedef struct cbuf_s
{
	volatile uint16_t prod;
	volatile uint16_t cons;
	uint16_t size;
    uint8_t *buffer;
} cbuf_t;


// use before functions, in global scope
#define CBUF_DECLARE(name,len)                 \
    static uint8_t name##buffer[len + 1];      \
    static cbuf_t name = {                     \
        .prod = 0, 								\
        .cons = 0, 								\
        .size = len+1,      	                \
        .buffer = (uint8_t *) name##buffer,     \
    }


cbuf_status_t cbuf_init(cbuf_t *cb);
cbuf_status_t cbuf_get(cbuf_t *cb, uint8_t *c);
cbuf_status_t cbuf_put(cbuf_t *cb, uint8_t c);
cbuf_status_t cbuf_flush(cbuf_t *cb);

#if 0
int16_t cbuf_find_str(cbuf_t *cb, uint8_t *str, uint16_t len, uint16_t *nb, uint32_t tmrout_ms);
int16_t cbuf_find_multi_str(cbuf_t *cb, cbuf_str_t *str_list, uint16_t len_list, uint32_t tmrout_ms);
int16_t cbuf_get_str_until_find(cbuf_t *cb, uint8_t *buf, uint16_t *buf_len,
                                     uint8_t *str, uint16_t len, uint32_t tmrout_ms);
int16_t cbuf_get_str(cbuf_t *cb, uint8_t *buf, uint16_t *buf_len, uint32_t tmrout_ms);
cbuf_status_t cbuf_get_beg(cbuf_t *cb, uint8_t *c, uint16_t *tail);
cbuf_status_t cbuf_get_end(cbuf_t *cb, uint16_t *tail);
int16_t cbuf_get_str_on_buffer_beg(cbuf_t *cb, uint16_t *tail, uint8_t **buf, uint16_t *buf_len, uint32_t tmrout_ms);
int16_t cbuf_get_str_on_buffer_end(cbuf_t *cb, uint16_t *tail);
cbuf_status_t cbuf_get_tmrout(cbuf_t *cb, uint8_t *c, uint32_t tmrout_ms);
#endif

#ifdef __cplusplus
}
#endif

