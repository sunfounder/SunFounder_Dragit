from pismart.amateur import PiSmart
import time

pismart = PiSmart('manual')
menu_list = ['0','1','2','3','4','5','6','7']
def menu():
    print ''
    print '|==================================================|'
    print '|             Test menu  for PiSmart               |'
    print '|--------------------------------------------------|'
    print '|  Input which one to test:                        |'
    print '|      1.  ADC read test                           |'
    print '|      2.  Servo ports test                        |'
    print '|      3.  Led test                                |'
    print '|      4.  Motor ports test                        |'
    print '|      5.  TTS test                                |'
    print '|      6.  Mic test                                |'
    print '|                                                  |'
    print '|                                        SunFounder|'
    print '|==================================================|'
    return raw_input("Test: ")

def main():
    while True:
        case = menu()
        if case not in menu_list:
            print "Input out of menu list"
            menu()
        elif case == menu_list[1]:
            adc()
        elif case == menu_list[2]:
            servo()
        elif case == menu_list[3]:
            led()
        elif case == menu_list[4]:
            motor()
        elif case == menu_list[5]:
            tts()
        elif case == menu_list[6]:
            mic()
        elif case == menu_list[0]:
            menu()

def adc():
    pismart.ADC_init()
    delay = 0.5
    try:
        while True:
            print ("A0 = {0}      A1 = {1}     A2 = {2}     A3 = {3}     A4 = {4}".format(
                pismart.A0, pismart.A1, pismart.A2, pismart.A3, pismart.A4 ))
            time.sleep(delay)
    except KeyboardInterrupt:
        pismart.ADC_end()

def servo():
    pismart.Servo_init()
    delay = 0.01
    try:
        while True:
            for i in range(0, 181, 1):
                pismart.Servo0 = i
                pismart.Servo1 = i
                pismart.Servo2 = i
                pismart.Servo3 = i
                pismart.Servo4 = i
                pismart.Servo5 = i
                pismart.Servo6 = i
                pismart.Servo7 = i
                time.sleep(delay)
                print i
            time.sleep(2)
            for i in range(180, -1, -1):
                pismart.Servo0 = i
                pismart.Servo1 = i
                pismart.Servo2 = i
                pismart.Servo3 = i
                pismart.Servo4 = i
                pismart.Servo5 = i
                pismart.Servo6 = i
                pismart.Servo7 = i
                time.sleep(delay)
                print i
            time.sleep(2)
    except KeyboardInterrupt:
        pismart.Servo_end() 
    
def led():
    pismart.LED_init()
    delay = 0.01
    try:
        while True:
            print "Brightness: 0~100, delay=%s"%delay
            for i in range(0, 101, 1):
                pismart.LED = i
                time.sleep(delay)
            #time.sleep(1)
            print "Brightness: 100~0, delay=%s"%delay
            for i in range(100, -1, -1):
                pismart.LED = i
                time.sleep(delay)
            #time.sleep(1)
    except KeyboardInterrupt:
        pismart.LED_end() 
    
def motor():
    pismart.Motor_init()
    try:
        while True:
            pismart.MotorA_reversed = True
            pismart.MotorA = 100
            pismart.MotorB = 100
            print "speed: 100"
            time.sleep(1)
            pismart.MotorA = 50
            pismart.MotorB = 50
            print "speed: 50"
            time.sleep(1)
            pismart.MotorA = 0
            pismart.MotorB = 0
            print "speed: 0"
            time.sleep(1)
            pismart.MotorA = -50
            pismart.MotorB = -50
            print "speed: -50"
            time.sleep(1)
            pismart.MotorA = -100
            pismart.MotorB = -100
            print "speed: -100"
            time.sleep(1)
            pismart.MotorA = 0
            pismart.MotorB = 0
            print "speed: 0"
    except KeyboardInterrupt:
        pismart.Motor_end()    

def switchs():
    print 'Set speaker volume to 100...',
    pismart.speaker_volume = 100
    print 'done'
    print 'Speaker volume now is', pismart.speaker_volume
    print 'Set capture volume to 100...',
    pismart.capture_volume = 100
    print 'done'
    print 'Capture volume now is', pismart.capture_volume
    print 'Set power type to DC...',
    pismart.power_type = 'DC'
    print 'done'
    print 'Power type now is', pismart.power_type
    print ''
    print 'Power voltage now is', pismart.power_voltage
    print 'Switch the servo on...',
    pismart.servo_switch(pismart.ON)
    print 'done'
    print 'Switch the PWM on...',
    pismart.pwm_switch(pismart.ON)
    print 'done'
    print 'Switch the motor on...',
    pismart.motor_switch(pismart.ON)
    print 'done'
    print 'Switch the speaker on...',
    pismart.speaker_switch(pismart.ON)
    print 'done'

    print 'Switch the servo off...',
    pismart.servo_switch(pismart.OFF)
    print 'done'
    print 'Switch the PWM off...',
    pismart.pwm_switch(pismart.OFF)
    print 'done'
    print 'Switch the motor off...',
    pismart.motor_switch(pismart.OFF)
    print 'done'
    print 'Switch the speaker off...',
    pismart.speaker_switch(pismart.OFF)
    print 'done'

def tts():
    pismart.TTS_init()
    print pismart.Say
    pismart.Say = "Yes, i am"

def stt():
    pismart.STT_init()
    try:
        while True:
            pismart.listen
            if pismart.heard:
                print "I heard that: %s" % pismart.result
    except KeyboardInterrupt:
       pismart.STT_end()

def mic():
    import os
    pismart.speaker_switch(pismart.ON)
    print "Record 5 seconds, and then play the voice"
    os.system('arecord -D "plughw:1,0" -d 5 > /tmp/test.wav && omxplayer /tmp/test.wav')

def volume_test():
    for i in range(100, -1, -10):
        print 'Set speaker volume to %s...' % i
        pismart.speaker_volume = i
        pismart.Say = 'This is %s percent volume' % i

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pismart.end()
