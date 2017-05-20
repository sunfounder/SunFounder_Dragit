from basic import _Basic_class

class ADC(_Basic_class):
    _class_name = 'ADC'
    CHANNEL0_HIGH       = 0x10
    CHANNEL0_LOW        = 0x11
    CHANNEL1_HIGH       = 0x12
    CHANNEL1_LOW        = 0x13
    CHANNEL2_HIGH       = 0x14
    CHANNEL2_LOW        = 0x15
    CHANNEL3_HIGH       = 0x16
    CHANNEL3_LOW        = 0x17
    CHANNEL4_HIGH       = 0x18
    CHANNEL4_LOW        = 0x19
    POWER_VOLTAGE_HIGH  = 0x1a
    POWER_VOLTAGE_LOW   = 0x1b

    ANALOG_CHANNEL = [CHANNEL0_HIGH, CHANNEL1_HIGH, CHANNEL2_HIGH, CHANNEL3_HIGH, CHANNEL4_HIGH, POWER_VOLTAGE_HIGH]

    def __init__(self, channel, debug=0):
        self.logger_setup()
        self.channel = channel
        self.DEBUG = debug

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, channel):
        if channel not in range(6):
            raise ValueError("ADC channel \"{0}\" is not in (0, 5).".format(channel))
        self._channel = channel
        self._debug("Channel set to %s" % self._channel)

    def read(self, delay=0.000001):
        value_return = 0
        raw_value = [0, 0]
        try:
            raw_value[0] = self._read_sys_byte(self.ANALOG_CHANNEL[self.channel], delay=delay)
            self._debug('Read high value = 0x%2X' % raw_value[0])
            raw_value[1] = self._read_sys_byte(self.ANALOG_CHANNEL[self.channel]+1, delay=delay)
            self._debug('Read low value = 0x%2X' % raw_value[1])
            value_return = (raw_value[0] << 8) + (raw_value[1])
            self._debug('Read value = %d ' % value_return)
            return value_return
        except Exception, e:
            self._error(e)
            return False
