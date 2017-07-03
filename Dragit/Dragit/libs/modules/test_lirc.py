#!/usr/bin/python

import pylirc, time
blocking = 0

def setup():
	integer = pylirc.init("my_lirc", "./pylirc_conf", blocking)

def loop():
	while True:
		ir_codes = pylirc.nextcode(1)
		if ir_codes != None:
			print("ircodes = %s"%ir_codes)
		time.sleep(0.05)

def destroy():
	pylirc.exit()

if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		destroy()

