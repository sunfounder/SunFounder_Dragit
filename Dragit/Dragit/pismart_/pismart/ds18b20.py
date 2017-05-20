from basic import _Basic_class

class DS18B20(_Basic_class):
    #need to enable w1 interface and add 1-wire module 
    #sudo nano /boot/config.txt
    #   add  this content :
    #       dtoverlay = w1-gpio 
    #   sudo nano /etc/modules
    #   add following contents:
    #       w1-gpio
    #       w1-therm

    RUNTIME = 1000
    def __init__(self):
        self._ds18b20 = ''
        self.C = 0
        self.F = 1
        self.run_command('sudo modprobe w1-gpio')
        self.run_command('sudo modprobe w1-therm')
        while True:
            for i in range(self.RUNTIME):
                for i in os.listdir('/sys/self.bus/w1/devices'):
                    if i[:3] == '28-':
                        self._ds18b20 = i
                if self._ds18b20 != '':
                    print 'DS18B20 founded.\nSlave address:', self._ds18b20
                    self._location = '/sys/self.bus/w1/devices/' + self._ds18b20
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
            for i in range(self.RUNTIME):
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
                _tmp = raw_input()

        _temperaturedata = _secondline.split(" ")[9]
        _temperature = float(_temperaturedata[2:])
        _temperature_c = _temperature / 1000
        if unit == self.C:
            return _temperature_c
        if unit == self.F:
            _temperature_f = _temperature_c * 9.0 / 5.0 + 32.0
            return _temperature_f