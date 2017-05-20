import pismart
from basic import _Basic_class

class PiSmart(_Basic_class):
    _class_name = 'Amateur PiSmart'

    ON = 1
    OFF = 0

    def __init__(self, *item):
        self._ps            = pismart.PiSmart()
        self._ps.DEBUG = 'error'
        self.servo_switch   = self._ps.servo_switch
        self.pwm_switch     = self._ps.pwm_switch
        self.motor_switch   = self._ps.motor_switch
        self.speaker_switch = self._ps.speaker_switch
        if len(item) == 0:
            self.ALL_init()
        elif item == "manual":
            pass

    def ALL_init(self):
        self.ADC_init()
        self.Servo_init()
        self.LED_init()
        self.Motor_init()
        self.TTS_init()
        self.STT_init()

    def ADC_init(self):
        from adc import ADC
        self._A0 = ADC(0)
        self._A1 = ADC(1)
        self._A2 = ADC(2)
        self._A3 = ADC(3)
        self._A4 = ADC(4)
        self._A0.DEBUG = 'error'
        self._A1.DEBUG = 'error'
        self._A2.DEBUG = 'error'
        self._A3.DEBUG = 'error'
        self._A4.DEBUG = 'error'

    def Servo_init(self):
        from servo import Servo
        self._servo0 = Servo(0)
        self._servo1 = Servo(1)
        self._servo2 = Servo(2)
        self._servo3 = Servo(3)
        self._servo4 = Servo(4)
        self._servo5 = Servo(5)
        self._servo6 = Servo(6)
        self._servo7 = Servo(7)
        self.servo_switch(self.ON)
        self._servo0.DEBUG = 'error'
        self._servo1.DEBUG = 'error'
        self._servo2.DEBUG = 'error'
        self._servo3.DEBUG = 'error'
        self._servo4.DEBUG = 'error'
        self._servo5.DEBUG = 'error'
        self._servo6.DEBUG = 'error'
        self._servo7.DEBUG = 'error'

    def PWM_init(self):
        from pwm import PWM
        self._pwm0 = PWM(0)
        self._pwm1 = PWM(1)
        self._pwm2 = PWM(2)
        self._pwm3 = PWM(3)
        self._pwm4 = PWM(4)
        self._pwm5 = PWM(5)
        self._pwm6 = PWM(6)
        self._pwm7 = PWM(7)
        self.pwm_switch(self.ON)
        self._pwm0.DEBUG = 'error'
        self._pwm1.DEBUG = 'error'
        self._pwm2.DEBUG = 'error'
        self._pwm3.DEBUG = 'error'
        self._pwm4.DEBUG = 'error'
        self._pwm5.DEBUG = 'error'
        self._pwm6.DEBUG = 'error'
        self._pwm7.DEBUG = 'error'

    def LED_init(self):
        from led import LED
        self._led = LED()
        self._led.DEBUG = 'error'

    def Motor_init(self):
        from motor import Motor
        self._motor_a = Motor(Motor.MotorA)
        self._motor_b = Motor(Motor.MotorB)
        self._motor_a.DEBUG = 'error'
        self._motor_b.DEBUG = 'error'
        self.motor_switch(self.ON)

    def TTS_init(self):
        from tts import TTS
        self._tts = TTS()
        self._tts.DEBUG = 'error'
        self.speaker_switch(self.ON)
        self.speaker_volume = 100

    def STT_init(self):
        from stt import STT
        self._stt = STT('dictionary', name_calling=False, timeout=10.0, dictionary_update=True)
        self._stt.DEBUG = 'error'
        self.capture_volume = 100

    def ADC_end(self):
        pass
    
    def Servo_end(self):
        self.servo_switch(self.OFF)

    def PWM_end(self):
        self.pwm_switch(self.OFF)

    def Motor_end(self):
        self._motor_a.stop()
        self._motor_b.stop()
        self.motor_switch(self.OFF)

    def LED_end(self):
        self.LED = 0

    def TTS_end(self):
        self._tts.end()
        self.speaker_switch(self.OFF)

    def STT_end(self):
        self._stt.end()


    def end(self):
        self.ADC_end()
        self.LED_end()
        self.Motor_end()
        self.Servo_end()
        self.PWM_end()
        self.STT_end()

    @property
    def power_type(self):
        return self._ps.power_type
    @power_type.setter
    def power_type(self, value):
        self._ps.power_type = value
    @property
    def power_voltage(self):
        return self._ps.power_voltage
    @power_voltage.setter
    def power_voltage(self, value):
        self._ps.power_voltage = value
    @property
    def speaker_volume(self):
        return self._ps.speaker_volume
    @speaker_volume.setter
    def speaker_volume(self, value):
        self._ps.speaker_volume = value
    @property
    def capture_volume(self):
        return self._ps.capture_volume
    @capture_volume.setter
    def capture_volume(self, value):
        self._ps.capture_volume = value
    @property
    def cpu_temperature(self):
        return self._ps.cpu_temperature

    @property
    def A0(self):
        return self._A0.read()
    @property
    def A1(self):
        return self._A1.read()
    @property
    def A2(self):
        return self._A2.read()
    @property
    def A3(self):
        return self._A3.read()
    @property
    def A4(self):
        return self._A4.read()

    @property
    def Servo0(self):
        return self._servo0.angle
    @Servo0.setter
    def Servo0(self, angle):
        self._servo0.angle = angle
    @property
    def Servo1(self):
        return self._servo1.angle
    @Servo1.setter
    def Servo1(self, angle):
        self._servo1.angle = angle
    @property
    def Servo2(self):
        return self._servo2.angle
    @Servo2.setter
    def Servo2(self, angle):
        self._servo2.angle = angle
    @property
    def Servo3(self):
        return self._servo3.angle
    @Servo3.setter
    def Servo3(self, angle):
        self._servo3.angle = angle
    @property
    def Servo4(self):
        return self._servo4.angle
    @Servo4.setter
    def Servo4(self, angle):
        self._servo4.angle = angle
    @property
    def Servo5(self):
        return self._servo5.angle
    @Servo5.setter
    def Servo5(self, angle):
        self._servo5.angle = angle
    @property
    def Servo6(self):
        return self._servo6.angle
    @Servo6.setter
    def Servo6(self, angle):
        self._servo6.angle = angle
    @property
    def Servo7(self):
        return self._servo7.angle
    @Servo7.setter
    def Servo7(self, angle):
        self._servo7.angle = angle

    @property
    def PWM0(self):
        return self._pwm0.value
    @PWM0.setter
    def PWM0(self, value):
        self._pwm0.value = value
    @property
    def PWM1(self):
        return self._pwm1.value
    @PWM1.setter
    def PWM1(self, value):
        self._pwm1.value = value
    @property
    def PWM2(self):
        return self._pwm2.value
    @PWM2.setter
    def PWM2(self, value):
        self._pwm2.value = value
    @property
    def PWM3(self):
        return self._pwm3.value
    @PWM3.setter
    def PWM3(self, value):
        self._pwm3.value = value
    @property
    def PWM4(self):
        return self._pwm4.value
    @PWM4.setter
    def PWM4(self, value):
        self._pwm4.value = value
    @property
    def PWM5(self):
        return self._pwm5.value
    @PWM5.setter
    def PWM5(self, value):
        self._pwm5.value = value
    @property
    def PWM6(self):
        return self._pwm6.value
    @PWM6.setter
    def PWM6(self, value):
        self._pwm6.value = value
    @property
    def PWM7(self):
        return self._pwm7.value
    @PWM7.setter
    def PWM7(self, value):
        self._pwm7.value = value

    @property
    def LED(self):
        return self._led.brightness
    @LED.setter
    def LED(self, value):
        self._led.brightness = value    

    @property
    def MotorA(self):
        return self._motor_a.speed
    @MotorA.setter
    def MotorA(self, value):
        self._motor_a.speed = value
    @property
    def MotorB(self):
        return self._motor_b.speed
    @MotorB.setter
    def MotorB(self, value):
        self._motor_b.speed = value

    @property
    def MotorA_reversed(self):
        return self._motor_a.is_reversed
    @MotorA_reversed.setter
    def MotorA_reversed(self, value):
        self._motor_a.is_reversed = value
    @property
    def MotorB_reversed(self):
        return self._motor_b.is_reversed
    @MotorB_reversed.setter
    def MotorB_reversed(self, value):
        self._motor_b.is_reversed = value

    @property
    def Say(self):
        return self._tts.say
    @Say.setter
    def Say(self, words):
        self._tts.say = words

    @property
    def listen(self):
        return self._stt.recognize()

    @property
    def heard(self):
        return self._stt.heard

    @property
    def result(self):
        return self._stt.result
    
    