
#pragma once

uint32_t cmd_parse_args(uint8_t * const cmdline, uint32_t size, uint32_t *argc, uint8_t *argv[], uint32_t max_args);
void cmd_proc(uint8_t * const cmdline, uint32_t size);

