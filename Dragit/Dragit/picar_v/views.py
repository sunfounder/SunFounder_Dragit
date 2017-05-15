
from django.shortcuts import render_to_response
from django.http import HttpResponse

from Dragit.picar.SunFounder_PCA9685.Servo import Servo
from Dragit.picar.SunFounder_PCA9685.PCA9685 import PWM
from Dragit.picar import front_wheels
from Dragit.picar import back_wheels
from Dragit.picar import ADC
import Dragit.picar
import time
import RPi.GPIO as GPIO
import sys, os

blob_x = 0
blob_y = 0
blob_r = 0

config_dir = '/opt/SunFounder_Dragit/Dragit/config'
os.system('touch %s'%config_dir)

try:
    import image_process
    adc  = ADC(0x48)
    fw   = front_wheels.Front_Wheels(db=config_dir)
    bw   = back_wheels.Back_Wheels(db=config_dir)
    pan  = Servo(1)
    tilt = Servo(2)
    left_wheel  = bw.left_wheel
    right_wheel = bw.right_wheel

    fw.turning_max = 45
    Dragit.picar.setup()
    GPIO.setmode(GPIO.BCM)

    blob_x = 0
    blob_y = 0
    blob_r = 0
    err_msg = ''
except Exception,e:
    err_msg = "PiCar-V is not avalible"

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

def cam_turn(angle):
    fix_angle = 30
    pan_angle = 0
    tilt_angle = 0
    if angle == 'up':
        tilt_angle = fix_angle
    elif angle == 'down':
        tilt_angle = -fix_angle
    elif angle == 'left':
        pan_angle = fix_angle
    elif angle == 'right':
        pan_angle = -fix_angle
    elif angle == 'center':
        pass
    else:
        print("angle not define: %s" % angle)
    pan.write(pan_angle+90)
    tilt.write(tilt_angle+90)

def pan_turn(angle):
    angle = int(angle)+90
    if angle < -90:
        angle = -90
    elif angle > 180:
        angle = 180
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

def servo_turn(channel, angle):
    channel = int(channel)
    angle = int(angle)
    if angle < 0:
        angle = 0
    elif angle > 180:
        angle = 180
    servo = Servo(channel)
    servo.write(angle)
    print("[PiCar-V] Set Servo %s to %d degree"%(channel, angle))

def get_analog(channel):
    channel = int(channel)
    value = adc.read(channel)
    print("[PiCar-V] Get Analog channel %s: %d"%(channel,value))
    return value

def cali_front_wheels(offset):
    value = int(offset)
    if value < -1024:
        value = -1024
    elif value > 1024:
        value = 1024
    fw.turning_offset = value
    print("[PiCar-V] Calibrate Front wheels %s"%(value))

def cali_left_wheel(offset):
    value = int(offset)
    bw.left_wheel.offset = value
    bw.cali_forward_A = value
    bw.cali_ok_A()
    print("[PiCar-V] Calibrate left wheel %d"%(value))
    bw.left_wheel.forward()
    bw.left_wheel.speed = 40
    time.sleep(1)
    bw.left_wheel.speed = 0

def cali_right_wheel(offset):
    value = int(offset)
    bw.right_wheel.offset = value
    bw.cali_forward_B = value
    bw.cali_ok_B()
    print("[PiCar-V] Calibrate right wheel %d"%(value))
    bw.right_wheel.forward()
    bw.right_wheel.speed = 40
    time.sleep(1)
    bw.right_wheel.speed = 0

def cali_pan_servo(offset):
    value = int(offset)
    if value < -1024:
        value = -1024
    elif value > 1024:
        value = 1024

    pan.offset = value
    pan.write(90)

    print("[PiCar-V] Calibrate Pan %s"%(value))

def cali_tilt_servo(offset):
    value = int(offset)
    if value < -1024:
        value = -1024
    elif value > 1024:
        value = 1024

    tilt.offset = value
    tilt.write(90)

    print("[PiCar-V] Calibrate Tilt %s"%(value))

def find_blob():
    print("Find red blob begin")
    (blob_x, blob_y), blob_r = image_process.find_blob()
    if  blob_r == -1:
        blob_x = (image_process.SCREEN_WIDTH/2)
        blob_y = (image_process.SCREEN_HIGHT/2)
    blob_x = -((image_process.SCREEN_WIDTH/2) - blob_x)
    blob_y = (image_process.SCREEN_HIGHT/2) - blob_y
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
    elif action == "cam_turn":
        value = value0
        cam_turn(value)

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
        print("[PiCar-V] Calibrate")
        member = value0
        offset = value1

        if member == "front_wheels":
            cali_front_wheels(offset)

        elif member == "left_wheel":
            cali_left_wheel(offset)

        elif member == "right_wheel":
            cali_right_wheel(offset)

        elif member == "pan_servo":
            cali_pan_servo(offset)

        elif member == "tilt_servo":
            cali_tilt_servo(offset)
        else:
            result = 'calibration member error: %s' % member

    # ================ Ball track =================
    elif action == "find_blob":
        find_blob()

    elif action == "get_blob":
        state = value0
        get_blob(state)

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