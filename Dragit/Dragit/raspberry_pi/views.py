# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
import commands, os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def ram_info():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return line.split()[1:4]

def disk_space():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()
        if i==2:
            return line.split()[1:5]


def cpu_temperature():
    raw_cpu_temperature = commands.getoutput("cat /sys/class/thermal/thermal_zone0/temp")
    cpu_temperature = float(raw_cpu_temperature)/1000
    #cpu_temperature = 'Cpu temperature : ' + str(cpu_temperature)
    return cpu_temperature

def gpu_temperature():
    raw_gpu_temperature = commands.getoutput( '/opt/vc/bin/vcgencmd measure_temp' )
    gpu_temperature = float(raw_gpu_temperature.replace( 'temp=', '' ).replace( '\'C', '' ))
    #gpu_temperature = 'Gpu temperature : ' + str(gpu_temperature)
    return gpu_temperature

def cpu_usage():
    result = str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip())
    return result

def ram_total():
    ram_total = round(int(ram_info()[0]) / 1000,1)
    return ram_total

def ram_used():
    ram_used = round(int(ram_info()[1]) / 1000,1)
    return ram_used

def disk_total():
    disk_total = float(disk_space()[0][:-1])
    return disk_total

def disk_used():
    disk_used = float(disk_space()[1][:-1])
    return disk_used

def get_i2c_address(busnum):
    cmd = "ls /dev/i2c-%d" % busnum
    output = commands.getoutput(cmd)
    print 'Commands "%s" output:' % cmd
    print output
    if '/dev/i2c-%d' % busnum in output.split(' '):
        print "I2C device setup OK"
    else:
        print "Seems like I2C have not been set, Use 'sudo raspi-config' to set I2C"
        return 'null'
    cmd = "i2cdetect -y %s" % busnum
    output = commands.getoutput(cmd)
    print "i2cdetect output:"
    print output
    outputs = output.split('\n')[1:]
    addresses = []
    for tmp_addresses in outputs:
        tmp_addresses = tmp_addresses.split(':')[1]
        tmp_addresses = tmp_addresses.strip().split(' ')
        for address in tmp_addresses:
            if address != '--':
                addresses.append(address)
    print "Conneceted i2c device:"
    address = []
    if addresses == []:
        print "No I2C devices connected"
        return "No I2C devices connected"
    else:
        for a in addresses:
            address.append("0x%s" % a)
    return str(address).replace("'", '').strip('[]').replace(' ','')

def run(request):
    print "Raspberry Pi run function start."
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

    # ================ GPIO Ports =================
    if action == "gpio":
        print "start"
        direction = value0
        channel = int(value1)
        if direction == 'output':
            status = value2
            if status == "HIGH":
                status = 1
            elif status == "LOW":
                status = 0
            GPIO.setup(channel, GPIO.OUT)
            GPIO.output(channel, status)
        elif direction == 'input':
            GPIO.setup(channel, GPIO.IN)
            result = GPIO.input(channel)
            print "result = %s" % result
        else:
            print "direction error"
    elif action == "cpu_temperature":
        # Get CPU Temperature in Celcius
        result = cpu_temperature()
    elif action == "gpu_temperature":
        # Get GPU Temperature in Celcius
        result = gpu_temperature()
    elif action == "ram_total":
        # Get Ram Total
        result = ram_total()
    elif action == "ram_used":
        # Get Ram Used
        result = ram_used()
    elif action == "disk_total":
        # Get Disk Total
        result = disk_total()
    elif action == "disk_used":
        # Get Disk Used
        result = disk_used()
    elif action == "cpu_usage":
        # Get CPU Usage
        result = cpu_usage()
    elif action == "i2cdetect":
        busnum = int(value0)
        result = get_i2c_address(busnum)
    else:
        print "action undefined"
    print("result: %s"%result)
    return HttpResponse(result)
