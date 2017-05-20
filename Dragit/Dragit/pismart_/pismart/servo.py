from basic import _Basic_class
from pwm import PWM

class Servo(PWM):
    _class_name = 'Servo'
    ALL = range(8)

    def __init__(self, channel, offset=0):
        self.logger_setup()
        self.offset = offset
        #self.pulse_width_cal()
        self.frequency          = 60
        self.min_pulse_width    = 600
        self.max_pulse_width    = 2400
        self.channel = channel

    @property
    def min_pulse_width(self):
        return self._min_pulse_width
    @min_pulse_width.setter
    def min_pulse_width(self, value):
        if isinstance(value, int):
            self._min_pulse_width = value
        else:
            self._error('Min pulse width value must be int')
    @property
    def max_pulse_width(self):
        return self._max_pulse_width
    @max_pulse_width.setter
    def max_pulse_width(self, value):
        if isinstance(value, int):
            self._max_pulse_width = value
        else:
            self._error('Max pulse width value must be int')
    @property
    def frequency(self):
        return self._frequency
    @frequency.setter
    def frequency(self, value):
        if isinstance(value, int):
            self._frequency = value
        else:
            self._error('Max pulse width value must be int')

    @property
    def channel(self):
        return self._channel
    # over write parent class PWM property channel
    @channel.setter      
    def channel(self, channel):
        if isinstance(channel, list):  # Argument channel is a list
            for i in channel:
                self.is_channel_available(i)
            self.is_channel_list = True
        elif isinstance(channel, int):  # Argument channel is int
            self.is_channel_available(channel)
            self.is_channel_list = False
        else:
            raise TypeError("PWM channel must be integer or list of integer")
        self._channel = channel
        self._debug("Channel set to %s" % self._channel)
        self.angle = 90
    # over write parent class PWM is_channel_available property
    def is_channel_available(self, channel):
        if channel not in range(8):
            raise ValueError("Servo channel \"{0}\" is not in (0, 7).".format(channel))

    def _angle_to_analog(self, angle):
        pulse_wide   = self._map(angle, 0, 180, self._min_pulse_width, self._max_pulse_width)
        analog_value = int(float(pulse_wide) / 1000000 * self.frequency * 4096)
        return analog_value

    @property
    def angle(self):
        return self._angle
    @angle.setter
    def angle(self, angle):
        self.write(angle)
        self._angle = angle

    def write(self, angle):
        if angle < 0:
            angle = 0
        elif angle > 180:
            angle = 180      
        value = self._angle_to_analog(angle)
        self._debug('Servo turn angle: [%d], PWM value: [%d]' % (angle, value))
        value += self._offset
        self._debug('Servo turn offset: [%d], PWM value: [%d]' % (self._offset, value))
        self._info('Servo turn channel: [%s] to angle: [%d]' % (self.channel, angle))
        self.set_PWM(value)

    def turn(self, angle):
        self.write(angle)

    @property
    def offset(self):
        return self._offset
    
    @offset.setter
    def offset(self, value):
        self._offset = value
