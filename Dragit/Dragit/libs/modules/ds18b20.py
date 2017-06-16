import os
import time

class DS18B20(object):

    _RUNTIME = 1000
    C = 'c'
    F = 'f'
    def __init__(self):
        print("DS18B20 init")
        self._ds18b20 = []
        print('DS18B20: Start searching ds18b20 addresses')
        self._unit = self.C
        for i in range(self._RUNTIME):
            for i in os.listdir('/sys/bus/w1/devices'):
                if i[:3] == '28-':
                    self._ds18b20.append(i)
            self.mount = len(self._ds18b20)
            if self.mount > 0:
                print('DS18B20: DS18B20 founded.')
                print('DS18B20: Slave addresses:')
                for i in range(self.mount):
                    print('DS18B20: Device: %d  Address: %s' % (i,self._ds18b20[i]))
                break
            time.sleep(0.001)
        if self.mount < 0:
            print('DS18B20: Timeout. No devices. Check if DS18B20 is connected.')

    @property
    def unit(self):
        return self._unit.upper()

    @unit.setter
    def unit(self, value):
        if value not in ['c', 'f']:
            print('DS18B20 ERROR: unit should be set to "C" or "F"')
            raise ValueError('unit should be set to "C" or "F"')
        self._unit = value

    def get_temperature(self, index):
        _location = '/sys/bus/w1/devices/%s/w1_slave' % self._ds18b20[index]
        print('DS18B20: Read device: %s'%_location)
        _flag = 0
        for i in range(self._RUNTIME):
            try:
                _tfile = open(_location)
                _text = _tfile.read()
                _tfile.close()
                _firstline = _text.split("\n")[0]
                _secondline = _text.split("\n")[1]
                status = _firstline.split(' ')[-1]
                if status != 'YES':
                    _flag = 0
                    self._warning('DS18B20@%s value error'%self._ds18b20[index])
                else:
                    _flag = 1
                    break
                time.sleep(0.001)
            except:
                _flag = 0

        if _flag == 1:
            _temperaturedata = _secondline.split(" ")[-1]
            print("DS18B20: Raw data: %s"%_temperaturedata)
            _temperature = float(_temperaturedata.split('=')[1])
            print("DS18B20: Raw value: %s"%_temperature)
            _temperature_c = _temperature / 1000
            print("DS18B20: Temperatue in Celsius: %s C"%_temperature_c)
            _temperature_f = _temperature_c * 9.0 / 5.0 + 32.0
            print("DS18B20: Temperatue in Fahrenheit: %s F"%_temperature_f)

            if self.unit.lower() == self.C:
                return _temperature_c
            elif self.unit.lower() == self.F:
                return _temperature_f
        else:
            print('DS18B20 ERROR: Timeout. No device. Check if device is connected correctly.')
            return "CRC ERROR"

    def get_all(self):
        result = []
        for i in range(self.mount):
            result.append(get_temperature(i))
        return result

def destroy():
    pass

def test():
    my_18b20 = DS18B20()
    while True:
        my_18b20.get_temperature(0)
        time.sleep(0.5)

if __name__ == '__main__':
    try:
        test()
    except KeyboardInterrupt:
        destroy()