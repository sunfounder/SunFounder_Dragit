from basic import _Basic_class
from distutils.spawn import find_executable

class TTS(_Basic_class):

    _class_name = 'TTS'
    ENGINE_LIST = ['festival', 'espeak', 'pico']

    def __init__(self, engine='pico'):
        self.engine = engine
        self._lang = "en-US"
        self.logger_setup()
        self.words = "Hello, I'm Pi Smart"

    def _check_executable(self, executable):
        executable_path = find_executable(executable)
        found = executable_path is not None
        return found

    @property
    def say(self):
        self.write(self.words)
        return self.words
    @say.setter
    def say(self, words):
        self.write(words)
        return self.words

    def write(self, words):
        self._debug('Engine [%s], say:\n [%s]' % (self.engine, words)) 
        if self.engine == 'festival':
            if self._check_executable('festival'):
                cmd = "echo '%s' | festival --tts & " % words
                self.run_command(cmd)
                self._debug('command: %s' %cmd)
            else:
                self._debug('Festival is busy. Pass')
        if self.engine == 'espeak':
            if self._check_executable('espeak'):
                cmd = 'espeak -a%d -s%d -g%d -p%d \"%s\" 2>/dev/null & ' % (self._amp, self._speed, self._gap, self._pitch, words)
                self.run_command(cmd)
                self._debug('command: %s' %cmd)
            else:
                self._debug('Festival is busy. Pass')
        if self.engine == 'pico':
            if self._check_executable('pico2wave') and self._check_executable('aplay'):
                cmd = 'pico2wave -l %s -w /tmp/pico.wav "%s" && aplay /tmp/pico.wav' % (self._lang, words)
                self.run_command(cmd)
                self._debug('command: %s' %cmd)
            else:
                self._debug('Festival is busy. Pass')

    def end(self):
        pass

    @property
    def lang(self):
        return self._lang
    
    @lang.setter
    def lang(self, value):
        self.lang = value

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, value):
        if value not in self.ENGINE_LIST:
            raise ValueError ("Engine should be one of \"{0}\", not \"{1}\".".format(self.ENGINE_LIST, engine))
        self._engine = value
        if self._engine == 'espeak':
            self._amp   = 100 
            self._speed = 175
            self._gap   = 5
            self._pitch = 50

    def espeak_params(self, amp=None, speed=None, gap=None, pitch=None):
        if self.engine != 'espeak':
            raise ValueError ('The TTS engine you choose is "{0}", please choose "espeak" to set espeak_params.\n \
                To choose espeak: TTS.engine = "espeak"').format(self.engine)
        else:
            if amp == None: 
                amp=self._amp
            if speed == None:
                speed=self._speed
            if gap == None:
                gap=self._gap
            if pitch == None:
                pitch=self._pitch

            if amp not in range(0, 200):
                raise ValueError('Amp should be in 0 to 200, not "{0}"').format(amp)
            if speed not in range(80, 260):
                raise ValueError('Amp should be in 80 to 260, not "{0}"').format(speed)
            if pitch not in range(0, 99):
                raise ValueError('Amp should be in 0 to 99, not "{0}"').format(pitch)   
            self._amp   = amp
            self._speed = speed
            self._gap   = gap
            self._pitch = pitch
