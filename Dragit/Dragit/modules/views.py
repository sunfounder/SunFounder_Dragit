# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from Dragit.sensors.Ultrasonic_Avoidance import Ultrasonic_Avoidance
from Dragit.sensors.Light_Follower import Light_Follower
from Dragit.sensors.Line_Follower import Line_Follower
from Dragit.picar import ADC

import time
import RPi.GPIO as GPIO
import sys, os

try:
    adc  = ADC(0x40)

    lf = Line_Follower()
    lt = Light_Follower()

    lt.analog_function = adc.read
    GPIO.setmode(GPIO.BCM)
    err_msg = ''

except Exception,e:
    err_msg = "Modules is not avalible"


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


def run(request):
    try:
        debug = ''
        action = None
        value0 = None
        value1 = None
        value2 = None
        result = None
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

        # ================ Ultrasonic avoide =================
        elif action == "ultra_distance":
            channel = value0
            result = ultra_get_distance(channel)

        # ================ Light Follower =================
        elif action == "light_follower_analog":
            channel = value0
            result = light_analog_index(channel)

        # ================ Line Follower =================
        elif action == "line_follower_analog":
            channel = value0
            result = line_analog_index(channel)

        elif action == "device_status":
            result = device_status()

    except Exception, e:
        result = '%s: %s'%(err_msg, e)
    finally:
        return HttpResponse(result)
