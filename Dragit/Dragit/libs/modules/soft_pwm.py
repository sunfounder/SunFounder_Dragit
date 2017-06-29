from __future__ import print_function
import RPi.GPIO as GPIO
import threading
import time

class Soft_PWM(object):
    """docstring for Soft_PWM"""

    def __init__(self, chn):
        self.chn  = chn
        self.dc   = 50
        self.freq = 100
        self.pwm_status = 0

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.chn, GPIO.OUT)
        self.t = threading.Thread(target=self.pwm_thread)

    def pwm_thread(self):
        self.pwm_status = 1
        try:
            while self.pwm_status:
                #print("-"*(self.dc/10),end="")
                GPIO.output(self.chn, 1)
                time.sleep(self.on_time)
                #print("_"*(10-self.dc/10),end="")
                GPIO.output(self.chn, 0)
                time.sleep(self.off_time)
        except:
            pass

    def start(self):
        self.t.start()

    def stop(self):
        self.pwm_status = 0
        GPIO.cleanup(self.chn)
        GPIO.setmode(GPIO.BCM)

    def set_frequency(self, freq):
        self.freq = freq
        self.on_time  = 1.0/self.freq * self.dc /100
        self.off_time = 1.0/self.freq * (100 - self.dc) /100

    def set_dutycycle(self, dc):
        self.dc = dc
        self.on_time  = 1.0/self.freq * self.dc /100
        self.off_time = 1.0/self.freq * (100 - self.dc) /100

    def get_status(self):
        return self.pwm_status

def test_dc():
    print ("Test DC, pin 17")
    led = Soft_PWM(17)
    led.set_frequency(100)
    led.start()
    for x in range(0,100):
        led.set_dutycycle(x)
        time.sleep(0.05)
    led.stop()

def test_freq():
    '''
    CL = [0, 131, 147, 165, 175, 196, 211, 248]     # Frequency of Low C notes

    CM = [0, 262, 294, 330, 350, 393, 441, 495]     # Frequency of Middle C notes

    CH = [0, 525, 589, 661, 700, 786, 882, 990]     # Frequency of High C notes
    '''
    print("Test freq")
    CM = [0, 262, 294, 330, 350, 393, 441, 495, 525]
    led = Soft_PWM(17)
    led.set_dutycycle(50)
    led.start()
    for x in range(1,9):
        led.set_frequency(CM[x])
        time.sleep(0.25)
    for x in range(8,0,-1):
        led.set_frequency(CM[x])
        time.sleep(0.25)
    led.stop()

def test_rpigpio_pwm():
    print("Test RPi.GPIO pwm")
    GPIO.setup(17,GPIO.OUT)
    led2 = GPIO.PWM(17, 100)
    led2.start(0)
    for x in range(0,100):
        led2.ChangeDutyCycle(x)
        time.sleep(0.05)
    led2.stop()

if __name__ == '__main__':
    for x in xrange(1,6):
        test_dc()
        time.sleep(0.5)
        test_rpigpio_pwm()
        time.sleep(0.5)

    #test_freq()