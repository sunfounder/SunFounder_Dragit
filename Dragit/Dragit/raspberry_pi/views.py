# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
import commands, os
import RPi.GPIO as GPIO
import time
from Dragit.libs.modules.bcm_gpio import BCM_GPIO as BCM_GPIO

GPIO.setmode(GPIO.BCM)

rpi_bcm_chn = [17, 18, 27, 22, 23, 24, 25, 4, 5, 6, 13, 19, 26, 12, 16, 20, 21]
pin_obj=[]

for x in rpi_bcm_chn:
    # creat object for each pin, so that can use the object to open or close pwm
    pin_obj.append(BCM_GPIO(x))

def pin(num):
    # return pin object
    n = rpi_bcm_chn.index(num)
    print ("pin ", rpi_bcm_chn[n])
    return pin_obj[n]

def set_pwm(chn, dc=None, freq=None):
    if dc == -1:
        dc = None
    if freq == -1:
        freq = None
    pin(chn).pwm_output(dc=dc, freq=freq)
    result = "set %s as pwm, dc=%s, freq=%s"%(chn, dc, freq)
    return result

def volume_set_pwm(vol_pwm_pin, vol_pwm_val):
    # Formate data in function, to make Code Reuse
    vol_pin = vol_pwm_pin.encode('utf8').split(',')
    vol_val = vol_pwm_val.encode('utf8').split(',')
    pwm_result = ""
    for x in range(0, len(vol_pin)):
        set_pwm(int(vol_pin[x]), float(vol_val[x]))
        pwm_result += ("  %s. pin = %s val = %s \n"%(x, vol_pin[x], vol_val[x]))
    result = "volume set pwm: \n" + pwm_result
    return result

def destroy_pwm(chn):
    pin(chn).end()
    result = "destroy_pwm, pin %s"%chn
    return result

def gpio(chn, direction, status):
    if direction == 'output':
        pin(chn).output(status)
    elif direction == 'input':
        result = pin(chn).input()
        print "result = %s" % result
        return result

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

def get_datetime(name):
    current_date_time = time.localtime()
    if name == 'year':
        return current_date_time.tm_year
    elif name == 'month':
        return current_date_time.tm_mon
    elif name == 'day of month':
        return current_date_time.tm_mday
    elif name == 'hour':
        return current_date_time.tm_hour
    elif name == 'minute':
        return current_date_time.tm_min
    elif name == 'second':
        return current_date_time.tm_sec
    elif name == 'weekday':
        return current_date_time.tm_wday
    elif name == 'day of year':
        return current_date_time.tm_yday

def run(request):
    print "Raspberry Pi run function start."
    debug = ''
    action = None
    result = None
    value0 = None
    value1 = None
    value2 = None
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

    # ================GPIO Ports =================
    if action == "gpio":
        # Control gpio input or output
        direction = value0
        chn  = int(value1)
        status    = value2
        result = gpio(chn, direction, status)

    elif action == "set_pwm":
        chn  = int(value0)
        dc   = float(value1)
        freq = int(value2)
        result = set_pwm(chn, dc, freq)

    elif action == "volume_set_pwm":
        vol_pwm_pin = value0
        vol_pwm_val = value1
        result = volume_set_pwm(vol_pwm_pin, vol_pwm_val)

    elif action == "stop_pwm":
        pin = int(value0)
        result = destroy_pwm(pin)

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

    elif action == "get_datetime":
        name = value0
        result = get_datetime(name)

    else:
        print "action undefined"
    print("result: %s"%result)
    return HttpResponse(result)
