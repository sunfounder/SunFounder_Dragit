
from django.shortcuts import render_to_response
from django.http import HttpResponse

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
import ball_tracker
import sys

Motor_A = 17
Motor_B = 27

blob_x = 0
blob_y = 0
blob_r = 0

adc  = ADC(0x48)
fw   = front_wheels.Front_Wheels(debug=True, db='config')
bw   = back_wheels.Back_Wheels(db='config')
pan  = Servo(1)
tilt = Servo(2)
left_wheel  = Motor(Motor_A)
right_wheel = Motor(Motor_B)

db   = filedb.fileDB(db='config')
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
        msg = "[PiCar-V] Set Rear wheels %s at speed %d"%(direction, speed)
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

    print("[PiCar-V] Set Motor %s %s at %d speed"%(motor_channel, direction, speed))

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
    msg = "[PiCar-V] Front wheels turn %s "%(angle)
    print(msg)

def pan_turn(angle):
    angle = int(angle)+90
    if angle < -90:
        angle = -90
    elif angle > 180:
        angle = 180
    pan.write(angle)
    msg = "[PiCar-V] Pan servo turn %s "%(angle)
    print(msg)

def tilt_turn(angle):
    angle = int(angle)+90
    if angle < -30:
        angle = -30
    elif angle > 180:
        angle = 180
    tilt.write(angle)
    msg = "[PiCar-V] Tilt servo turn %s "%(angle)
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
    msg = "[PiCar-V] PWM chn: %s value: %s "%(channel, value)
    print(msg)

def servo_turn(servo_channel, angle):
    angle = int(angle)
    if angle < 0:
        angle = 0
    elif angle > 180:
        angle = 180
    servo = Servo(int(servo_channel))
    servo.write(angle)
    print("[PiCar-V] Set Servo %s to %d degree"%(servo_channel, angle))

def get_analog(analog_channel):
    if analog_channel == "A0":
        value = adc.A0
    elif analog_channel == "A1":
        value = adc.A1
    elif analog_channel == "A2":
        value = adc.A2
    elif analog_channel == "A3":
        value = adc.A3
    elif analog_channel == "A4":
        value = adc.A4
    print("[PiCar-V] Get Analog channel %s: %d"%(analog_channel,value))
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
    print("[PiCar-V] Calibrate Front wheels %s"%(value))

def cali_left_wheel(offset):
    if int(offset) < 0:
        value = 1
    else:
        value = 0
    db.set('forward_A', value)
    bw.left_wheel.offset = value
    print("[PiCar-V] Calibrate left wheel %s"%(value))
    time.sleep(0.1)

def cali_right_wheel(offset):
    if int(offset) < 0:
        value = 1
    else:
        value = 0
    db.set('forward_A', value)
    bw.left_wheel.offset = value
    print("[PiCar-V] Calibrate right wheel %s"%(value))
    time.sleep(0.1)

def cali_pan_servo(offset):
    value = int(offset)
    if value < -1024:
        value = -1024
    elif value > 1024:
        value = 1024

    pan.offset = value
    pan.write(90)

    db.set('pan_offset', value)
    print("[PiCar-V] Calibrate Pan %s"%(value))

def cali_tilt_servo(offset):
    value = int(offset)
    if value < -1024:
        value = -1024
    elif value > 1024:
        value = 1024

    tilt.offset = value
    tilt.write(90)

    db.set('tilt_offset', value)
    print("[PiCar-V] Calibrate Tilt %s"%(value))

def find_blob():
    print("Find red blob begin")
    (blob_x, blob_y), blob_r = ball_tracker.find_blob()
    if  blob_r == -1:
        blob_x = (ball_tracker.SCREEN_WIDTH/2)
        blob_y = (ball_tracker.SCREEN_HIGHT/2)
    blob_x = -((ball_tracker.SCREEN_WIDTH/2) - blob_x)
    blob_y = (ball_tracker.SCREEN_HIGHT/2) - blob_y
    print("x: %s, y: %s, r: %s"%(blob_x, blob_y, blob_r))
    print("[PiCar-V] Find red blob")

def get_blob(state):
    if state == "x":
        value = blob_x
    elif state == "y":
        value = blob_y
    elif state == "r":
        value = blob_r
    print("[PiCar-V] Blob %s: %d"%(state, value))
    return value

# Stop
def rw_stop():
    bw.stop()
    msg = "[PiCar-V] Stop"
    print(msg)

def run(request):
    debug = ''
    action = None
    value = None
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

    # ================ Pan & Tilt=================
    elif action == "pan_turn":
        value = value0
        pan_turn(value)

    elif action == "tilt_turn":
        value = value0
        tilt_turn(value)

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

        elif member == "pan servo":
            cali_pan_servo(offset)

        elif member == "tilt servo":
            cali_tilt_servo(offset)

    elif action == "get_offset_fw":
        result = turning_offset

    # ================ Ball track =================
    elif action == "find_blob":
        find_blob()

    elif action == "get_blob":
        state = value0
        get_blob(state)



    return HttpResponse(result)
