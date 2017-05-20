# -*- coding: utf-8 -*-
import smbus
import logging
import time
import commands
import tempfile
import subprocess

class _Basic_class(object):
    _class_name = '_Basic_class'
    _DEBUG = 0
    DEBUG_LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL,
              }
    DEBUG_NAMES = ['critical', 'error', 'warning', 'info', 'debug']

    bus = smbus.SMBus(1)
    SYS_ADDRESS = 0x10

    def __init__(self):
        self.logger_setup()
        
    def logger_setup(self):
        self.logger = logging.getLogger(self._class_name)
        self.ch = logging.StreamHandler()
        form = "%(asctime)s	[%(levelname)s]	%(message)s"
        self.formatter = logging.Formatter(form)
        self.ch.setFormatter(self.formatter)
        self.logger.addHandler(self.ch)
        self._debug    = self.logger.debug
        self._info     = self.logger.info
        self._warning  = self.logger.warning
        self._error    = self.logger.error
        self._critical = self.logger.critical

    @property
    def DEBUG(self):
        return self._DEBUG
    
    @DEBUG.setter
    def DEBUG(self, debug):
        if debug in range(5):
            self._DEBUG = self.DEBUG_NAMES[debug]
        elif debug in self.DEBUG_NAMES:
            self._DEBUG = debug
        else:
            raise ValueError('Debug value must be 0(critical), 1(error), 2(warning), 3(info) or 4(debug), not \"{0}\".'.format(debug))  
        self.logger.setLevel(self.DEBUG_LEVELS[self._DEBUG])
        self.ch.setLevel(self.DEBUG_LEVELS[self._DEBUG])
        self._debug('Set logging level to [%s]' % self._DEBUG)

    def run_command(self, cmd):
        self._debug('Run command: "%s"' % cmd)
        with tempfile.TemporaryFile() as f:
            subprocess.call(cmd, shell=True, stdout=f, stderr=f)
            f.seek(0)
            output = f.read()
            return output

    def _map(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def _write_sys_byte(self, value):
        self._info('Write "0x%02X" to I2C_dev(0x%02X)' % (value, self.SYS_ADDRESS))
        self._debug('└─Write "0x%02X" to I2C_dev(0x%02X) start' % (value, self.SYS_ADDRESS))
        self.bus.write_byte(self.SYS_ADDRESS, value)
        self._debug("└─Done")

    def _read_sys_byte(self, reg, delay=0):
        self._info('Read from I2C_dev(0x%02X) at "0x%02X"' % (self.SYS_ADDRESS, reg))
        self._debug('└─Write "0x%02X" to I2C_dev(0x%02X)' % (reg, self.SYS_ADDRESS))
        self.bus.write_byte(self.SYS_ADDRESS, reg)
        self._debug("└─Done")
        if delay != 0:
            time.sleep(delay)

        self._debug('└─Read from I2C_dev(0x%02X)' % (self.SYS_ADDRESS))
        number = self.bus.read_byte(self.SYS_ADDRESS)
        self._debug('└─Done, read value: "0x%02X"' % number)
        if delay != 0:
            time.sleep(delay)
        return number
        
    def end(self):
        pass        
