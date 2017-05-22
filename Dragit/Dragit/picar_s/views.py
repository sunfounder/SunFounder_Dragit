
from django.shortcuts import render_to_response
from django.http import HttpResponse

from Dragit.sensors.Ultrasonic_Avoidance import Ultrasonic_Avoidance
from Dragit.sensors.Light_Follower import Light_Follower
from Dragit.sensors.Line_Follower import Line_Follower

from Dragit.picar.SunFounder_PCA9685.Servo import Servo
from Dragit.picar.SunFounder_PCA9685.PCA9685 import PWM
from Dragit.picar import front_wheels
from Dragit.picar import back_wheels
from Dragit.picar import ADC
import Dragit.picar
import time
import RPi.GPIO as GPIO
import sys, os

try:
    config_dir = '/opt/SunFounder_Dragit/Dragit/config'
    os.system('touch %s'%config_dir)

    adc  = ADC(0x48)

    lf = Line_Follower()
    lt = Light_Follower()
    fw = front_wheels.Front_Wheels(db=config_dir)
    bw = back_wheels.Back_Wheels(db=config_dir)
    left_wheel  = bw.left_wheel
    right_wheel = bw.right_wheel

    lt.analog_function = adc.read

    fw.turning_max = 45
    Dragit.picar.setup()
    GPIO.setmode(GPIO.BCM)
    err_msg = ''
except Exception,e:
    err_msg = "PiCar-S is not avalible"

def rw_run(motor_channel, direction, speed):
    if speed < 0:
        speed = 0
    elif speed > 100:
        speed = 100

    # both motor
    if motor_channel == "both":
        if direction == "forward":
            bw.forward()
        elif direction == "backward":
            bw.backward()
        bw.speed = speed
        msg = "[PiCar-S] Set Rear wheels %s at speed %d"%(direction, speed)
        print(msg)
    # left motor
    elif motor_channel == "left":
        if direction == "backward":
            bw.left_wheel.backward()
        elif direction == "forward":
            bw.left_wheel.forward()
        bw.left_wheel.speed = speed
    # right motor
    elif motor_channel == "right":
        if direction == "backward":
            bw.right_wheel.backward()
        elif direction == "forward":
            bw.right_wheel.forward()
        bw.right_wheel.speed = speed

    print("[PiCar-S] Set Motor %s %s at %d speed"%(motor_channel, direction, speed))

def fw_turn(angle):
    if angle == 'left':
        fw.turn_left()
    elif angle == 'straight':
        fw.turn_straight()
    elif angle == 'right':
        fw.turn_right()
    else:
        angle = int(angle)+90
        fw.turn(angle)
    msg = "[PiCar-S] Front wheels turn %s "%(angle)
    print(msg)

def pwm_output(channel, value):
    channel = int(channel)
    value   = int(value)
    if value < 0:
        value = 0
    elif value > 4095:
        value = 4095
    pwm = PWM(channel)
    pwm.write(value)
    msg = "[PiCar-S] PWM chn: %s value: %s "%(channel, value)
    print(msg)

def servo_turn(channel, angle):
    channel = int(channel)
    angle = int(angle)
    if angle < 0:
        angle = 0
    elif angle > 180:
        angle = 180
    servo = Servo(channel)
    servo.write(angle)
    print("[PiCar-S] Set Servo %s to %d degree"%(channel, angle))

def get_analog(channel):
    channel = int(channel)
    value = adc.read(channel)
    print("[PiCar-S] Get Analog channel %s: %d"%(channel,value))
    return value

def cali_front_wheels(offset):
    value = int(offset)
    if value < -1024:
        value = -1024
    elif value > 1024:
        value = 1024
    fw.turning_offset = value
    print("[PiCar-S] Calibrate Front wheels %s"%(value))

def cali_left_wheel(offset):
    value = int(offset)
    bw.left_wheel.offset = value
    bw.cali_forward_A = value
    bw.cali_ok_A()
    print("[PiCar-S] Calibrate left wheel %s"%(value))
    bw.left_wheel.forward()
    bw.left_wheel.speed = 40
    time.sleep(1)
    bw.left_wheel.speed = 0

def cali_right_wheel(offset):
    value = int(offset)
    bw.right_wheel.offset = value
    bw.cali_forward_B = value
    bw.cali_ok_B()
    print("[PiCar-S] Calibrate right wheel %s"%(value))
    bw.right_wheel.forward()
    bw.right_wheel.speed = 40
    time.sleep(1)
    bw.right_wheel.speed = 0

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
    print("[PiCar-S] Get Ultrasonic sensor channel: %s, distance: %s"%(channel, result))
    return result

def light_analog_index(channel):
    result = lt.read_analogs()
    if channel != None:
        value = result[int(channel)]
        print("[PiCar-S] Light_Follower channel:%s, value:%s"%(channel, value))
    else:
        value = str(result).replace("'", '').strip('[]').replace(' ','')
        print("[PiCar-S] Light_Follower value:%s"%(value))
    return value

def line_analog_index(channel):
    result = lf.read_analogs()
    if channel != None:
        value = result[int(channel)-1]
        print("[PiCar-S] Light_Follower channel:%s, value:%s"%(channel, value))
    else:
        value = str(result).replace("'", '').strip('[]').replace(' ','')
        print("[PiCar-S] Light_Follower value:%s"%(value))
    return value

# Stop
def rw_stop():
    bw.stop()
    msg = "[PiCar-S] Stop"
    print(msg)

def device_status():
    if err_msg == '':
        return 'Device is ok'
    else:
        return err_msg

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

        # ============== Back wheels =============
        if action == 'rw_run':
            motor_channel = value0
            direction = value1
            speed = int(value2)
            rw_run(motor_channel, direction, speed)
            debug = "motor_channel = ", motor_channel
            debug = "direction =", direction
            debug = "speed =", speed

        elif action == 'rw_stop':
            rw_stop()

        # ============== Front wheels =============
        elif action == 'fw_turn':
            value = value0
            fw_turn(value)

        # ================ Servo & Motor =================
        elif action == "servo_turn":
            servo_channel = int(value0)
            angle         = int(value1)
            servo_turn(servo_channel, angle)

        elif action == "motor_run":
            motor_channel = value0
            direction     = value1
            speed         = int(value2)
            motor_run(motor_channel, direction, speed)

        # ================ PWM =================
        elif action == "pwm_output":
            pwm_channel = value0
            value = value1
            pwm_output(pwm_channel, value)

        # ================ get analog =================
        elif action == "get_analog":
            analog_channel = value0
            result = get_analog(analog_channel)

        # ================ Calibrate =================
        elif action == "calibrate":
            member = value0
            offset = value1

            if member == "front_wheels":
                cali_front_wheels(offset)

            elif member == "left_wheel":
                cali_left_wheel(offset)

            elif member == "right_wheel":
                cali_right_wheel(offset)

        elif action == "get_offset_fw":
            result = turning_offset

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
