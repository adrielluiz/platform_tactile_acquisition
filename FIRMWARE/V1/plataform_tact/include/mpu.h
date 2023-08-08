#pragma once

void mpu_init(void);
void mpu_read(void);

typedef struct mpu_data_e
{
    int16_t AcX;
    int16_t AcY;
    int16_t AcZ;
    int16_t Tmp;
    int16_t GyX;
    int16_t GyY;
    int16_t GyZ; 
}mpu_data_t;

mpu_data_t* mpu_get(void);


