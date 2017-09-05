# -*- coding: utf-8 -*-
# pin connect:
#   module         pin       BCM_pin
#
#   ds18b20        sig       GPIO_4
#
#   IR_receiver    sig       GPIO_26
#
#   RTC_ds1302     SCL       GPIO_23
#                  I/O       GPIO_24
#                  RST       GPIO_25
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from Dragit.libs.modules.Ultrasonic_Avoidance import Ultrasonic_Avoidance
from Dragit.libs.modules.Light_Follower import Light_Follower
from Dragit.libs.modules.Line_Follower import Line_Follower
from Dragit.libs.modules.PCF8591 import PCF8591 as ADC
from Dragit.libs.modules.ds18b20 import DS18B20 as DS18B20
from Dragit.libs.modules.liquid_crystal_i2c import LiquidCrystal_I2C as LCD_I2C
from Dragit.libs.modules.dht11 import DHT11 as DHT11
from Dragit.libs.modules.mpu6050 import MPU6050 as MPU6050
from Dragit.libs.modules.rpi_time import DS1302 as DS1302
from Dragit.libs.modules.bmp280 import BMP280 as BMP280
from Dragit.libs.modules.bcm_gpio import BCM_GPIO as BCM_GPIO
from Dragit.libs.modules.rotary_encoder import RotaryEncoder as RotaryEncoder
from SunFounder_Emo import Emo as Emo

import pylirc
import time
import math
import RPi.GPIO as GPIO
import sys, os

ir_conf_path = "/etc/lirc/pylirc_conf"
ir_time_out = 1
ultrasonic_time_out = 2
buzz_note = {'C':262, 'D':294, 'E':330, 'F':350, 'G':393, 'A':441, 'B':495, 'C2':525}
read_ir_key_val = None

r_pin = 0
g_pin = 0
b_pin = 0
buzzer_chn = 0
i2c_lcd1602 = False
i2c_lcd2004 = False

try:
    # adc = ADC(0x48)
    #my_18b20 = DS18B20()

    lf = Line_Follower()
    lt = Light_Follower()
    sunfounder_emo = Emo()

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    err_msg = ''

except Exception,e:
    err_msg = "Modules is not avalible"

def ultrasonic_3pin(channel):
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

def pcf8591_write(addr, value):
    try:
        addr   = addr.encode('utf8')  # unicode to str
        addr   = int(addr, 16)         # Hex str to int
        value  = value.encode('utf8') # unicode to str
        value  = int(value, 10)  # Oct str to int
        #print ("addr: %s, %s" %(type(addr), addr))
        #print ("chn: %s, %s" %(type(chn), chn))
        adc  = ADC(addr)
        adc.write(value)
        print("[Modules] Analog write addr=%s, value=%s"%(addr, value))
    except:
        print("[Modules] Analog write address error")

    return value

def w1_temperature(index, unit):
    try:
        my_18b20 = DS18B20()
        index = int(index)
        my_18b20.unit = unit.encode('utf8')
        value = my_18b20.get_temperature(index)
        my_18b20 = 0
        return value
    except:
        return "Device not founded"

def setup_ultrasonic_4pin(trig, echo):
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

    GPIO.output(trig, 0)
    time.sleep(0.000002)

    GPIO.output(trig, 1)
    time.sleep(0.00001)
    GPIO.output(trig, 0)

def ultrasonic_4pin(t_pin, e_pin):
    trig = int(t_pin)
    echo = int(e_pin)
    setup_ultrasonic_4pin(trig, echo)
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
    dis = round(dis, 3)
    print("during = %s ,dis = %s cm"%(during, dis))
    return dis

def setup_i2c_lcd1602(addr=0x27):
    global i2c_lcd1602
    if not isinstance(i2c_lcd1602, LCD_I2C):
        try:
            i2c_lcd1602 = LCD_I2C(addr, 16, 2, bus_num=1) # init(slave address, bus_num, numlines=2)
            i2c_lcd1602.backlight()
        except:
            print("Can't init lcd1602, check i2c")
    return i2c_lcd1602

def i2c_lcd1602_print(pos_col, pos_row, words):
    global i2c_lcd1602
    setup_i2c_lcd1602()
    pos_col = int(pos_col)
    pos_row = int(pos_row)
    words   = words.encode('utf8')
    try:
        i2c_lcd1602.setCursor(pos_col, pos_row)
        i2c_lcd1602.show(words)
    except Exception, e:
        print e
        i2c_lcd1602 = False

def i2c_lcd1602_clear():
    global i2c_lcd1602
    setup_i2c_lcd1602()
    try:
        i2c_lcd1602.clear()
    except Exception, e:
        print e
        i2c_lcd1602 = False

def setup_i2c_lcd2004(addr=0x27):
    global i2c_lcd2004
    if not isinstance(i2c_lcd2004, LCD_I2C):
        try:
            i2c_lcd2004 = LCD_I2C(addr, 20, 4, bus_num=1) # init(slave address, bus_num, numlines=2)
            i2c_lcd2004.backlight()
        except:
            print("Can't init lcd2004, check i2c")
    return i2c_lcd2004

def i2c_lcd2004_print(pos_col, pos_row, words):
    global i2c_lcd2004
    setup_i2c_lcd2004()
    pos_col = int(pos_col)
    pos_row = int(pos_row)
    words   = words.encode('utf8')
    try:
        i2c_lcd2004.setCursor(pos_col, pos_row)
        i2c_lcd2004.show(words)
    except Exception, e:
        print e
        i2c_lcd2004 = False

def i2c_lcd2004_clear():
    global i2c_lcd2004
    setup_i2c_lcd2004()
    try:
        i2c_lcd2004.clear()
    except Exception, e:
        print e
        i2c_lcd2004 = False

def emo_show(byte_list):
    byte_list = byte_list.encode('utf8')
    byte_list = byte_list.split(',')
    for i in range(0,24):
        byte_list[i] = (int(byte_list[i]))
        #print("byte_list[%d] = %s"%(i, byte_list[i]))
    sunfounder_emo.show_bytes(byte_list)
    print(byte_list)

def emo_to_byte_list(emo):
    emo = emo.encode('utf8')
    if emo in sunfounder_emo.emotions._emotions.keys():
            _bits_list = sunfounder_emo.emotions.emotion(emo)
    if emo in sunfounder_emo.emotions._emotions.keys():
            _bits_list = sunfounder_emo.emotions.emotion(emo)

    # bit to byte
    _bytes = []
    if len(_bits_list) != 8:
        self._error("arguement should be list of 8 lines of strings")
    for _bits in _bits_list:
        _bits = _bits.replace(',', '').replace(' ', '')
        if len(_bits) != 24:
            self._error('every item in the list should be string with exact 24 "0" and "1" representing "off" and "on"')
        _byte0 = _bits[:8]
        _byte0 = int(_byte0, base=2)
        _bytes.append(_byte0)
        _byte1 = _bits[8:16]
        _byte1 = int(_byte1, base=2)
        _bytes.append(_byte1)
        _byte2 = _bits[16:]
        _byte2 = int(_byte2, base=2)
        _bytes.append(_byte2)
    # byte_list to str
    _bytes = str(_bytes)
    print(_bytes)
    return _bytes

def emo_make(byte_list):
    byte_list = byte_list.encode('utf8')
    byte_list = byte_list.split(',')
    for i in range(0,24):
        byte_list[i] = (int(byte_list[i]))
        #print("byte_list[%d] = %s"%(i, byte_list[i]))
    sunfounder_emo.show_bytes(byte_list)
    print(byte_list)
    return (byte_list)


def passive_buzzer(chn, freq, on_off):
    chn = int(chn)

    Buzz = BCM_GPIO(chn)

    if (on_off == 'off'):
        Buzz.end()
    else:
        Buzz.pwm_output(freq=int(freq))

def buzzer_play(chn, note, second):
    chn  = int(chn)
    sec  = float(second)
    note = note.encode('utf8')
    freq = buzz_note[note]

    Buzz = BCM_GPIO(chn)

    Buzz.pwm_output(freq=int(freq))
    time.sleep(sec)
    Buzz.end()

def dht11_read(pin,mode):
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
        if value == 1:
            print ("ERR_MISSING_DATA")
        elif value == 2:
            print ("ERR_CRC")
        return (False)

def dht11_module(pin,mode):
    for _ in range(10):
        value = dht11_read(pin,mode)
        if value:
            return value
    return "Value Error"

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

    if item == "acceleration x":
        accel_x_scaled = accel_out[0]
        return (accel_x_scaled)

    elif item == "acceleration y":
        accel_y_scaled = accel_out[1]
        return (accel_y_scaled)

    elif item == "acceleration z":
        accel_z_scaled = accel_out[2]
        return (accel_z_scaled)

    elif item == "x rotation":
        x_rotation = rotation_out[0]
        return (x_rotation)

    elif item == "y rotation":
        y_rotation = rotation_out[1]
        return (y_rotation)

    elif item == "gyroscope x":
        gyro_x = gyro_out[0]
        return (gyro_x)

    elif item == "gyroscope y":
        gyro_y = gyro_out[1]
        return (gyro_y)

    elif item == "gyroscope z":
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
    global read_ir_key_val
    GPIO.setup(26, GPIO.IN)
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
            read_ir_key_val = conf_key
            return conf_key
        elif (time.time()-timeout_start > ir_time_out):
            pylirc.exit()
            read_ir_key_val = None
            print "time out"
            return -1
        time.sleep(0.05)

def is_IR_received():
    result = ir_codes()
    if result == -1:
        print "[IR_receiver] time out"
        return 0
    else:
        print ("[IR_receiver] IR is received, %s"%read_ir_key_val)
        return 1

def IR_received_val():
    global read_ir_key_val
    received_val = read_ir_key_val
    #read_ir_key_val = None
    print ("[IR_receiver] IR is received, %s"%read_ir_key_val)
    return received_val

def thermitor(analogVal):
    analogVal = float(analogVal)
    B = 3950
    Tk0 = 273.15
    T0 = 25+ Tk0
    Vref = 3.3
    R0 = 10000
    Vr = Vref * float(analogVal) / 255
    print ("Vr = %s"%Vr)
    Rt = R0 * Vr / (Vref - Vr)
    print ("Rt = %s"%(Rt/1000))
    temp = B / (math.log(Rt/R0)+(B/T0))
    temp = temp - Tk0
    print 'temperature = ', temp, 'C'
    return temp

encoder = 0
def start_encoder(A_PIN, B_PIN, SW):
    a_pin = int(A_PIN)
    b_pin = int(B_PIN)
    sw    = int(SW)
    encoder = RotaryEncoder(a_pin, b_pin, sw)
    encoder.start()
    print encoder
    return encoder

def get_encoder_rotation(encoder):
    encoder = encoder
    try:
        return encoder.get_rotation()
    except:
        return "enconder not started"

def get_encoder_button(encoder):
    encoder = encoder
    try:
        return encoder.get_button()
    except:
        return "enconder not started"

def end_encoder(encoder):
    encoder = encoder
    try:
        encoder.end()
        print ("encoder ended")
    except:
        return "encoder not started"


def get_result(request):
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
    if action == "ultrasonic_3pin":
        channel = value0
        result  = ultrasonic_3pin(channel)

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

    elif action == "pcf8591_write":
        addr    = value0
        value   = value1
        result  = pcf8591_write(addr, value)

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

    # ================ thermitor =================
    elif action == "thermitor":
        analogVal = value0
        result  = thermitor(analogVal)

    # ================ W1 ds18b20 =================
    elif action == "w1":
        index = value0
        unit  = value1
        result  = w1_temperature(index, unit)

    # ================ ultra sonic trig & echo =================
    elif action == "ultrasonic_4pin":
        t_pin   = value0
        e_pin   = value1
        result  = ultrasonic_4pin(t_pin, e_pin)

    # ================ I2C LCD1602 =================
    elif action == "i2c_lcd1602_print":
        pos_row  = value0
        pos_col  = value1
        words    = value2
        result   = i2c_lcd1602_print(pos_col, pos_row, words)

    elif action == "i2c_lcd1602_clear":
        result   = i2c_lcd1602_clear()

    # ================ I2C LCD2004 =================
    elif action == "i2c_lcd2004_print":
        pos_row  = value0
        pos_col  = value1
        words    = value2
        result   = i2c_lcd2004_print(pos_col, pos_row, words)

    elif action == "i2c_lcd2004_clear":
        result   = i2c_lcd2004_clear()

    # ================ Emo led matrix =================
    elif action == "emo_show":
        byte_list = value0
        result    = emo_show(byte_list)

    elif action == "emo_maps":
        emo     = value0
        result  = emo_to_byte_list(emo)

    elif action == "emo_make":
        emo     = value0
        result  = emo_make(emo)

    # ================ passive buzzer =================
    elif action == "passive_buzzer":
        chn     = value0
        freq    = value1
        on_off  = value2
        result  = passive_buzzer(chn, freq, on_off)

    elif action == "buzzer_play":
        chn     = value0
        note    = value1
        second  = value2
        result  = buzzer_play(chn, note, second)

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
        _date    = value0
        _time    = value1
        result  = rtc_ds1302_set(_date, _time)

    # ================ IR key_pressed =================
    elif action == "is_IR_received":
        result = is_IR_received()

    elif action == "IR_received_val":
        result  = IR_received_val()

    global encoder
    # ================ rotary encoder =================
    if action == "encoder_start":
        A_PIN  = value0
        B_PIN  = value1
        SW_PIN = value2
        if encoder == 0:
            encoder = start_encoder(A_PIN, B_PIN, SW_PIN)
        result = "start encoder %s %s %s"%(A_PIN, B_PIN, SW_PIN)
        print result

    elif action == "encoder_rotation":
        try:
            result = get_encoder_rotation(encoder)
            print result
        except:
            result = "encoder not started"

    elif action == "encoder_button":
        try:
            result = get_encoder_button(encoder)
            print result
        except:
            result = "encoder not started"

    elif action == "encoder_end":
        try:
            result  = end_encoder(encoder)
            encoder = 0
            print result
        except:
            result = "encoder not started"


    return result

def run_with_try(request):
    try:
        result = get_result(request)
    except Exception, e:
        result = '%s: %s'%(err_msg, e)
    finally:
        print result
        return HttpResponse(result)

def run(request):
    return HttpResponse(get_result(request))
    #return run_with_try(request)
