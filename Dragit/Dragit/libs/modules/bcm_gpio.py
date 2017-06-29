#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import threading
import time

class BCM_GPIO(object):
    """docstring for rpi_pin"""
    INPUT  = 0
    OUTPUT = 1
    PWM    = 2
    _mode_=["input", "output", "pwm_output"]
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    def __init__(self, chn):
        self.chn = chn
        self.freq = 100
        self.mode = self._mode_[self.INPUT]
        self.dc  = 50
        self.pwm = -1        # an pwm object
        GPIO.setup(self.chn, GPIO.IN)
        print("Init GPIO%s success"%self.chn)

    def input(self):
        self.try_stop_pwm()
        GPIO.cleanup(self.chn)
        GPIO.setup(self.chn, GPIO.IN)
        self.mode  = self._mode_[self.INPUT]
        value = GPIO.input(self.chn)
        print ("GPIO%s input value:%s"%(self.chn, value))
        return value

    def output(self, value):
        self.try_stop_pwm()
        GPIO.cleanup(self.chn)
        GPIO.setup(self.chn, GPIO.OUT)
        self.mode = self._mode_[self.OUTPUT]
        if value == 'HIGH':
            GPIO.output(self.chn, GPIO.HIGH)
        elif value == 'LOW':
            GPIO.output(self.chn, GPIO.LOW)
        else:
            print("Output value: ('HIGH') or ('LOW')")

    def pwm_init(self):
        self.pwm = self.Soft_PWM(self.chn)
        self.pwm.set_frequency(self.freq)
        self.pwm.set_dutycycle(self.dc)
        self.pwm.start()
        self.mode  = self._mode_[self.PWM]

    def pwm_output(self, dc=None, freq=None):
        if self.pwm == -1:     # pwm object not creat
            self.pwm_init()

        if dc != None:          # pwm_output(dc=xx)
            self.dc = dc
            self.pwm.set_dutycycle(self.dc)
        if freq != None:        # pwm_output(freq=xx)
            self.freq = freq
            self.pwm.set_frequency(self.freq)
        print ("DC = %s, freq = %s"%(self.dc, self.freq))

    def try_stop_pwm(self):
        try:
            self.pwm.stop()
            self.pwm  = -1   # remove pwm object
            self.mode = self._mode_[0]
            GPIO.cleanup(self.chn)
        except Exception, e:
            #print Exception,":",e
            pass

    def get_status(self):
        print ("chn: %s, \n ├─mode: %s, \n ├─freq: %s, \n └─dc: %s"\
            %(self.chn, self.mode, self.freq, self.dc))
        return (self.chn, self.mode, self.freq, self.dc)

    def end(self):
        self.try_stop_pwm()

    class Soft_PWM(object):
        """docstring for Soft_PWM"""

        def __init__(self, chn):
            self.chn  = chn
            self.dc   = 30
            self.freq = 60
            self.pwm_status = 0

            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(self.chn, GPIO.OUT)
            self.t = threading.Thread(target=self.pwm_thread)

        def pwm_thread(self):
            self.pwm_status = 1
            try:
                while self.pwm_status:
                    #time.sleep(0.00000000000001)
                    #print("pwm thread running")
                    GPIO.output(self.chn, 1)
                    time.sleep(self.on_time)
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


def test_input(chn):
    print("[Class Test] Test BCM_GPIO input")
    pin17 = BCM_GPIO(chn)
    a = pin17.input()
    print "input value", a
    pin17.get_status()

def test_output(chn, value):
    print("[Class Test] Test BCM_GPIO output")
    pin17 = BCM_GPIO(chn)
    pin17.output(value)
    print "output value:", value
    pin17.get_status()

def test_pwm_freq(chn):
    print("[Class Test] Test BCM_GPIO pwm freq")
    pin17 = BCM_GPIO(chn)
    CM = [1, 262, 294, 330, 350, 393, 441, 495, 525]
    for x in range(1,9):
        pin17.pwm_output(freq=CM[x])
        time.sleep(0.25)
    pin17.pwm_output(freq=CM[0])
    time.sleep(0.5)
    for x in range(8,0,-1):
        pin17.pwm_output(freq=CM[x])
        time.sleep(0.25)
    pin17.get_status()
    pin17.end()

def test_pwm_dc(chn):
    print("[Class Test] Test BCM_GPIO pwm dc")
    pin17 = BCM_GPIO(chn)
    for x in range(0, 101):
        pin17.pwm_output(dc=x)
        time.sleep(0.01)
    for x in range(100, 0, -1):
        pin17.pwm_output(dc=x)
        time.sleep(0.02)
    pin17.get_status()
    pin17.end()

if __name__ == '__main__':
    #try:
    #    test_input(17)
    #for x in xrange(1,5):
    #    test_output(17, 'HIGH')
    #    time.sleep(1)
    #    test_output(17, 'LOW')
    #    time.sleep(1)
    test_pwm_freq(17)
    #test_pwm_dc(20)
    #test_input(17)
    #except KeyboardInterrupt: