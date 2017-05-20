#!/usr/bin/python

import time
import math
import RPi.GPIO as GPIO
import os
import commands
import tempfile
import subprocess
import sys
import pismart
from distutils.spawn import find_executable

DIGITAL_CHANNEL = [17, 18, 27, 22, 23, 24, 25, 4]   # wiringPi pin 0~7 -> BCM GPIO

def _write_data(reg, value):
    self.bus.write_byte_data(PWM_ADDRESS, reg, value)
    return -1

def _write_file(filename, str_value):
    fp = open(filename, "w")
    fp.write(str_value)
    fp.close()
    
def _read_file(filename):
    fp = open(filename, "r")
    value = fp.readline()
    fp.close()
    return value

def _test_mode():
    from test import test
    try:
        test.main()
    except KeyboardInterrupt:
        test.pismart.end()

def main_setup():
    global usage_dic, p
    usage_dic = {
        'basic'          :'',
        'speaker_volume' :'',
        'speaker_volume' :'',
        'motor_switch'   :'',
        'servo_switch'   :'',
        'speaker_switch' :'',
        'power_type'     :'',
        'get'            :'',
        'test'           :'',
        'all'            :'',
    }
    usage_dic['basic']          = \
          'Usage:\n' \
        + '  pismart [option] [control]\n\n' \
        + 'Options:\n' \
        + '    speaker_volume    Control the volume for speaker\n' \
        + '    capture_volume    Control the volume for microphone\n' \
        + '    motor_switch      Switch for motor\n' \
        + '    servo_switch      Switch for servo\n' \
        + '    speaker_switch    Switch for speaker\n' \
        + '    power_type        Change power type for alarm\n' \
        + '    get               Get informations you want\n' \
        + '    test              Run test mode\n' \
        + '    start_project     Start an amateur project\n'
    usage_dic['speaker_volume'] = \
          'Usage:\n' \
        + '  pismart speaker_volume [volume]\n\n' \
        + 'volume:      Specified a volume in [0, 100]\n\n' \
        + 'Example:\n' \
        + '  pismart speaker_volume 100  # Set speaker volume to 100%\n'
    usage_dic['capture_volume'] = \
          'Usage:\n' \
        + '  pismart capture_volume [volume]\n\n' \
        + 'volume:      Specified a volume in [0, 100]\n\n' \
        + 'Example:\n' \
        + '  pismart capture_volume 100  # Set capture volume to 100%\n'
    usage_dic['motor_switch'] = \
          'Usage:\n' \
        + '  pismart motor_switch [status]\n\n' \
        + 'status: \n' \
        + '  on/1     Turn the motor switch on\n\n' \
        + '  off/0    Turn the motor switch off\n\n' \
        + 'Example:\n' \
        + '  pismart motor_switch 1  # Turn the motor switch on\n'
    usage_dic['servo_switch'] = \
          'Usage:\n' \
        + '  pismart servo_switch [status]\n\n' \
        + 'status: \n' \
        + '  on/1     Turn the servo switch on\n\n' \
        + '  off/0    Turn the servo switch off\n\n' \
        + 'Example:\n' \
        + '  pismart servo_switch 1  # Turn the servo switch on\n'
    usage_dic['pwm_switch'] = \
          'Usage:\n' \
        + '  pismart pwm_switch [status]\n\n' \
        + 'status: \n' \
        + '  on/1     Turn the pwm switch on\n\n' \
        + '  off/0    Turn the pwm switch off\n\n' \
        + 'Example:\n' \
        + '  pismart pwm_switch 1  # Turn the pwm switch on\n'
    usage_dic['speaker_switch'] = \
          'Usage:\n' \
        + '  pismart speaker_switch [status]\n\n' \
        + 'status: \n' \
        + '  on/1     Turn the speaker switch on\n\n' \
        + '  off/0    Turn the speaker switch off\n\n' \
        + 'Example:\n' \
        + '  pismart speaker_switch 1  # Turn the speaker switch on\n'
    usage_dic['power_type'] = \
          'Usage:\n' \
        + '  pismart power_type [type]\n\n' \
        + 'type:      Specified a power type in 2S/3S/DC, indicate 2S/3S Li-po battery or DC power\n\n' \
        + 'Example:\n' \
        + '  pismart power_type 2S  # Specified the power type as 2S\n'
    usage_dic['get'] = \
          'Usage:\n' \
        + '  pismart get [info]\n\n' \
        + 'info:      Specified an information.\n\n' \
        + 'Avalible informations: \n' \
        + '  voltage       Get power voltage\n' \
        + '  power_type    Get power type\n' \
        + '  cpu_usage     Get cpu usage  \n' \
        + '  cpu_temp      Get cpu temperature \n' \
        + '  gpu_temp      Get gpu temperature \n' \
        + '  ram_info      Get ram infomation  \n' \
        + '  disk_info     Get disk infomation  \n' \
        + 'Example:\n' \
        + '  pismart get voltage  # Get current power voltage\n'
    usage_dic['test'] = \
          'Usage:\n'\
        + '  pismart test  # Run test mode\n\n' \
        + 'Example:\n' \
        + '  pismart test  # Run test mode\n'
    usage_dic['start_project'] = \
          'Usage:\n'\
        + '  pismart start_project [project name] # Run test mode\n\n' \
        + 'Example:\n' \
        + '  pismart start_project my_project     # Run test mode\n'
    usage_dic['all'] = \
          usage_dic['basic'] \
        + usage_dic['speaker_volume'] \
        + usage_dic['capture_volume'] \
        + usage_dic['motor_switch'] \
        + usage_dic['servo_switch'] \
        + usage_dic['speaker_switch'] \
        + usage_dic['power_type'] \
        + usage_dic['get'] \
        + usage_dic['test'] \
        + usage_dic['start_project']
    p = pismart.PiSmart()
    p.DEBUG = 'error'

def usage(opt = 'basic'):
    print usage_dic[opt]
    quit()

def check_command():
    option = ''
    argv_len = len(sys.argv)

    if argv_len < 2:
        usage()
    else:
        option = sys.argv[1]

    if argv_len < 3:
        control = None
    else:
        control = sys.argv[2]
    return option, control

def on_off_handle(on_off):
    if on_off in ['1', 'on', 'On', 'ON']:
        on_off = 1
    elif on_off in ['0', 'off', 'Off', 'OFF']:
        on_off = 0
    else:
        return -1
    return on_off

def print_bar(value, total, unit):
    percentage = round(value *100.0 / total, 1)
    a = ' %s%%    %s%s/%s%s' %(percentage, value, unit, total, unit)
    b = ''
    count = int(round(percentage/10))
    for i in range(count):
        b += "="
    for i in range(10-count):
        b += " "
    print ' [%s] %s' %(b, a)

def start_project(project_name):
    sample = 'sample'
    cmd = 'mkdir %s' % project_name
    code_dir = '%s/%s.py' % (project_name, project_name)
    commands.getoutput(cmd)
    cmd = 'cp /usr/local/bin/%s/* %s/' % (sample, project_name)
    commands.getoutput(cmd)
    cmd = 'mv %s/%s.py %s' % (project_name, sample, code_dir)
    commands.getoutput(cmd)
    code = open(code_dir, 'r')
    lines = code.readlines()
    new_lines = []
    for line in lines:
        if sample in line:
            line = line.replace(sample,project_name)
        new_lines.append(line)
    code.close()
    code = open(code_dir, 'w')
    code.writelines(new_lines)
    code.close()

def main():
    main_setup()
    option, control = check_command()

    if option == 'speaker_volume':
        try:
            control = int(control)
        except:
            usage("speaker_volume")
        if control not in range(0, 101):
            usage("speaker_volume")
        p.volume = control
        print "Set speaker volume %s, Done"%control
    elif option == 'capture_volume':
        try:
            control = int(control)
        except:
            usage("capture_volume")
        if control not in range(0, 101):
            usage("capture_volume")
        p.capture_volume = control
        print "Set capture volume %s, Done"%control
    elif option == 'motor_switch':
        control = on_off_handle(control)
        if control not in [0, 1]:
            usage("motor_switch")
        p.motor_switch(control)
        print "Set motor switch %s, Done"%control
    elif option == 'speaker_switch':
        control = on_off_handle(control)
        if control not in [0, 1]:
            usage("speaker_switch")
        p.speaker_switch(control)
        print "Set speaker switch %s, Done"%control
    elif option == 'servo_switch':
        control = on_off_handle(control)
        if control not in [0, 1]:
            usage("servo_switch")
        p.servo_switch(control)
        print "Set servo switch %s, Done"%control
    elif option == 'pwm_switch':
        control = on_off_handle(control)
        if control not in [0, 1]:
            usage("pwm_switch")
        p.pwm_switch(control)
        print "Set pwm switch %s, Done"%control
    elif option == 'power_type':
        if control not in ['2S', '3S', 'DC']:
            usage("power_type")
        p.power_type = control
        print "Set power type %s, Done"%control
    elif option == 'get':
        if control == 'voltage':
            print "Current power voltage is: %sV"%p.power_voltage
        elif control == 'power_type':
            print "Current power type is: %s"%p.power_type
        elif control == 'cpu_usage':
            print "Current cpu usage is: %s%%"%p.cpu_usage
        elif control == 'cpu_temp':
            print "Current cpu temperature is: %s`C"%p.cpu_temperature
        elif control == 'gpu_temp':
            print "Current gpu temperature is: %s`C"%p.gpu_temperature
        elif control == 'ram_info':
            print "Current ram information:"
            print_bar(p.ram_used, p.ram_total, 'M')
        elif control == 'disk_info':
            print "Current disk information:"
            print_bar(p.disk_used, p.disk_total, 'G')
        else:
            usage("get")
    elif option == 'test':
        _test_mode()
    elif option == 'start_project':
        if control != None:
            start_project(control)
        else:
            usage(option)
    else:
        usage() 
