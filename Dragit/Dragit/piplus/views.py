# Create your views here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.http import HttpResponse

import RPi.GPIO as GPIO
import Dragit.libs.piplus.piplus as plus
from Dragit.libs.modules.ds18b20 import DS18B20 as DS18B20

import time

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    lcd_flag = False
    err_msg = ''

except Exception,e:
    print e
    err_msg = "Modules is not avalible"

def buzzer_on_off(port, status):
    buzzer = plus.Buzzer(port)
    if status == "on":
        buzzer.on()
    else:
        buzzer.off()

def buzzer_morsecode(port, morsecode, speed):
    buzzer = plus.Buzzer(port)
    code = morsecode.encode('utf8')
    if speed == 'slow':
        speed = plus.SLOW
    else:
        speed = plus.FAST
    #buzzer.morsecode(code, speed)
    #buzzer.beep(times=10)
    for x in range(0,10):
        buzzer.on()
        print ('on')
        time.sleep(1)
        buzzer.off()
        print ('    off')
        time.sleep(1)

def led_ring_pwm(port, led_on_list):
    led_ring = plus.LED_Ring(port)
    led_on_list = led_on_list.split(",")
    for x in range(0,len(led_on_list)):
        led_on_list[x] = int(led_on_list[x])
    #print (led_on_list[0])
    #print (led_on_list[1])
    #print (led_on_list[2])
    #print ('[0]==0:', led_on_list[0]==0)
    #print led_on_list, type(led_on_list)
    led_ring.on(led_on_list)

def led_ring_on(port, led_on_list):
    led_ring = plus.LED_Ring(port)
    led_on_list = led_on_list.encode('utf8')
    led_on_list = led_on_list.split(",")
    #print(led_on_list[0])
    #print (led_on_list[1])
    #print (led_on_list[2])
    #print ("[0]==false", led_on_list[0]=='false')
    #print led_on_list, type(led_on_list)
    for x in range(0,len(led_on_list)):
        if led_on_list[x] == 'false':
            led_on_list[x] = 0
        else:
            led_on_list[x] = 100
    print ("led_on_list: ", led_on_list)
    led_ring.on(led_on_list)

def led_ring_spin(port, style, direct, delay):
    led_ring = plus.LED_Ring(port)

    if style == "SINGLE":
        _ring = led_ring.SINGLE()
    if style == "STAR":
        _ring = led_ring.STAR()

    if direct == "cw":
        w = 0
    else:
        w = 1

    dt = float(delay)
    led_ring.spin(_ring, w, dt)

def led_ring_breath(port, delay):
    led_ring = plus.LED_Ring(port)
    dt = float(delay)
    led_ring.breath(dt)

def led_ring_meter(port, value, bright):
    led_ring = plus.LED_Ring(port)
    value = float(value)
    bright = int(bright)
    led_ring.meter(value, bright)


def led_bar_graph_meter(port, value):
    led_bar_graph = plus.LED_Bar_Graph(port)
    value = float(value)
    led_bar_graph.meter(value)

def led_bar_graph_pulse(port, value):
    led_bar_graph = plus.LED_Bar_Graph(port)
    value = float(value)
    led_bar_graph.pulse(value)


def rgb_off(port):
    rgb = plus.RGB_LED(port)
    rgb.off()

def rgb_rgb(port, r, g, b):
    rgb = plus.RGB_LED(port)
    r = int(r)
    g = int(g)
    b = int(b)
    if r > 100:
        r = 100
    elif r < 0:
        r = 0
    if g > 100:
        g = 100
    elif g < 0:
        g = 0
    if b > 100:
        b = 100
    elif b < 0:
        b = 0
    rgb.rgb(r, g, b)

def rgb_hsb(port, h, s, b):
    rgb = plus.RGB_LED(port)
    h = float(h)
    s = float(s)
    b = float(b)
    if h > 360:
        h = h%360
    elif h < 0:
        h = 0
    if s > 1:
        s = 1
    elif s < 0:
        s = 0
    if b > 1:
        b = 1
    elif b < 0:
        b = 0
    rgb.hsb(h, s, b)

def rgb_breath(port, r, g, b, dt):
    rgb = plus.RGB_LED(port)
    r = int(r)
    g = int(g)
    b = int(b)
    dt = float(dt)
    if r > 100:
        r = 100
    elif r < 0:
        r = 0
    if g > 100:
        g = 100
    elif g < 0:
        g = 0
    if b > 100:
        b = 100
    elif b < 0:
        b = 0
    rgb.breath(r, g, b, dt)


def buttons(port):
    pass

def rotary_encoder(port):
    pass

def joystick():
    jstk = plus.Joystick()
    return jstk.get_status()

def photoresistor():
    resistor = plus.Photoresistor()
    return resistor.brightness()

def slide_potentiometers(item):
    sp = plus.Slide_Potentiometers()
    sp1, sp2, sp3 = sp.get_value(1, 2, 3)
    item = item.encode('utf8')
    if item == 'sp1':
        return sp1
    elif item == 'sp2':
        return sp2
    elif item == 'sp3':
        return sp3

def sound_sensor():
    sound_sensor = plus.Sound_Sensor()
    return sound_sensor.read()


def lcd_print(col0, word0, col1, word1):
    lcd = plus.LCD1602()
    col0  = int(col0)
    col1  = int(col1)
    word0 = word0.encode('utf8')
    word1 = word1.encode('utf8')
    lcd.write(col0, 0, word0)
    lcd.write(col1, 1, word1)

def lcd_clear():
    lcd = plus.LCD1602()
    lcd.clear()


def motion_sensor(item):
    try:
        motion_sensor = plus.Motion_Sensor()
        if   item == 'gyroscope x':
            return motion_sensor.get_gyro()[0]
        elif item == 'gyroscope y':
            return motion_sensor.get_gyro()[1]
        elif item == 'gyroscope z':
            return motion_sensor.get_gyro()[2]
        elif item == 'acceleration x':
            return motion_sensor.get_accel()[0]
        elif item == 'acceleration y':
            return motion_sensor.get_accel()[1]
        elif item == 'acceleration z':
            return motion_sensor.get_accel()[2]
        elif item == 'x rotation':
            return motion_sensor.get_rotation()[0]
        elif item == 'y rotation':
            return motion_sensor.get_rotation()[1]
    except:
        return "Device not founded"

'''
def ds18b20(unit):
    ds18b20 = plus.DS18B20()   # zu se
    unit = unit.encode('utf8')
    if unit == 'c':
        return ds18b20.get_temperature(unit=0)
    elif unit == 'f':
        return ds18b20.get_temperature(unit=1)
'''
def ds18b20(unit):
    try:
        my_18b20 = DS18B20()
        my_18b20.unit = unit.encode('utf8')
        value = my_18b20.get_temperature(index=0)
        my_18b20 = 0
        return value
    except:
        return "Device not founded"




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

    # ================ plus_buzzer =================
    if action == "plus_buzzer_on_off":
        port   = value0
        status = value1
        result = buzzer_on_off(port, status)

    if action == "plus_buzzer_morsecode":
        port      = value0
        morsecode = value1
        speed     = value2
        result    = buzzer_morsecode(port, morsecode, speed)

    # ================ plus_led_ring =================
    elif action == "plus_led_ring_on":
        port    = value0
        led_list= value1
        result  = led_ring_on(port, led_list)

    elif action == "plus_led_ring_pwm":
        port    = value0
        led_list= value1
        result  = led_ring_pwm(port, led_list)

    elif action == "plus_led_ring_spin":
        port    = value0
        style   = value1
        direct  = value2
        delay   = value3
        result  = led_ring_spin(port, style, direct, delay)

    elif action == "plus_led_ring_breath":
        port    = value0
        delay   = value1
        result  = led_ring_breath(port, delay)

    elif action == "plus_led_ring_meter":
        port    = value0
        value   = value1
        bright  = value2
        result  = led_ring_meter(port, value, bright)

    # ================ plus_led_bar graph ================
    elif action == "plus_led_bar_graph_meter":
        port    = value0
        value   = value1
        result  = led_bar_graph_meter(port, value)

    elif action == "plus_led_bar_graph_pulse":
        port    = value0
        value   = value1
        result  = led_bar_graph_pulse(port, value)

    # ================ plus_rgb ====================
    elif action == "plus_rgb_off":
        port    = value0
        result  = rgb_off(port)

    elif action == "plus_rgb_rgb":
        port    = value0
        r       = value1
        g       = value2
        b       = value3
        result  = rgb_rgb(port, r, g, b)

    elif action == "plus_rgb_hsb":
        port    = value0
        h       = value1
        s       = value2
        b       = value3
        result  = rgb_hsb(port, h, s, b)

    elif action == "plus_rgb_breath":
        port    = value0
        r       = value1
        g       = value2
        b       = value3
        dt      = value4
        result  = rgb_breath(port, r, g, b, dt)

    # ================ plus_buttons ========================
    elif action == "plus_buttons":
        port    = value0
        result  = buttons(port)

    # ================ plus_rotary_encoder =================
    elif action == "plus_rotary_encoder":
        port    = value0
        result  = rotary_encoder(port)

    # ================ plus_joystick ======================
    elif action == "plus_joystick":
        result  = joystick()

    # ================ plus_photoresistor =================
    elif action == "plus_photoresistor":
        result  = photoresistor()

    # ================ plus_slide_potentiometers ==========
    elif action == "plus_slide_potentiometers":
        item    = value0
        result  =  slide_potentiometers(item)

    elif action == "plus_sound_sensor":
        result  =  sound_sensor()

    # ================ plus_lcd1602 =================
    elif action == "plus_lcd1602_print":
        col0    = value0
        word0   = value1
        col1    = value2
        word1   = value3
        result  = lcd_print(col0, word0, col1, word1)

    elif action == "plus_lcd1602_clear":
        result   = lcd_clear()

    # ================ plus_motion_sensor =================
    elif action == "plus_motion_sensor":
        item    = value0
        result  = motion_sensor(item)

    # ================ plus_ds18b20 =================
    elif action == "plus_ds18b20":
        unit    = value0
        result  = ds18b20(unit)


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