
from django.shortcuts import render_to_response
from django.http import HttpResponse

from sensor_modules.SunFounder_Ultrasonic_Avoidance.Ultrasonic_Avoidance import Ultrasonic_Avoidance
from sensor_modules.SunFounder_Light_Follower.Light_Follower import Light_Follower
from sensor_modules.SunFounder_Line_Follower.Line_Follower import Line_Follower

from picar.SunFounder_PCA9685.Servo import Servo
from picar.SunFounder_PCA9685.PCA9685 import PWM
from picar.SunFounder_TB6612.TB6612 import Motor
from picar import front_wheels
from picar import back_wheels
from picar import filedb
from picar import ADC
import picar
import time
import RPi.GPIO as GPIO
import sys

Motor_A = 17
Motor_B = 27

adc  = ADC(0x48)
pan  = Servo(1)
tilt = Servo(2)
left_wheel  = Motor(Motor_A)
right_wheel = Motor(Motor_B)

lf = Line_Follower()
lt = Light_Follower()
lt.analog_function = adc.read
fw = front_wheels.Front_Wheels(debug=True, db='config')
bw = back_wheels.Back_Wheels(db='config')

db = filedb.fileDB(db='config')
turning_offset = int(fw.db.get('turning_offset', default_value=0))
pan_offset     = int(fw.db.get('pan_offset',     default_value=0))
tilt_offset    = int(fw.db.get('tilt_offset',    default_value=0))

fw.turning_max = 45
picar.setup()
GPIO.setmode(GPIO.BCM)

blob_x = 0
blob_y = 0
blob_r = 0

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

def servo_turn(servo_channel, angle):
    angle = int(angle)
    if angle < 0:
        angle = 0
    elif angle > 180:
        angle = 180
    servo = Servo(int(servo_channel))
    servo.write(angle)
    print("[PiCar-S] Set Servo %s to %d degree"%(servo_channel, angle))

def get_analog(analog_channel):
    if analog_channel == "0":
        value = adc.A0
    elif analog_channel == "1":
        value = adc.A1
    elif analog_channel == "2":
        value = adc.A2
    elif analog_channel == "3":
        value = adc.A3
    elif analog_channel == "4":
        value = adc.A4
    print("[PiCar-S] Get Analog channel %s: %d"%(analog_channel,value))
    return value

def get_digital(digital_channel):
    digital_channel = int(digital_channel)
    GPIO.setup(digital_channel, GPIO.IN)
    result = GPIO.input(digital_channel)
    print("Read GPIO %s, state: %s" )%(digital_channel, result)
    return result

def set_digital(digital_channel, IO_state):
    digital_channel = int(digital_channel)
    GPIO.setup(digital_channel, GPIO.OUT)
    if(IO_state == "HIGH"):
        GPIO.output(digital_channel, GPIO.HIGH)
    else:
        GPIO.output(digital_channel, GPIO.LOW)
    print ("Set GPIO %s state to %s")%(digital_channel, IO_state)

def cali_front_wheels(offset):
    value = int(offset)
    if value < -1024:
        value = -1024
    elif value > 1024:
        value = 1024
    fw.turning_offset = value
    print("[PiCar-S] Calibrate Front wheels %s"%(value))

def cali_left_wheel(offset):
    if int(offset) <= 0:
        value = 0
    else:
        value = 1
    db.set('forward_A', value)
    bw.left_wheel.offset = value
    print("[PiCar-S] Calibrate left wheel %s"%(value))
    bw.left_wheel.forward()
    bw.left_wheel.speed = 40
    time.sleep(1)
    bw.left_wheel.speed = 0

def cali_right_wheel(offset):
    if int(offset) <= 0:
        value = 0
    else:
        value = 1
    db.set('forward_B', value)
    bw.right_wheel.offset = value
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

def run(request):
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

        if member == "front wheel":
            cali_front_wheels(offset)

        elif member == "left wheel":
            cali_left_wheel(offset)

        elif member == "right wheel":
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


    return HttpResponse(result)
