#include <Arduino.h>
#include<Wire.h>
#include "mpu.h"

const int MPU_addr=0x68; //Endereço do sensor
mpu_data_t mpu_dat;

void mpu_init(void)
{
    Wire.setSCL(PB6);
    Wire.setSDA(PB7);

    Wire.begin(); //Inicia a comunicação I2C
    Wire.beginTransmission(MPU_addr); //Começa a transmissao de dados para o sensor
    Wire.write(0x6B); // registrador PWR_MGMT_1
    Wire.write(0); // Manda 0 e "acorda" o MPU 6050
    Wire.endTransmission(true);
}

void mpu_read(void)
{
    Wire.beginTransmission(MPU_addr); //Começa a transmissao de dados para o sensor
    Wire.write(0x3B); // registrador dos dados medidos (ACCEL_XOUT_H)
    Wire.endTransmission(false);
    Wire.requestFrom(MPU_addr,14,true); // faz um "pedido" para ler 14 registradores, que serão os registrados com os dados medidos
    mpu_dat.AcX=Wire.read()<<8|Wire.read(); // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)
    mpu_dat.AcY=Wire.read()<<8|Wire.read(); // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
    mpu_dat.AcZ=Wire.read()<<8|Wire.read(); // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)
    mpu_dat.Tmp=Wire.read()<<8|Wire.read(); // 0x41 (TEMP_OUT_H) & 0x42 (TEMP_OUT_L)
    mpu_dat.GyX=Wire.read()<<8|Wire.read(); // 0x43 (GYRO_XOUT_H) & 0x44 (GYRO_XOUT_L)
    mpu_dat.GyY=Wire.read()<<8|Wire.read(); // 0x45 (GYRO_YOUT_H) & 0x46 (GYRO_YOUT_L)
    mpu_dat.GyZ=Wire.read()<<8|Wire.read(); // 0x47 (GYRO_ZOUT_H) & 0x48 (GYRO_ZOUT_L)

    mpu_dat.Tmp = (mpu_dat.Tmp/340.00)+36.53; //Equação da temperatura em Cº de acordo com o datasheet
}
