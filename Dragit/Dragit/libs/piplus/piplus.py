#=============== SunFounder_PiPlus =================
#
#	SunFounder PiPlus is a kit from SunFounder,
#	designed for Raspbery Pi model B+ and Raspbery Pi 2 model B.
#
#	It is a kit with no wires -- just plug & play.
#
#	This program is under the GNU license.
#


#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import math
import random
import smbus
import time
import os
import commands
import threading

'''
Convert the GPIOs from BOARD to PIPLUS
'''
D0		=	7

DA1		=	17
DA2		=	18
DA3		=	27
DA4		=	22
DA5		=	23
DA6		=	24
DA7		=	25
DA8		=	5

DB1		=	6
DB2 	=	13
DB3 	=	19
DB4 	=	26
DB5 	=	12
DB6 	=	16
DB7 	=	20
DB8		=	21

CE0		=	8
CE1		=	7

SDA		=	2
SCL		=	3
TXD		=	14
RXD		=	15
MOSI	=	10
MISO	=	9
SCLK	=	11

AIN0	=	0
AIN1	=	1
AIN2	=	2
AIN3	=	3

GPIO.setmode(GPIO.BCM)

'''
Define the Joystick status
'''
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
HOME = 5
PRESSED = 6

RUNTIME = 1000

HOUR12 = 0		#12 hour clock defined
HOUR24 = 1		#24 hour clock defined

SLOW = 0
FAST = 1

MORSECODE = {
	'A':'01', 'B':'1000', 'C':'1010', 'D':'100', 'E':'0', 'F':'0010', 'G':'110',
	'H':'0000', 'I':'00', 'J':'0111', 'K':'101', 'L':'0100', 'M':'11', 'N':'10',
	'O':'111', 'P':'0110', 'Q':'1101', 'R':'010', 'S':'000', 'T':'1',
	'U':'001', 'V':'0001', 'W':'011', 'X':'1001', 'Y':'1011', 'Z':'1100',
	'1':'01111', '2':'00111', '3':'00011', '4':'00001', '5':'00000',
	'6':'10000', '7':'11000', '8':'11100', '9':'11110', '0':'11111',
	'?':'001100', '/':'10010', ',':'110011', '.':'010101', ';':'101010',
	'!':'101011', '@':'011010', ':':'111000',
	}

'''
Define a Map function to map different ranges
'''
def Map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

'''
A function for Normal Distribution use
'''
def NormalDistribution(x, u=0, d=1):
	PI = 3.1415926
	E = 2.718281828
	result = (E ** (-((x-u)**2) / (2*d*d))) / (math.sqrt(2 * PI) * d)
	return result

'''
A function for Low-pass Filter
'''
def LowpassFilter(_value, _new_value):
	_a = 50
	_base = 100
	return ((_base-_a)*_value)/100.0+(_a*_new_value)/100.0

'''
A function to get a Threshold
'''
def Threshold(_value, threshold=200):
	if _value > threshold:
		return 1
	elif _value < threshold:
		return 0

'''
classes for each module
'''
class DS1307(object):
	# DS1307 on Plus Shield
	def __init__(self, _clock = HOUR24):
		os.system('echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-1/new_device')
		self._clockset = _clock

	def get_datetime(self):
		status, _datetime=commands.getstatusoutput('hwclock -r')
		return _datetime

	def get_date(self):
		_datetime = self.get_datetime()
		split_datetime = _datetime.split(' ')
		_date = [split_datetime[0], split_datetime[1], split_datetime[2], split_datetime[3]]
		_blank = ' '
		_date = _blank.join(_date)
		return _date

	def get_time(self):
		_time = self.get_datetime().split(' ')[4]
		if self._clockset == HOUR12 :
			_hour = int(_time.split(':')[0])
			if _hour > 11 :
				apm = 'PM'
			else:
				apm = 'AM'
			if _hour > 12 :
				_hour = _hour - 12
			if _hour == 0:
				_hour = 12
			if _hour < 10:
				_hour = '0%d' % _hour
			_time = '%s:%s:%s %s' % (_hour, _time.split(':')[1], _time.split(':')[2], apm)
		return _time

	def get_split_datetime(self):
		_datetime = self.get_datetime()
		split_datetime = _datetime.split(' ')
		_date = [split_datetime[0], split_datetime[1], split_datetime[2], split_datetime[3]]
		_time = split_datetime[4]
		if self._clockset == HOUR12 :
			_hour = int(_time.split(':')[0])
			if _hour > 11 :
				apm = 'PM'
			else:
				apm = 'AM'
			if _hour > 12 :
				_hour = _hour - 12
			if _hour == 0:
				_hour = 12
			if _hour < 10:
				_hour = '0%d' % _hour
			_time = '%s:%s:%s %s' % (_hour, _time.split(':')[1], _time.split(':')[2], apm)
		_blank = ' '
		_date = _blank.join(_date)
		return _date, _time

	def destroy(self):
		pass

class PCF8591(object):
	# PCF8597 on Plus Shield
	_ADC_bus = smbus.SMBus(1) # or bus = smbus.SMBus(0) for Revision 1 boards
	def __init__(self, Address=0x48, _bus=_ADC_bus):
		super(PCF8591, self).__init__()
		self._address = Address
		self._bus = _bus

	def read(self, chn): #channel
		if chn == 0:
			self._bus.write_byte(self._address,0x40)
		if chn == 1:
			self._bus.write_byte(self._address,0x41)
		if chn == 2:
			self._bus.write_byte(self._address,0x42)
		if chn == 3:
			self._bus.write_byte(self._address,0x43)
		self._bus.read_byte(self._address) # dummy read to start conversion
		return self._bus.read_byte(self._address)

	def read_all(self):
		return self.read(0), self.read(1), self.read(2), self.read(3)

	def write(self, val):
		_temp = val # move string value to temp
		_temp = int(_temp) # change string to integer
		# print temp to see on terminal else comment out
		self._bus.write_byte_data(self._address, 0x40, _temp)

	def destroy(self):
		pass

class LED_Ring(object):
	# Plus LED Ring module of PiPlus from SunFounder
	def __init__(self, port='A'):
		if port not in ['A', 'a', 'B', 'b']:
			raise ValueError("Unexpected port value {0}, Set port to 'A' or 'B', like: '(port='A')'".format(port))

		if port in ['A', 'a']:
			LED = [DA1, DA2, DA3, DA4, DA5, DA6, DA7, DA8]
		elif port in ['B', 'b']:
			LED = [DB1, DB2, DB3, DB4, DB5, DB6, DB7, DB8]

		for x in LED:
			GPIO.setup(x, GPIO.OUT, initial=1)

		self._led1 = GPIO.PWM(LED[0], 100)
		self._led2 = GPIO.PWM(LED[1], 100)
		self._led3 = GPIO.PWM(LED[2], 100)
		self._led4 = GPIO.PWM(LED[3], 100)
		self._led5 = GPIO.PWM(LED[4], 100)
		self._led6 = GPIO.PWM(LED[5], 100)
		self._led7 = GPIO.PWM(LED[6], 100)
		self._led8 = GPIO.PWM(LED[7], 100)
		self._led1.start(100)
		self._led2.start(100)
		self._led3.start(100)
		self._led4.start(100)
		self._led5.start(100)
		self._led6.start(100)
		self._led7.start(100)
		self._led8.start(100)


	def SINGLE(self):
		return [100,   0,   0,   0,   0,   0,   0,   0]

	def ARC(self):
		return [100, 100, 100,   0,   0,   0,   0,   0]

	def STAR(self):
		return [  0,  60,   0,  60,   0,  60,   0,  60]

	def ALL_BRIGHT(self):
		return [100, 100, 100, 100, 100, 100, 100, 100]

	def ALL_DIM(self):
		return [ 60,  60,  60,  60,  60,  60,  60,  60]

	def ALL_OFF(self):
		return [  0,   0,   0,   0,   0,   0,   0,   0]


	def on(self, _ring):
		for i in range(8):
			if _ring[i] > 100:
				_ring[i] = 100
			if _ring[i] < 0:
				_ring[i] = 0
		self._led1.ChangeDutyCycle(100 - _ring[0])
		self._led2.ChangeDutyCycle(100 - _ring[1])
		self._led3.ChangeDutyCycle(100 - _ring[2])
		self._led4.ChangeDutyCycle(100 - _ring[3])
		self._led5.ChangeDutyCycle(100 - _ring[4])
		self._led6.ChangeDutyCycle(100 - _ring[5])
		self._led7.ChangeDutyCycle(100 - _ring[6])
		self._led8.ChangeDutyCycle(100 - _ring[7])

	def _spin(self, _w, _ring): # w=0: clockwise, w=1: anticlockwise
		if _w == 0:
			_tmp = _ring[0]
			_ring[0] = _ring[1]
			_ring[1] = _ring[2]
			_ring[2] = _ring[3]
			_ring[3] = _ring[4]
			_ring[4] = _ring[5]
			_ring[5] = _ring[6]
			_ring[6] = _ring[7]
			_ring[7] = _tmp
		if _w == 1:
			_tmp = _ring[7]
			_ring[7] = _ring[6]
			_ring[6] = _ring[5]
			_ring[5] = _ring[4]
			_ring[4] = _ring[3]
			_ring[3] = _ring[2]
			_ring[2] = _ring[1]
			_ring[1] = _ring[0]
			_ring[0] = _tmp
		return _ring

	def breath(self, dt=0.03):
		_breathLED = self.ALL_OFF()
		for b in range(200):
			_value = math.cos(b*0.0314) * -70 + 70
			for i in range(8):
				if i == 4:
					_breathLED[i] = _value
				if i == 3 or i == 5:
					_breathLED[i] = _value - 20
				if i == 2 or i == 6:
					_breathLED[i] = _value - 40
				if i == 1 or i == 7:
					_breathLED[i] = _value - 60
				if i == 0:
					_breathLED[i] = _value - 80
			time.sleep(dt)
			self.on(_breathLED)

	def _ledmount(self, _x, _brightness):
		_mount = self.ALL_OFF()
		for i in range(_x):
			_mount[7-i] = _brightness
		return _mount

	def spin(self, _ring, w=0, dt=0.2):
		_tmp = _ring
		self.on(_tmp)
		if dt != 0:
			_tmp = self._spin(w, _tmp)
			time.sleep(dt)
		return _tmp

	def meter(self, _value, brightness=40):
		_ring = self.ALL_OFF()
		if _value < 0:
			raise ValueError("Unexpected '_value' value {0}, _value should not be negective)'".format(_value))
		for i in range(1, 9):
			if _value < 32*i:
				_ring = self._ledmount(i,brightness)
				break
		for i in range(3):
			_ring = self._spin(0, _ring)
		self.on(_ring)
		time.sleep(0.001)

	def destroy(self):
		self._led1.stop()
		self._led2.stop()
		self._led3.stop()
		self._led4.stop()
		self._led5.stop()
		self._led6.stop()
		self._led7.stop()
		self._led8.stop()

class Buzzer(object):
	# Plus Buzzer module of PiPlus from SunFounder
	def __init__(self, port='A'):
		self._port = port
		if self._port == 'A' or self._port == 'a':
			self._Buzzer = DA8
		elif self._port == 'B' or self._port == 'b':
			self._Buzzer = DB8
		else:
			print "port should be 'A' or 'B' like: '(port='A')'"
			quit()
		GPIO.setup(self._Buzzer, GPIO.OUT, initial=0)

	def on(self):
		GPIO.output(self._Buzzer, 0)

	def off(self):
		GPIO.output(self._Buzzer, 1)

	def beep(self, dt=0.5, times=1):	# x for dalay time.
		for i in range(times):
			self.on()
			time.sleep(dt)
			self.off()
			time.sleep(dt)

	def morsecode(self, code, speed=FAST):
		if speed == FAST:
			pause = 0.25
		if speed == SLOW:
			pause = 0.5
		code = code.upper()
		for letter in code:
			for tap in MORSECODE[letter]:
				if tap == '0':
					self.beep(dt=pause/2)
				if tap == '1':
					self.beep(dt=pause)
			time.sleep(pause)

	def destroy(self):
		self.off()

class LED_Bar_Graph(object):
	# Plus LED Bar Graph module of PiPlus from SunFounder
	def __init__(self, port='A'):
			# Plus LED_Bar_Graph module from PiPlus@SunFounder
		if port not in ['A', 'a', 'B', 'b']:
			raise ValueError("Unexpected port value {0}, Set port to 'A' or 'B', like: '(port='A')'".format(port))

		if port in ['A', 'a']:
			self.LED = [CE0, DA1, DA2, DA3, DA4, DA5, DA6, DA7, DA8, CE1]
		elif port in ['B', 'b']:
			self.LED = [CE0, DB1, DB2, DB3, DB4, DB5, DB6, DB7, DB8, CE1]

		for x in self.LED:
			GPIO.setup(x, GPIO.OUT, initial=1)

	def off(self):
		for i in self.LED:
			GPIO.output(i, 1)

	def meter(self, value):
		self.off()
		for i in range(10):
			if value < 25.5*i:
				break
			GPIO.output(self.LED[i], 0)

	def pulse(self, value):
		self.off()
		for i in range(5):
			if value < 51*i:
				break
			GPIO.output(self.LED[i+5], 0)
			GPIO.output(self.LED[4-i], 0)

	def destroy(self):
		self.off()

class RGB_LED(object):
	# Plus RGB LED module of PiPlus from SunFounder
	def __init__(self, port='A'):
		#!/usr/bin/env python
		if port not in ['A', 'a', 'B', 'b']:
			raise ValueError("Unexpected port value {0}, Set port to 'A' or 'B', like: '(port='A')'".format(port))

		if port in ['A', 'a']:
			self._pins = [DA5, DA6, DA7]
		elif port in ['B', 'b']:
			self._pins = [DB5, DB6, DB7]
		for i in self._pins:
			GPIO.setup(i, GPIO.OUT, initial=GPIO.HIGH)   # Set _pins mode to output

		self._R = GPIO.PWM(self._pins[0], 100)  # set Frequece to 100Hz
		self._G = GPIO.PWM(self._pins[1], 100)
		self._B = GPIO.PWM(self._pins[2], 100)

		self._R.start(100)      # Initial duty Cycle = 100(leds off)
		self._G.start(100)
		self._B.start(100)

	def off(self):
		self._R.stop()
		self._G.stop()
		self._B.stop()
		for i in self._pins:
			GPIO.output(i, GPIO.HIGH)    # Turn off all LEDs

	def rgb(self, _R_val, _G_val, _B_val):
		_R_val = Map(_R_val, 0, 255, 0, 100)
		_G_val = Map(_G_val, 0, 255, 0, 100)
		_B_val = Map(_B_val, 0, 255, 0, 100)

		self._R.ChangeDutyCycle(100-_R_val)
		self._G.ChangeDutyCycle(100-_G_val)
		self._B.ChangeDutyCycle(100-_B_val)

	def breath(self, _R_val, _G_val, _B_val, dt = 0.01):
		for x in range(628):
			y = -math.cos(x/100.0)*128+128
			_R = Map(y, 0, 256, 0, _R_val)
			_G = Map(y, 0, 256, 0, _G_val)
			_B = Map(y, 0, 256, 0, _B_val)
			self.rgb(_R, _G, _B)
			time.sleep(dt)

	def hsb(self, _h, _s = 1, _b = 1):
		_hi = (_h/60)%6
		_f = _h / 60.0 - _hi
		_p = _b * (1 - _s)
		_q = _b * (1 - _f * _s)
		_t = _b * (1 - (1 - _f) * _s)

		if _hi == 0:
			_R_val = _b
			_G_val = _t
			_B_val = _p
		if _hi == 1:
			_R_val = _q
			_G_val = _b
			_B_val = _p
		if _hi == 2:
			_R_val = _p
			_G_val = _b
			_B_val = _t
		if _hi == 3:
			_R_val = _p
			_G_val = _q
			_B_val = _b
		if _hi == 4:
			_R_val = _t
			_G_val = _p
			_B_val = _b
		if _hi == 5:
			_R_val = _b
			_G_val = _p
			_B_val = _q
		else:
			_R_val = 0
			_G_val = 0
			_B_val = 0

		try:
			self.rgb(_R_val*255.0, _G_val*255.0, _B_val*255.0)
		except:
			print _R_val, _G_val, _B_val

	def fireup(self):
		_color = [255, 14, 0]
		for i in range(1, 17):
			_rate = ((i * i)-1) / 255.0
			_r = _rate * _color[0]
			_g = _rate * _color[1]
			_b = _rate * _color[2]
			self.rgb(_r, _g, _b)
			time.sleep(0.03)
		for i in range(1, 7):
			_rate = ((i * i)-1) / 255.0
			_r = (1 - _rate) * _color[0]
			_g = (1 - _rate) * _color[1]
			_b = (1 - _rate) * _color[2]
			self.rgb(_r, _g, _b)
			time.sleep(0.03)


	def destroy(self):
		self.off()
		self._R.stop()
		self._G.stop()
		self._B.stop()

class Buttons(object):
	# Plus Buttons module of PiPlus from SunFounder
	def __init__(self, port='A'):
		#!/usr/bin/env python
		if port not in ['A', 'a', 'B', 'b']:
			raise ValueError("Unexpected port value {0}, Set port to 'A' or 'B', like: '(port='A')'".format(port))

		if port in ['A', 'a']:
			self.UP = DA1
			self.LEFT = DA2
			self.DOWN = DA3
			self.RIGHT = DA4
		elif port in ['B', 'b']:
			self.UP = DB1
			self.LEFT = DB2
			self.DOWN = DB3
			self.RIGHT = DB4

		GPIO.setup(self.UP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(self.LEFT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(self.DOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(self.RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	def add_event_detect(self, up_falling=None, left_falling=None, down_falling=None, right_falling=None, up_rising=None, left_rising=None, down_rising=None, right_rising=None, up_both=None, left_both=None, down_both=None, right_both=None):
		_c_up = [up_falling, up_rising, up_both]
		_c_left = [left_falling, left_rising, left_both]
		_c_down = [down_falling, down_rising, down_both]
		_c_right = [right_falling, right_rising, right_both]

		if _c_up.count(None) < 2 or _c_left.count(None) < 2 or _c_down.count(None) < 2 or _c_right.count(None) < 2:
			raise RuntimeError('Conflicting edge detection events, The same button should not be defined as two different edge detection events')
		if up_falling != None:
			GPIO.add_event_detect(self.UP, GPIO.FALLING, callback=up_falling)
		if left_falling != None:
			GPIO.add_event_detect(self.LEFT, GPIO.FALLING, callback=left_falling)
		if down_falling != None:
			GPIO.add_event_detect(self.DOWN, GPIO.FALLING, callback=down_falling)
		if right_falling != None:
			GPIO.add_event_detect(self.RIGHT, GPIO.FALLING, callback=right_falling)

		if up_rising != None:
			GPIO.add_event_detect(self.UP, GPIO.RISING, callback=up_rising)
		if left_rising != None:
			GPIO.add_event_detect(self.LEFT, GPIO.RISING, callback=left_rising)
		if down_rising != None:
			GPIO.add_event_detect(self.DOWN, GPIO.RISING, callback=down_rising)
		if right_rising != None:
			GPIO.add_event_detect(self.RIGHT, GPIO.RISING, callback=right_rising)

		if up_both != None:
			GPIO.add_event_detect(self.UP, GPIO.BOTH, callback=up_both)
		if left_both != None:
			GPIO.add_event_detect(self.LEFT, GPIO.BOTH, callback=left_both)
		if down_both != None:
			GPIO.add_event_detect(self.DOWN, GPIO.BOTH, callback=down_both)
		if right_both != None:
			GPIO.add_event_detect(self.RIGHT, GPIO.BOTH, callback=right_both)

	def destroy(self):
		pass

class Rotary_Encoder(object):
	# Plus Rotary Encoder module of PiPlus from SunFounder
	def __init__(self, port='A'):
		self._port = port
		if port not in ['A', 'a', 'B', 'b']:
			raise ValueError("Unexpected port value {0}, Set port to 'A' or 'B', like: '(port='A')'".format(port))

		if port in ['A', 'a']:
			self._APin	 = DA1    # A Pin
			self._BPin	 = DA2    # B Pin
			self.BTN = DA3    # Button Pin
		elif port in ['B', 'b']:
			self._APin	 = DB1    # A Pin
			self._BPin	 = DB2    # B Pin
			self.BTN = DB3    # Button Pin

		self._flag = 0
		self._Last_RoB_Status = 0
		self._Current_RoB_Status = 0

		GPIO.setup(self._APin, GPIO.IN)    # input mode
		GPIO.setup(self._BPin, GPIO.IN)
		GPIO.setup(self.BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	def add_event_detect(self, btn_falling=None, btn_rising=None, btn_both=None):
		_c_btn = [btn_falling, btn_rising, btn_both]

		if _c_btn.count(None) < 2:
			raise RuntimeError('Conflicting edge detection events, The same button should not be defined as two different edge detection events')

		if btn_falling != None:
			GPIO.add_event_detect(self.BTN, GPIO.FALLING, callback=btn_falling)
		if btn_rising != None:
			GPIO.add_event_detect(self.BTN, GPIO.RISING, callback=btn_rising)
		if btn_both != None:
			GPIO.add_event_detect(self.BTN, GPIO.BOTH, callback=btn_both)

	def rotary_deal(self, _counter, step=1):
		self._Last_RoB_Status = GPIO.input(self._BPin)
		while(not GPIO.input(self._APin)):
			self._Current_RoB_Status = GPIO.input(self._BPin)
			self._flag = 1
		if self._flag == 1:
			self._flag = 0
			if (self._Last_RoB_Status == 0) and (self._Current_RoB_Status == 1):
				_counter = _counter + step
			if (self._Last_RoB_Status == 1) and (self._Current_RoB_Status == 0):
				_counter = _counter - step
		return _counter

	def destroy(self):
		GPIO.remove_event_detect(self.BTN)

class Analog_Port(object):
	def __init__(self):
		self._adc = PCF8591()

	def destroy(self):
		self._adc.destroy()

class Photoresistor(Analog_Port):
	def read(self):
		_value = self._adc.read(AIN0)
		return _value

	def brightness(self):
		return 255 - self._adc.read(AIN0)

class Slide_Potentiometers(Analog_Port):
	def get_value(self, *_sp): # _sp: slider potentiometer
		_sp_value = []
		for _i in _sp:
			_sp_value.append(self._adc.read(_i-1))

		return tuple(_sp_value)

class Joystick(Analog_Port):
	def read(self):
		_x = self._adc.read(AIN0)
		_y = self._adc.read(AIN1)
		_btn = self._adc.read(AIN2)
		return _x, _y, _btn

	def get_status(self):
		_x, _y, _btn = self.read()
		if _btn == 0:
			return 'pressed'
		elif 118 < _x < 138 and 118 < _y < 138:
			return 'home'
		else:
			if _y > 245:
				return 'up'
			if _y < 10:
				return 'down'
			if _x > 245:
				return 'left'
			if _x < 10:
				return 'right'

class Sound_Sensor(Analog_Port):
	def __init__(self):
		self._adc = PCF8591()
		self._tmp = 0
		self._F_tmp = 0

	def read(self):
		_value = self._adc.read(AIN3)
		_value = Map(_value, 150, 255, 0, 255)
		return _value

class LCD1602(object):
	# Plus LCD1602 module of PiPlus from SunFounder
	_LCD_bus = smbus.SMBus(1) # or bus = smbus.SMBus(0) for Revision 1 boards
	def __init__(self, BACKGROUND_LIGHT=1, ADDRESS=0x27, _bus=_LCD_bus):
		self._LCD_bus = _bus
		self._LCD_ADDR = ADDRESS
		self._background_light = BACKGROUND_LIGHT

		self._send_command(0x33) # Must initialize to 8-line mode at first
		time.sleep(0.005)
		self._send_command(0x32) # Then initialize to 4-line mode
		time.sleep(0.005)
		self._send_command(0x28) # 2 Lines & 5*7 dots
		time.sleep(0.005)
		self._send_command(0x0C) # Enable display without cursor
		time.sleep(0.005)
		self._send_command(0x01) # Clear Screen
		self._LCD_bus.write_byte(self._LCD_ADDR, 0x08)

	def _write_data(self, data):
		_tmp = data
		if self._background_light == 1:
			_tmp |= 0x08
		else:
			_tmp &= 0xF7
		self._LCD_bus.write_byte(self._LCD_ADDR, _tmp)

	def _send_data(self, data):
		# Send bit7-4 firstly
		_tmp = data & 0xF0
		_tmp |= 0x05               # RS = 1, RW = 0, EN = 1
		self._write_data(_tmp)
		time.sleep(0.002)
		_tmp &= 0xFB               # Make EN = 0
		self._write_data(_tmp)

		# Send bit3-0 secondly
		_tmp = (data & 0x0F) << 4
		_tmp |= 0x05               # RS = 1, RW = 0, EN = 1
		self._write_data(_tmp)
		time.sleep(0.002)
		_tmp &= 0xFB               # Make EN = 0
		self._write_data(_tmp)

	def _send_command(self, comm):
		# Send bit7-4 firstly
		_tmp = comm & 0xF0
		_tmp |= 0x04               # RS = 0, RW = 0, EN = 1
		self._write_data(_tmp)
		time.sleep(0.002)
		_tmp &= 0xFB               # EN = 0
		self._write_data(_tmp)

		# Send bit3-0 secondly
		_tmp = (comm & 0x0F) << 4
		_tmp |= 0x04               # RS = 0, RW = 0, EN = 1
		self._write_data(_tmp)
		time.sleep(0.002)
		_tmp &= 0xFB               # EN = 0
		self._write_data(_tmp)

	def _openlight(self):  # Enable the backlight
		self._LCD_bus.write_byte(self._LCD_ADDR,0x08)
		self._LCD_bus.close()

	def clear(self):
		self._send_command(0x01) # Clear Screen

	def write(self, x, y, text):
		if x < 0:
			x = 0
		if x > 15:
			x = 15
		if y <0:
			y = 0
		if y > 1:
			y = 1

		# Move cursor
		_addr = 0x80 + 0x40 * y + x
		self._send_command(_addr)
		text = str(text)
		for i in text:
			self._send_data(ord(i))

	def destroy(self):
		self.clear()
		self._LCD_bus.write_byte(self._LCD_ADDR,0xF7)
		self._LCD_bus.close()

class Motion_Sensor(object):
	# Plus Motion Sensor of PiPlus from SunFounder
	_MS_bus = smbus.SMBus(1) # or bus = smbus.SMBus(0) for Revision 1 boards

	def __init__(self, _bus=_MS_bus):
		# Power management registers
		self._power_mgmt_1 = 0x6b
		self._power_mgmt_2 = 0x6c
		self._MS_bus = _bus
		self._address = 0x69
		# Now wake the 6050 up as it starts in sleep mode
		self._MS_bus.write_byte_data(self._address, self._power_mgmt_1, 0)

	def _read_byte(self, _adr):
		return self._MS_bus.read_byte_data(self._address, _adr)

	def _read_word(self, _adr):
		_high = self._MS_bus.read_byte_data(self._address, _adr)
		_low = self._MS_bus.read_byte_data(self._address, _adr+1)
		_val = (_high << 8) + _low
		return _val

	def _read_word_2c(self, _adr):
		_val = self._read_word(_adr)
		if (_val >= 0x8000):
			return -((65535 - _val) + 1)
		else:
			return _val

	def _dist(self, _a, _b):
		return math.sqrt((_a * _a) + (_b * _b))

	def _get_x_rotation(self, _x, _y, _z):
		_radians = math.atan2(_y, self._dist(_x, _z))
		return math.degrees(_radians)

	def _get_y_rotation(self, _x, _y, _z):
		_radians = math.atan2(_x, self._dist(_y, _z))
		return -math.degrees(_radians)

	def get_gyro(self):
		_gyro_xout = self._read_word_2c(0x43)
		_gyro_yout = self._read_word_2c(0x45)
		_gyro_zout = self._read_word_2c(0x47)

		return _gyro_xout, _gyro_yout, _gyro_zout

	def get_scaled_gyro(self):
		_gyro_xout, _gyro_yout, _gyro_zout = self.get_gyro()

		return (_gyro_xout / 131.0), (_gyro_yout / 131.0), (_gyro_zout / 131.0)

	def get_accel(self):
		_accel_xout = self._read_word_2c(0x3b)
		_accel_yout = self._read_word_2c(0x3d)
		_accel_zout = self._read_word_2c(0x3f)

		return _accel_xout, _accel_yout, _accel_zout

	def get_scaled_accel(self):
		_accel_xout, _accel_yout, _accel_zout = self.get_accel()

		_accel_xout_scaled = _accel_xout / 16384.0
		_accel_yout_scaled = _accel_yout / 16384.0
		_accel_zout_scaled = _accel_zout / 16384.0

		return _accel_xout_scaled, _accel_yout_scaled, _accel_zout_scaled

	def get_temp(self):
		_temperature = self._read_word_2c(0x41)
		_temperature = _temperature/340+36.53
		return _temperature

	def get_rotation(self):
		_x, _y, _z = self.get_scaled_accel()
		return self._get_x_rotation(_x, _y, _z), self._get_y_rotation(_x, _y, _z)

	def destroy():
		pass

class DS18B20(object):
	def __init__(self):
		self._ds18b20 = ''
		self.C = 0
		self.F = 1
		os.system('modprobe w1-gpio')
		os.system('modprobe w1-therm')
		while True:
			for i in range(RUNTIME):
				for i in os.listdir('/sys/bus/w1/devices'):
					if i[:3] == '28-':
						self._ds18b20 = i
				if self._ds18b20 != '':
					print 'DS18B20 founded.\nSlave address:', self._ds18b20
					self._location = '/sys/bus/w1/devices/' + self._ds18b20
					break
				time.sleep(0.001)
			if self._ds18b20 != '':
				break
			else:
				print 'Timeout. No device. Check if Plus DS18B20 is pluged in.'
				print 'Press enter to try again, or Crrl + C to quit.'
				_tmp = raw_input()

	def get_temperature(self, unit=0):
		_location = self._location + '/w1_slave'
		while True:
			for i in range(RUNTIME):
				try:
					_tfile = open(_location)
					_text = _tfile.read()
					_tfile.close()
					_secondline = _text.split("\n")[1]
					if _secondline == '00 00 00 00 00 00 00 00 00 t=0':
						_flag = 0
					else:
						_flag = 1
						break
					time.sleep(0.001)
				except:
					_flag = 0
			if _flag == 1:
				break
			else:
				print 'Timeout. No device. Check if Plus DS18B20 is pluged in.'
				print 'Press enter to try again, or Crrl + C to quit.'
				#_tmp = raw_input()
				return None

		_temperaturedata = _secondline.split(" ")[9]
		_temperature = float(_temperaturedata[2:])
		_temperature_c = _temperature / 1000
		if unit == self.C:
			return _temperature_c
		if unit == self.F:
			_temperature_f = _temperature_c * 9.0 / 5.0 + 32.0
			return _temperature_f

	def destroy(self):
		pass

