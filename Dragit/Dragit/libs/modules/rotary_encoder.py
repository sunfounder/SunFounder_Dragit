#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import threading


class RotaryEncoder(object):
    """docstring for RotaryEncoder"""
    CW  = 1
    CCW = -1
    def __init__(self, SCL, DT, SW):
        self.RoAPin = SCL    # CLK Pin
        self.RoBPin = DT    # DT Pin
        self.BtnPin = SW    # Button Pin

        self.flag = 0
        self.Last_RoB_Status = 0
        self.Current_RoB_Status = 0

        GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
        GPIO.setup(self.RoAPin, GPIO.IN)    # input mode
        GPIO.setup(self.RoBPin, GPIO.IN)
        GPIO.setup(self.BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.t = threading.Thread(target=self.rotaryDeal_thread)
        self.alive_status = 0
        self.rotation = 0
        self.button = 0

    def rotaryDeal_thread(self):
        #print("Thread run...")
        try:
            while self.alive_status:
                self.Last_RoB_Status = GPIO.input(self.RoBPin)
                #print ('self.Last_RoB_Status ', self.Last_RoB_Status)
                while(not GPIO.input(self.RoAPin)):
                    #print ("A input: %s "%(GPIO.input(self.RoAPin)))
                    self.Current_RoB_Status = GPIO.input(self.RoBPin)
                    self.flag = 1
                    time.sleep(0.0001)
                #print ("B status: %s -> %s"%(self.Last_RoB_Status, self.Current_RoB_Status))
                if self.flag == 1:
                    self.flag = 0
                    if (self.Last_RoB_Status == 0) and (self.Current_RoB_Status == 1):
                        self.rotation = self.CW
                    elif (self.Last_RoB_Status == 1) and (self.Current_RoB_Status == 0):
                        self.rotation = self.CCW
                    else:
                        self.rotation = 0
                #print ("self.globalCounter ", self.globalCounter)
                time.sleep(0.0001)
        except:
            pass

    def get_button(self):
        return GPIO.input(self.BtnPin)

    def get_rotation(self):
        result = self.rotation
        #print ("get rotation: %s"%result)
        self.rotation = 0
        return result

    def start(self):
        self.alive_status = 1
        self.t.start()

    def end(self):
        self.alive_status = 0
        GPIO.cleanup(self.RoAPin)
        GPIO.cleanup(self.RoBPin)
        GPIO.cleanup(self.BtnPin)

    def get_status(self):
        return self.alive_status


def test():
    try:
        encoder = RotaryEncoder(17,18,27)
        encoder.start()
        count = 0
        tmp = 0
        while True:
            count = count + encoder.get_rotation()
            if (not encoder.get_button()):
                count = 0
            #if tmp != count:
            print ("%s count = %s"%(time.time(), count))
            #    tmp = count
            time.sleep(1)
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        encoder.end()


if __name__ == '__main__':     # Program start from here
    test()


