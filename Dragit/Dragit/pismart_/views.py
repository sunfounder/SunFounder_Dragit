# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.http import HttpResponse

import RPi.GPIO as GPIO
import time
import sys, os
import threading

try:
    from pismart.pismart import PiSmart
    from pismart.led import  LED
    from pismart.motor import  Motor
    from pismart.servo import  Servo
    from pismart.pwm import  PWM
    from pismart.adc import  ADC
    from pismart.tts import  TTS
    from pismart.stt import  STT

    D_CHANNEL = {"0":17, "1":18, "2":22, "3":27, "4":23, "5":24, "6":25, "7":4,}
    D_STATE   = {"HIGH":GPIO.HIGH, "LOW":GPIO.LOW}

    GPIO.setmode(GPIO.BCM)
    pismart = PiSmart()
    pico    = TTS('pico')

    sps_file_path = "/opt/SunFounder_Dragit/Dragit/dictionary.sps"
    #os.system("cp %s ./"%sps_file_path)
    stt     = STT('dictionary', dictionary_update=True)

    pismart.speaker_switch(0)  # 1:on 0:off
    pismart.servo_switch(1)
    pismart.pwm_switch(1)
    pismart.motor_switch(1)

    pismart.speaker_volume = 100
    pismart.capture_volume = 100

    def stt_recognize():
        while True:
            print("Thread start")
            stt.recognize()

    power_voltage = pismart.power_voltage
    err_msg = ''
    t = threading.Thread(target=stt_recognize,name="Recognize")
    t.daemon = True
    t.start()
    print("Current Thread: %s"%threading.current_thread().name)
except Exception,e:
    err_msg = "PiSmart is not avalible"
'''
def init_pismart(pwm=1,motor=1,speaker=1):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    pismart.servo_switch(pwm)
    pismart.pwm_switch(pwm)
    pismart.motor_switch(motor)
    pismart.speaker_switch(speaker)

    pismart.speaker_volume = 100
    pismart.capture_volume = 100

    power_voltage = pismart.power_voltage
'''

def set_led_brightness(brightness):
    if brightness < 0:
        brightness = 0
    elif brightness > 100:
        brightness = 100

    led = LED()
    led.brightness = int(brightness)
    msg = "[PiSmart] Set LED brightness %d"%(brightness)
    print(msg)

def led_off():
    led = LED()
    led.off()
    msg = "[PiSmart] Set LED off"
    print(msg)

def motor_run(motor_chn, speed):
    #pismart.motor_switch(1)
    # motor库中有速度正负和限值的处理。
    if motor_chn == "A":
        MotorA = Motor(Motor.MotorA)
        MotorA.speed = int(speed)
    elif motor_chn == "B":
        MotorB = Motor(Motor.MotorB)
        MotorB.speed = int(speed)
    elif motor_chn == "both":
        MotorA = Motor(Motor.MotorA)
        MotorA.speed = int(speed)
        MotorB = Motor(Motor.MotorB)
        MotorB.speed = int(speed)
    msg = "[PiSmart] Set Motor %s at speed %d"%(motor_chn, speed)
    print(msg)

def pwm_output(pwm_channel, value):
    channel = int(pwm_channel)
    value   = int(value)
    # pwm 库有value限值的处理
    pwm = PWM(channel)
    pwm.value = value
    msg = "[PiSmart PWM chn: %s value: %s "%(channel, value)
    print(msg)

def servo_turn(servo_channel, angle):
    #pismart.servo_switch(1)
    channel = int(servo_channel)
    angle = int(angle)
    # servo 库有value限值的处理
    servo = Servo(channel)
    servo.angle = angle
    msg = "[PiSmart] Set Servo %s to %d degree"%(channel, angle)
    print(msg)

def set_digital(d_chn, d_state):
    GPIO.setup(D_CHANNEL[d_chn], GPIO.OUT)
    GPIO.output(D_CHANNEL[d_chn],D_STATE[d_state])
    msg = "[PiSmart] Set Digital %s to %s"%(d_chn, d_state)
    print(msg)

def get_digital(d_chn):
    GPIO.setup(D_CHANNEL[d_chn], GPIO.IN)
    state = GPIO.input(D_CHANNEL[d_chn])
    msg = "[PiSmart] Read Digital %s : %s"%(d_chn, state)
    print(msg)
    return state

def get_analog(analog_channel):
    channel = int(analog_channel)
    adc = ADC(channel)
    value = adc.read()
    msg = "[PiSmart] Read analog channel %s: %d"%(channel,value)
    print(msg)
    return value

def say(words):
    global pico
    pismart.speaker_switch(1)  # 1:on 0:off
    pico.say = words
    time.sleep(2)
    pismart.speaker_switch(0)  # 1:on 0:off

def set_dictionary(dic):
    global stt
    stt.end()
    cmds = []
    words = []
    dics = dic.split(',')
    for x in range(0,len(dics)):  # unicode 转换到 string
        dics[x] = dics[x].encode("utf-8")

    print("dics: %s" % dics)

    for dic in dics:
        cmds.append(dic.split(':')[0].encode("utf-8"))
        words.append(dic.split(':')[1].encode("utf-8"))
    #cmds[0].replace("['","").replace("']","")
    #words[0].replace("['","").replace("']","")
    print("commands: %s" % cmds)
    print("words: %s" % words)

    try:
        sps_file = open(sps_file_path, 'w')
        '''
        [ words ];
        @results
            0 {'result'}
        @
        '''
        for i in range(0,len(cmds)):
            sps_file.write("\n")
            sps_file.write("[ %s ];\n"%words[i])
            sps_file.write("@results\n")
            sps_file.write("    0 {\'%s\'}\n"%cmds[i])
            sps_file.write("@")
    finally:
        sps_file.close()
        os.system("cp %s ./"%sps_file_path)
        stt.update_dictionary()

def stt_heard():
    return stt.heard

def stt_result():
    return stt.result

def device_status():
    if err_msg == '':
        return 'Device is ok'
    else:
        return err_msg

def run_request(request):
    debug = ''
    action = None
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

    # ============== Led =============
    if action == 'set_led_brightness':
        brightness = int(value0)
        set_led_brightness(brightness)

    elif action == 'led_off':
        led_off()

    # ============== Motor =============
    elif action == 'motor_run':
        motor_chn = value0
        speed     = int(value1)
        motor_run(motor_chn, speed)

    # ================ Servo =================
    elif action == "servo_turn":
        servo_channel = int(value0)
        angle         = int(value1)
        servo_turn(servo_channel, angle)

    # ================ PWM =================
    elif action == "pwm_output":
        pwm_channel  = int(value0)
        value        = int(value1)
        pwm_output(pwm_channel, value)

    # ================ get analog =================
    elif action == "get_analog":
        analog_channel = int(value0)
        result = get_analog(analog_channel)

    # ================ digital =================
    elif action == "set_digital":
        digital_channel = value0
        digital_state   = value1
        result = set_digital(digital_channel, digital_state)

    elif action == "get_digital":
        digital_channel = value0
        result = get_digital(digital_channel)

    # ================ Say =================
    elif action == "say":
        print("[PiSmart] Say")
        words = value0
        say(words)

    # ================ Heard =================
    elif action == "set_dictionary":
        dic = value0
        set_dictionary(dic)

    elif action == "heard":
        msg = stt_heard()
        print("Heard: %s"%msg)
        result = msg

    elif action == "result":
        msg = stt_result()
        print("Result: %s"%msg)
        result = msg

    elif action == "device_status":
        result = device_status()

    else:
        result = 'action error: %s' % action
    return result

def run(request):
    try:
        result = run_request(request)
    except Exception, e:
        result = '\n%s\n%s'%(err_msg, e)
    finally:
        print("result:%s"%result)
        return HttpResponse(result)

def run_test(request):
    return HttpResponse(run_request(request))
