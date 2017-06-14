# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from Dragit.libs.modules.Ultrasonic_Avoidance import Ultrasonic_Avoidance
from Dragit.libs.modules.Light_Follower import Light_Follower
from Dragit.libs.modules.Line_Follower import Line_Follower
from Dragit.libs.modules.PCF8591 import PCF8591 as ADC
from Dragit.libs.modules.ds18b20 import DS18B20 as DS18B20
import Dragit.libs.modules.i2c_lcd as LCD1602
from Dragit.libs.modules.dht11 import DHT11 as DHT11
from Dragit.libs.modules.mpu6050 import MPU6050 as MPU6050
from Dragit.libs.modules.rpi_time import DS1302 as DS1302
from Dragit.libs.modules.bmp280 import BMP280 as BMP280

import pylirc
import time
import RPi.GPIO as GPIO
import sys, os

ir_conf_path = "/etc/lirc/pylirc_conf"
ir_time_out = 5
ultrasonic_time_out = 2

try:
    # adc = ADC(0x48)
    #my_18b20 = DS18B20()

    lf = Line_Follower()
    lt = Light_Follower()

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    r_pin = 17
    g_pin = 18
    b_pin = 27
    buzzer_chn = -1
    err_msg = ''
    num = 0
    num2 = 0

except Exception,e:
    err_msg = "Modules is not avalible"

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def setup_rgb_led(r_pin=17, g_pin=18, b_pin=27):
    print ("setup rgb led r:%s g:%s b:%s"%(r_pin, g_pin, b_pin))
    global p_R, p_G, p_B
    pins = (int(r_pin), int(g_pin), int(b_pin))
    for i in range(0,3):
        GPIO.setup(pins[i], GPIO.OUT)
        #GPIO.output(pins[i], GPIO.HIGH)
    p_R = GPIO.PWM(pins[0], 6000)
    p_G = GPIO.PWM(pins[1], 6000)
    p_B = GPIO.PWM(pins[2], 6000)

    p_R.start(0)      # Initial duty Cycle = 0(leds off)
    p_G.start(0)
    p_B.start(0)

def set_rgb_color(R_val=0, G_val=0, B_val=0):   # For example : col = 0x112233
    #R_val = (col & 0xff0000) >> 16
    #G_val = (col & 0x00ff00) >> 8
    #B_val = (col & 0x0000ff) >> 0

    R_val = map(R_val, 0, 255, 0, 100)
    G_val = map(G_val, 0, 255, 0, 100)
    B_val = map(B_val, 0, 255, 0, 100)

    print ("R_duty=%d G_duty=%d B_duty=%d "%(R_val, G_val, B_val))
    p_R.ChangeDutyCycle(R_val)
    p_G.ChangeDutyCycle(G_val)
    p_B.ChangeDutyCycle(B_val)

def rgb_led(r, g, b, com_pol, color):
    global r_pin, g_pin, b_pin
    if (r == r_pin) and (g == g_pin) and (b == b_pin):
        pass
    else:
        r_pin = r
        g_pin = g
        b_pin = b
        setup_rgb_led(r_pin, g_pin, b_pin)

    color = color[5:-1].split(',')
    for i in range(0,len(color)):   # unicode to int
        color[i] = int(color[i])
    #print ("%s %s"%(type(color),color))
    R_val = color[0]
    G_val = color[1]
    B_val = color[2]
    if com_pol == 'cathode':
        R_val = 255 - R_val
        G_val = 255 - G_val
        B_val = 255 - B_val
    print ("R_val=%d G_val=%d B_val=%d "%(R_val,G_val,B_val))
    return set_rgb_color( R_val, G_val, B_val)

def setup_dual_led(r_pin, g_pin):
    try:
        GPIO.setup(r_pin, GPIO.OUT)
        GPIO.setup(g_pin, GPIO.OUT)
    except:
        pass
    print ("setup dual led r:%s g:%s"%(r_pin, g_pin))

def set_dual_color(r, g, com_pol, col):
    if com_pol == 0:
        on_val = GPIO.HIGH
        off_val = GPIO.LOW
    elif com_pol == 1:
        on_val = GPIO.LOW
        off_val = GPIO.HIGH

    if col == 'red':
        GPIO.output(r, on_val)
        GPIO.output(g, off_val)
        print("%s pin, %s \n%s pin, %s "%(r, on_val, g, off_val))
    elif col == 'green':
        GPIO.output(r, off_val)
        GPIO.output(g, on_val)
        print("%s pin, %s \n%s pin, %s "%(r, off_val, g, on_val))
    elif col == 'off':
        GPIO.output(r, off_val)
        GPIO.output(g, off_val)
        print("%s pin, %s \n%s pin, %s "%(r, off_val, g, off_val))

def dual_color_led(r, g, com_pol, col):
    r = int(r)
    g = int(g)
    com_pol = int(com_pol)
    col = col.encode('utf8')
    setup_dual_led(r, g)
    set_dual_color(r, g, com_pol, col)


def ultra_get_distance(channel):
    print("Get Ultrasonic sensor distance ")
    ua = Ultrasonic_Avoidance(int(channel))
    def get_distance(mount = 10):
        sum_a = []
        for i in range(mount):
            a = ua.distance()
            #print '    %s' % a
            sum_a.append(a)
        sum_a.sort()
        sum_a = sum_a[1:-1]
        return int(sum(sum_a)/(mount-2))
    result = get_distance(mount=10)
    print("[Modules] Get Ultrasonic sensor channel: %s, distance: %s"%(channel, result))
    return result

def light_analog_index(channel):
    adc  = ADC(0x40)
    lt.analog_function = adc.read
    result = lt.read_analogs()
    if channel != None:
        value = result[int(channel)]
        print("[Modules] Light_Follower channel:%s, value:%s"%(channel, value))
    else:
        value = str(result).replace("'", '').strip('[]').replace(' ','')
        print("[Modules] Light_Follower value:%s"%(value))
    return value

def line_analog_index(channel):
    result = lf.read_analogs()
    if channel != None:
        value = result[int(channel)-1]
        print("[Modules] Light_Follower channel:%s, value:%s"%(channel, value))
    else:
        value = str(result).replace("'", '').strip('[]').replace(' ','')
        print("[Modules] Light_Follower value:%s"%(value))
    return value

def pcf8591_read(addr, chn):
    try:
        addr = addr.encode('utf8')  # unicode to str
        addr = int(addr, 16)         # Hex str to int
        chn  = chn.encode('utf8') # unicode to str
        chn  = int(chn, 10)  # Oct str to int
        #print ("addr: %s, %s" %(type(addr), addr))
        #print ("chn: %s, %s" %(type(chn), chn))
        adc  = ADC(addr)
        if chn != None:
            value = adc.read(chn)
            print("[Modules] Analog read addr=%s, chn=%s, value=%s"%(addr, chn, value))
        else:
            value = None
            print("[Modules] Analog read no channel")
    except:
        value = None
        print("[Modules] Analog read address error")

    return value

def w1_temperature(index, unit):
    my_18b20 = DS18B20(log=False)
    index = int(index)
    my_18b20.unit = unit.encode('utf8')
    value = my_18b20.get_temperature(index)
    return value

def setup_ultrasonic(trig,echo):
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

    GPIO.output(trig, 0)
    time.sleep(0.000002)

    GPIO.output(trig, 1)
    time.sleep(0.00001)
    GPIO.output(trig, 0)

def ultrasonic_ranging(t_pin, e_pin):
    trig = int(t_pin)
    echo = int(e_pin)
    setup_ultrasonic(trig, echo)
    timeout_start = time.time()
    while GPIO.input(echo) == 0:
        if (time.time()-timeout_start > ultrasonic_time_out):
            return -1
            print("time out")
    time1 = time.time()
    print("time1 = %d"%time1)
    timeout_start = time.time()
    while GPIO.input(echo) == 1:
        if (time.time()-timeout_start > ultrasonic_time_out):
            print("time out")
            return -1
    time2 = time.time()
    print("time2 = %d"%time2)
    during = time2 - time1
    dis = (during *340 *100 /2)
    print("during = %s ,dis = %s cm"%(during, dis))
    return dis

def setup_i2c_lcd(addr=0x27):
    LCD1602.init(addr, 1)   # init(slave address, background light)

def set_i2c_lcd(pos_col, pos_row, words):
    LCD1602.write(pos_col, pos_row, words)

def i2c_lcd_print(pos_col, pos_row, words):
    setup_i2c_lcd()
    pos_col = int(pos_col)
    pos_row = int(pos_row)
    words   = words.encode('utf8')
    set_i2c_lcd(pos_col, pos_row, words)

def setup_buzzer(buzzer_chn=17):
    print ("setup passive buzzer %s"%buzzer_chn)
    global Buzz
    GPIO.setup(buzzer_chn, GPIO.OUT)
    Buzz = GPIO.PWM(buzzer_chn, 440)
    Buzz.start(0)
    print ("setup success")

def passive_buzzer(chn, freq, on_off):
    global buzzer_chn, num, num2
    chn = int(chn)
    if (chn == buzzer_chn):
        pass
    else:
        buzzer_chn = chn
        setup_buzzer(buzzer_chn)

    if (on_off == 'off'):
        Buzz.stop()
    else:
        Buzz.ChangeFrequency(int(freq))

def dht11_module(pin,mode):
    pin = int(pin)
    mode = mode.encode('utf8')

    instance = DHT11(pin)
    value = instance.read()

    if value.is_valid():
        if mode == 'temperature C':
            value = value.temperature
            print("Temperature: %d C" % value)
            return (value)
        elif mode == 'temperature F':
            value = value.temperature
            temperature_f = value * 9.0 / 5.0 + 32.0
            print("Temperature: %d F" % temperature_f)
            return (temperature_f)
        elif mode == 'humidity':
            value = value.humidity
            print("Humidity: %d %%" % value)
            return (value)
    else:
        value = value.error_code
        print("Error: %d" % value)
        return ("value not good")

def bmp280_sensor(item):
    bmp = BMP280()
    chip_id, chip_version = bmp.read_id()

    if chip_id == 88:
        bmp.reg_check()

        temperature, pressure = bmp.read()
        print("Temperature : %2.2f `C" % temperature)
        print("Pressure    : %5.4f mbar" % pressure)
        if item == 'temperature':
            print("Temperature : %2.2f `C" % temperature)
            return temperature
        elif item == 'pressure':
            print("Pressure    : %5.4f mbar" % pressure)
            return pressure
    else:
        print("Error")
        print("Chip ID     : %d" % chip_id)
        print("Version     : %d" % chip_version)
        time.sleep(0.2)

def mpu6050_sensor(item):
    my_mpu6050 = MPU6050()
    item = item.encode('utf8')
    accel_out = my_mpu6050.get_accel_out()
    rotation_out = my_mpu6050.get_rotation_out()
    gyro_out = my_mpu6050.get_gyro_out()

    if item == "accel_x_scaled":
        accel_x_scaled = accel_out[0]
        return (accel_x_scaled)

    elif item == "accel_y_scaled":
        accel_y_scaled = accel_out[1]
        return (accel_y_scaled)

    elif item == "accel_z_scaled":
        accel_z_scaled = accel_out[2]
        return (accel_z_scaled)

    elif item == "x_rotation":
        x_rotation = rotation_out[0]
        return (x_rotation)

    elif item == "y_rotation":
        x_rotation = rotation_out[1]
        return (y_rotation)

    elif item == "gyro_x":
        gyro_x = gyro_out[0]
        return (gyro_x)

    elif item == "gyro_y":
        gyro_y = gyro_out[1]
        return (gyro_y)

    elif item == "gyro_z":
        gyro_z = gyro_out[2]
        return (gyro_z)

def rtc_ds1302_get(item):
    item = item.encode('utf8')
    rtc = DS1302()
    dt = rtc.get_datetime()
    print ("Your ds1302 date and time :%s"%dt)
    if item == 'year':
        return dt.year
    elif item == 'month':
        return dt.month
    elif item == 'day':
        return dt.day
    elif item == 'hour':
        return dt.hour
    elif item == 'minute':
        return dt.minute
    elif item == 'second':
        return dt.second

def rtc_ds1302_set(date, time):
    date = date.split(',')
    time = time.split(',')
    for i in range(0,len(date)):
        date[i] = int(date[i])
    for i in range(0,len(time)):
        time[i] = int(time[i])
    #print(type(date), (date))
    #print(type(time), (time))
    rtc = DS1302()
    rtc.set_datetime(date, time)
    dt = rtc.get_datetime()
    print ("set ds1302 success \n time: %s"%dt)

def ir_codes():
    pylirc.init("my_lirc", ir_conf_path, 0)
    ir_codes = pylirc.nextcode(1)
    # while with time out
    timeout_start = time.time()
    while True:
        ir_codes = pylirc.nextcode(1)
        if ir_codes != None:
            conf_key = ir_codes[0]['config']
            #print("ircodes = %s"%ir_codes)
            #print(type(conf_key))
            pylirc.exit()
            return conf_key
        elif (time.time()-timeout_start > ir_time_out):
            pylirc.exit()
            return "time out"
        time.sleep(0.05)


def run(request):
    try:
        debug = ''
        action = None
        result = None
        value0 = None
        value1 = None
        value2 = None
        value3 = None
        value4 = None
        if 'action' in request.GET:
            action = request.GET['action']
            print("Get action: %s"%action)
        if 'value0' in request.GET:
            value0 = request.GET['value0']
            print("Get value0: %s"%value0)
        if 'value1' in request.GET:
            value1 = request.GET['value1']
            print("Get value1: %s"%value1)
        if 'value2' in request.GET:
            value2 = request.GET['value2']
            print("Get value2: %s"%value2)
        if 'value3' in request.GET:
            value3 = request.GET['value3']
            print("Get value3: %s"%value3)
        if 'value4' in request.GET:
            value4 = request.GET['value4']
            print("Get value4: %s"%value4)

        # ================ Ultrasonic avoide =================
        if action == "ultra_distance":
            channel = value0
            result  = ultra_get_distance(channel)

        # ================ Light Follower =================
        elif action == "light_follower_analog":
            channel = value0
            result  = light_analog_index(channel)

        # ================ Line Follower =================
        elif action == "line_follower_analog":
            channel = value0
            result  = line_analog_index(channel)

        elif action == "device_status":
            result  = device_status()

        # ================ analog input sensor =================
        elif action == "pcf8591":
            addr    = value0
            channel = value1
            result  = pcf8591_read(addr, channel)

        # ================ RGB led =================
        elif action == "rgb_led":
            r_pin = value0
            g_pin = value1
            b_pin = value2
            com_pol = value3
            color = value4
            result  = rgb_led(r_pin, g_pin, b_pin, com_pol, color)

        elif action == "dual_color_led":
            r_pin = value0
            g_pin = value1
            com_pol = value2
            color = value3
            result  = dual_color_led(r_pin, g_pin, com_pol, color)

        # ================ W1 ds18b20 =================
        elif action == "w1":
            index = value0
            unit  = value1
            result  = w1_temperature(index, unit)

        # ================ ultra sonic trig & echo =================
        elif action == "ultrasonic_ranging":
            t_pin   = value0
            e_pin   = value1
            result  = ultrasonic_ranging(t_pin, e_pin)

        # ================ I2C LCD1602 =================
        elif action == "i2c_lcd":
            pos_row  = value0
            pos_col  = value1
            words    = value2
            result   = i2c_lcd_print(pos_col, pos_row, words)

        # ================ passive buzzer =================
        elif action == "passive_buzzer":
            chn     = value0
            freq    = value1
            on_off  = value2
            result  = passive_buzzer(chn, freq, on_off)

        # ================ dht11 module =================
        elif action == "dht11_module":
            pin     = value0
            mode    = value1
            result  = dht11_module(pin, mode)

        # ================ bmp280 =================
        elif action == "bmp280_sensor":
            item    = value0
            result  = bmp280_sensor(item)

        # ================ mpu6050 =================
        elif action == "mpu6050_sensor":
            item    = value0
            result  = mpu6050_sensor(item)

        # ================ rtc_ds1302 =================
        elif action == "rtc_ds1302_get":
            item    = value0
            result  = rtc_ds1302_get(item)

        elif action == "rtc_ds1302_set":
            date    = value0
            time    = value1
            result  = rtc_ds1302_set(date, time)

        # ================ rtc_ds1302 =================
        elif action == "ir_codes":
            result  = ir_codes()


    except Exception, e:
        result = '%s: %s'%(err_msg, e)
    finally:
        print result
        return HttpResponse(result)
