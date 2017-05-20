from basic import _Basic_class

class PWM(_Basic_class):
    _class_name = "PWM"
    PWM_ADDRESS         = 0x40

    _LED0_ON_L          = 0x06
    _LED0_ON_H          = 0x07
    _LED0_OFF_L         = 0x08
    _LED0_OFF_H         = 0x09

    _MODE1              = 0x00
    _MODE2              = 0x01
    _SUBADR1            = 0x02
    _SUBADR2            = 0x03
    _SUBADR3            = 0x04
    _PRESCALE           = 0xFE
    _LED0_ON_L          = 0x06
    _LED0_ON_H          = 0x07
    _LED0_OFF_L         = 0x08
    _LED0_OFF_H         = 0x09
    _ALL_LED_ON_L       = 0xFA
    _ALL_LED_ON_H       = 0xFB
    _ALL_LED_OFF_L      = 0xFC
    _ALL_LED_OFF_H      = 0xFD

    _RESTART            = 0x80
    _SLEEP              = 0x10
    _ALLCALL            = 0x01
    _INVRT              = 0x10
    _OUTDRV             = 0x04

    def __init__(self, channel):
        self.logger_setup()
        self.channel = channel

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, channel):
        if isinstance(channel, list):
            for i in channel:
                self.is_channel_available(i)
            self.is_channel_list = True
        elif isinstance(channel, int):
            self.is_channel_available(channel)
            self.is_channel_list = False
        else:
            raise TypeError("PWM channel must be integer or list of integer")
        self._channel = channel
        self._debug("Channel set to %s" % self._channel)

    def is_channel_available(self, channel):
        if channel not in range(16):
            raise ValueError("PWM channel \"{0}\" is not in (0, 15).".format(channel))

    @property
    def frequency(self):
        return _frequency

    @frequency.setter
    def frequency(self, freq):
        '''Set PWM frequency'''
        self._debug('Set frequency to %d' % freq)
        self._frequency = freq
        prescale_value = 25000000.0
        prescale_value /= 4096.0
        prescale_value /= float(freq)
        prescale_value -= 1.0
        self._debug('Setting PWM frequency to %d Hz' % freq)
        self._debug('Estimated pre-scale: %d' % prescale_value)
        prescale = int(prescale_value + 0.5)
        self._debug('Final pre-scale: %d' % prescale)

        old_mode = self.bus.read_byte_data(self._MODE1);
        new_mode = (old_mode & 0x7F) | 0x10
        self.bus.write_byte_data(self._MODE1, new_mode)
        self.bus.write_byte_data(self._PRESCALE, int(math.floor(prescale)))
        self.bus.write_byte_data(self._MODE1, old_mode)
        time.sleep(0.005)
        self._write_byte_data(self._MODE1, old_mode | 0x80)

    def set_PWM(self, on, off=0):
        if on<off:
            raise ValueError('PWM ontime value must larger than offtime. "{}" is lower than "{}".'.format(on, off))
        elif on < 0 or on > 4095 or off < 0 or off > 4095:
            raise ValueError('ontime or offtime must be in(0, 4095)')
        if not self.is_channel_list :
            channel = [self.channel]
            self.bus.write_byte_data(self.PWM_ADDRESS, self._LED0_ON_L+4*self.channel, off & 0xFF)
            self.bus.write_byte_data(self.PWM_ADDRESS, self._LED0_ON_H+4*self.channel, off >> 8)
            self.bus.write_byte_data(self.PWM_ADDRESS, self._LED0_OFF_L+4*self.channel, on & 0xFF)
            self.bus.write_byte_data(self.PWM_ADDRESS, self._LED0_OFF_H+4*self.channel, on >> 8)
        else:
            for channel in self.channel:
                self.bus.write_byte_data(self.PWM_ADDRESS, self._LED0_ON_L+4*channel, off & 0xFF)
                self.bus.write_byte_data(self.PWM_ADDRESS, self._LED0_ON_H+4*channel, off >> 8)
                self.bus.write_byte_data(self.PWM_ADDRESS, self._LED0_OFF_L+4*channel, on & 0xFF)
                self.bus.write_byte_data(self.PWM_ADDRESS, self._LED0_OFF_H+4*channel, on >> 8)

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self.set_PWM(value)
        self._value = value