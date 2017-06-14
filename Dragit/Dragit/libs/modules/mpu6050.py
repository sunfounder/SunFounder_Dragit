#!/usr/bin/python

import smbus
import math
import time

class MPU6050(object):
    """docstring for MPU6050"""
    # Power management registers
    power_mgmt_1 = 0x6b
    power_mgmt_2 = 0x6c
    bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
    address = 0x68       # This is the address value read via the i2cdetect command

    def __init__(self, address=0x68):
        # Now wake the 6050 up as it starts in sleep mode
        self.bus.write_byte_data(address, self.power_mgmt_1, 0)

    def read_byte(self, adr): #channel
        return self.bus.read_byte_data(self.address, adr)

    def read_word(self, adr):
        high = self.bus.read_byte_data(self.address, adr)
        low = self.bus.read_byte_data(self.address, adr+1)
        val = (high << 8) + low
        return val

    def read_word_2c(self, adr):
        val = self.read_word(adr)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val

    def dist(self, a,b):
        return math.sqrt((a*a)+(b*b))

    def get_y_rotation(self, x,y,z):
        radians = math.atan2(x, self.dist(y,z))
        return -math.degrees(radians)

    def get_x_rotation(self, x,y,z):
        radians = math.atan2(y, self.dist(x,z))
        return math.degrees(radians)

    def get_gyro_out(self):
        gyro_xout = self.read_word_2c(0x43)
        gyro_yout = self.read_word_2c(0x45)
        gyro_zout = self.read_word_2c(0x47)
        print "gyro_xout : ", gyro_xout, " scaled: ", (gyro_xout / 131)
        print "gyro_yout : ", gyro_yout, " scaled: ", (gyro_yout / 131)
        print "gyro_zout : ", gyro_zout, " scaled: ", (gyro_zout / 131)
        return (gyro_xout, gyro_yout, gyro_zout)

    def get_accel_out(self):
        accel_xout = self.read_word_2c(0x3b)
        accel_yout = self.read_word_2c(0x3d)
        accel_zout = self.read_word_2c(0x3f)

        accel_xout_scaled = accel_xout / 16384.0
        accel_yout_scaled = accel_yout / 16384.0
        accel_zout_scaled = accel_zout / 16384.0

        print "accel_xout: ", accel_xout, " scaled: ", accel_xout_scaled
        print "accel_yout: ", accel_yout, " scaled: ", accel_yout_scaled
        print "accel_zout: ", accel_zout, " scaled: ", accel_zout_scaled
        return (accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)

    def get_rotation_out(self):
        accel_xout_scaled, accel_yout_scaled, accel_zout_scaled = self.get_accel_out()
        x_rotation = self.get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
        y_rotation = self.get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
        print "x rotation: " , x_rotation
        print "y rotation: " , y_rotation
        return (x_rotation, y_rotation)

def test():
    my_mpu6050 = MPU6050()
    while True:
        my_mpu6050.get_gyro_out()
        my_mpu6050.get_accel_out()
        my_mpu6050.get_rotation_out()
        print("")
        time.sleep(1)

def destroy():
    pass

if __name__ == '__main__':
    try:
        test()
    except KeyboardInterrupt:
        destroy()
