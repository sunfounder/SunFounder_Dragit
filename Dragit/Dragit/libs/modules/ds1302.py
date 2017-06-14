#!/usr/bin/env python
#-----------------------------------------------------
#
#		This is a program for DS1302 RTC Module.
#	It provide precision timmer.
#
#		This program depend on rpi_time.py.
#
#		ds1302 Module 			   Pi
#			VCC ------------------ 5 V (Must be 5v)
#			GND ------------------ GND
#			SCL ---------------- BCM GPIO 23
#			SDA ---------------- BCM GPIO 24
#			RST ---------------- BCM GPIO 25
#
#-----------------------------------------------------
from datetime import datetime
import rpi_time
import time

rtc = rpi_time.DS1302()

def setup():
	print ''
	print ''
	print rtc.get_datetime()
	print ''
	print ''
	a = raw_input( "Do you want to setup date and time?(y/n) ")
	if a == 'y' or a == 'Y':
		date = raw_input("Input date:(YYYY MM DD week) ")
		time = raw_input("Input time:(HH MM SS) ")
		date = date.split()
		time = time.split()
		print ''
		print ''
		rtc.set_datetime(date, time)
		dt = rtc.get_datetime()
		print "You set the date and time to:", dt

def loop():
	while True:
		a = rtc.get_datetime()
		print a
		time.sleep(0.5)

def destory():
	pass				# Release resource

if __name__ == '__main__':		# Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destory()
