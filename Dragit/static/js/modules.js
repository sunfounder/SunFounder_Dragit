// SunFounder modules

modules.cloud = "2017-May-05"

SpriteMorph.prototype.loadModulesCategories = function(blocks, block, watcherToggle){
    //blocks.push(watcherToggle('light_analog'));
    blocks.push(block('light_analog'));
    blocks.push(block('light_analog_index'));
    blocks.push('-');
    //blocks.push(watcherToggle('line_analog'));
    blocks.push(block('line_analog'));
    blocks.push(block('line_analog_index'));
    blocks.push('-');
    blocks.push(block('ultrasonic_3pin'));
    blocks.push(block('ultrasonic_4pin'));
    blocks.push('-');
    blocks.push(block('temperature_sensor'));
    blocks.push(block('ds18b20_temper'));
    blocks.push(block('bmp280_sensor'));
    blocks.push(block('dht11_module'));
    blocks.push(block('mpu6050_sensor'));

    blocks.push('=');
    blocks.push(block('pcf8591_module'));
    blocks.push(block('pcf8591_output'));

    blocks.push('=');
    blocks.push(block('is_IR_received'));
    blocks.push(block('IR_received_val'));
    blocks.push(block('IR_key_list'));

    blocks.push('-');
    blocks.push(block('passive_buzzer_module'));
    blocks.push(block('passive_buzzer_play_note'));
    blocks.push('=');

    blocks.push(block('rgb_led'));
    blocks.push(block('i2c_lcd_clear'));
    blocks.push(block('i2c_lcd_print'));
    //blocks.push(block('led_matrix'));
    //blocks.push(block('led_matrix_mod'));
    blocks.push('-');
    blocks.push(block('rtc_ds1302_set'));
    blocks.push(block('rtc_ds1302_get'));

    //blocks.push(block('dual_color_led'));
/*  // Input module
    // digital input modules
    blocks.push('=');
    blocks.push(block('button_module'));
    blocks.push(block('tilt_switch'));
    blocks.push(block('reed_switch'));
    blocks.push(block('touch_switch'));
    blocks.push(block('mercury_switch'));
    blocks.push(block('vibration_switch'));
    blocks.push(block('photo_interrupter'));
    blocks.push(block('hall_sensor'));
    blocks.push(block('ir_obstacle_avoidance_module'));
    blocks.push(block('ir_receiver_module'));
 */

/*  // Output module
    // digital output modules
    blocks.push('=');
    blocks.push(block('relay_module'));
    blocks.push(block('color_auto_flash_led'));
    blocks.push(block('laser_emitter_module'));
    blocks.push(block('active_buzzer_module'));
 */
/*  // Input modules
    // analog input (convert to digital)
    blocks.push('=');
    blocks.push(block('analog_hall_switch'));
    blocks.push(block('tracking_sensor'));
    blocks.push(block('potentiometer_module'));
    blocks.push(block('photoresistor_module'));
    blocks.push(block('rain_detection'));
    blocks.push(block('sound_sensor'));
    blocks.push(block('flame_sensor'));
    blocks.push(block('gas_sensor'));
    //blocks.push(block('set_joystick_ps2'));
    blocks.push(block('joystick_ps2'));
 */
/*
    // Output module

    // pwm output ()

    // BUS modul

    // difficult
    blocks.push(block('rotary_encoder_module'));
 */
}

// modules
SpriteMorph.prototype.categories.push('Modules')   // Add categories

SpriteMorph.prototype.blockColor.Modules = new Color(96, 125, 159)    // Blue Gray 700 rgb(96, 125, 199)

/*
type:   command
        reporter
        predicate
        hat
        ring
 */

SpriteMorph.prototype.blocks.ultrasonic_3pin = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'ultrasonic distance %br   sig %rpi_bcm_chn',
    defaults: ['17']
  }

SpriteMorph.prototype.blocks.ultrasonic_4pin = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'ultrasonic distance %br   trig %rpi_bcm_chn echo %rpi_bcm_chn',
    defaults: ['17', '18']
  }

SpriteMorph.prototype.blocks.light_analog_index = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'light follower state %lt_index_chn',
    defaults: ["0"]
  }

SpriteMorph.prototype.blocks.light_analog = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'light follower state'
  }

SpriteMorph.prototype.blocks.line_analog_index = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'line follower state %lf_index_chn',
    defaults: [1]
  }

SpriteMorph.prototype.blocks.line_analog = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'line follower state'
  }

// digital input modules
SpriteMorph.prototype.blocks.button_module = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'button %rpi_bcm_chn state',
    defaults: ['17']
  }

SpriteMorph.prototype.blocks.touch_switch = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'touch switch %rpi_bcm_chn  state',
    defaults: ['17']
  }

SpriteMorph.prototype.blocks.tilt_switch = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'tilt switch %rpi_bcm_chn state',
    defaults: ['17']
  }

SpriteMorph.prototype.blocks.vibration_switch = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'vibration switch %rpi_bcm_chn state',
    defaults: ['17']
  }

SpriteMorph.prototype.blocks.mercury_switch = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'mercury switch %rpi_bcm_chn state',
    defaults: ['17']
  }

SpriteMorph.prototype.blocks.reed_switch = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'reed switch %rpi_bcm_chn state',
    defaults: ['17']
  }

SpriteMorph.prototype.blocks.photo_interrupter = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'photo interrupter %rpi_bcm_chn state',
    defaults: ['17']
  }

SpriteMorph.prototype.blocks.hall_sensor = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'hall sensor %rpi_bcm_chn state',
    defaults: ['17']
  }

SpriteMorph.prototype.blocks.ir_obstacle_avoidance_module = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'ir avoidance %rpi_bcm_chn state',
    defaults: ['17']
  }

SpriteMorph.prototype.blocks.ir_receiver_module = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'ir receiver %rpi_bcm_chn state',
    defaults: ['17']
  }

// digital output modules
SpriteMorph.prototype.blocks.relay_module = {
    type    : 'command',
    category: 'Modules',
    spec    : 'relay %rpi_bcm_chn %sf_on_off',
    defaults: ['17', 'on']
  }

SpriteMorph.prototype.blocks.laser_emitter_module = {
    type    : 'command',
    category: 'Modules',
    spec    : 'laser emitter %rpi_bcm_chn %sf_on_off',
    defaults: ['17', 'on']
  }

SpriteMorph.prototype.blocks.active_buzzer_module = {
    type    : 'command',
    category: 'Modules',
    spec    : 'active buzzer %rpi_bcm_chn %sf_on_off',
    defaults: ['17', 'on']
  }

SpriteMorph.prototype.blocks.passive_buzzer_module = {
    type    : 'command',
    category: 'Modules',
    spec    : 'passive buzzer %rpi_bcm_chn %sf_on_off %br   frequency %n',
    defaults: ['12', 'off', 131]
  }

SpriteMorph.prototype.blocks.passive_buzzer_play_note = {
    type    : 'command',
    category: 'Modules',
    spec    : 'passive buzzer %rpi_bcm_chn %br    play %buzzer_note %n second',
    defaults: ['12', 'C', '0.25']
  }

// PCF9685
SpriteMorph.prototype.blocks.pcf8591_module = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'adc pcf8591 %br  addr: %pcf8591_addr %br  chn: %pcf8591_ain',
    defaults: ['0x48', 'AIN0']
  }

SpriteMorph.prototype.blocks.pcf8591_output = {
    type    : 'command',
    category: 'Modules',
    spec    : 'adc pcf8591 %br  addr: %pcf8591_addr %br  output: %n',
    defaults: ['0x48', '0']
  }

// analog input modules
SpriteMorph.prototype.blocks.analog_hall_switch = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'analog hall switch %s',
    //defaults: ['pcf8591_mod']
  }

SpriteMorph.prototype.blocks.temperature_sensor = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'thermistor %s',
    defaults: ['adc block']
  }

SpriteMorph.prototype.blocks.tracking_sensor = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'tracking sensor %s',
    //defaults: ['pcf8591_mod']
  }

SpriteMorph.prototype.blocks.potentiometer_module = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'potentiometer %s',
    //defaults: ['pcf8591_mod']
  }

SpriteMorph.prototype.blocks.photoresistor_module = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'photoresistor %s',
    //defaults: ['pcf8591_mod']
  }

SpriteMorph.prototype.blocks.rain_detection = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'rain detection %s',
    //defaults: ['pcf8591_mod']
  }

SpriteMorph.prototype.blocks.sound_sensor = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'sound sensor %s',
    //defaults: ['pcf8591_mod']
  }

SpriteMorph.prototype.blocks.flame_sensor = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'flame sensor %s',
    //defaults: ['pcf8591_mod']
  }

SpriteMorph.prototype.blocks.gas_sensor = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'gas sensor %s',
    //defaults: ['pcf8591_mod']
  }

/*SpriteMorph.prototype.blocks.set_joystick_ps2 = {
    type    : 'command',
    category: 'Modules',
    spec    : 'set joystick to pcf9685_addr: %pcf8591_addr %br X:%pcf8591_ain Y:pcf8591_ain Bt:pcf8591_ain',
    defaults: ['0x48', 'AIN0','AIN1','AIN2']
  }*/

SpriteMorph.prototype.blocks.joystick_ps2 = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'joystick ps2 %s',
    //defaults: ['pcf8591_mod']
  }

SpriteMorph.prototype.blocks.color_auto_flash_led = {
    type    : 'command',
    category: 'Modules',
    spec    : 'auto flash led %rpi_bcm_chn %sf_on_off',
    defaults: [17, 'on']
  }

SpriteMorph.prototype.blocks.rgb_led = {
    type    : 'command',
    category: 'Modules',
    spec    : 'rgb led %br   R pin: %rpi_bcm_chn %br   G pin: %rpi_bcm_chn %br   B pin: %rpi_bcm_chn %br   com: %common_polarity %br   color: %clr ',
    defaults: [16, 20, 21, 'cathode']
  }

SpriteMorph.prototype.blocks.dual_color_led = {
    type    : 'command',
    category: 'Modules',
    spec    : 'dual color led %br   R pin: %rpi_bcm_chn %br   G pin: %rpi_bcm_chn %br   reverse: %sf_0_1 %br   color: %DUALcolors ',
    defaults: [17, 18, '0', 'green']
  }

SpriteMorph.prototype.blocks.ds18b20_temper = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'ds18b20 ordinal %n %br unit %unit',
    defaults: [0, 'c']
  }

SpriteMorph.prototype.blocks.i2c_lcd_clear = {
    type    : 'command',
    category: 'Modules',
    spec    : 'i2c lcd1602 clear',
  }

SpriteMorph.prototype.blocks.i2c_lcd_print = {
    type    : 'command',
    category: 'Modules',
    spec    : 'i2c lcd1602 print %br   row %row_1602 col %col_1602 %br   words %s',
    defaults: [0, 0, 'Hello,World!']
  }

SpriteMorph.prototype.blocks.dht11_module = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'dht11 %rpi_bcm_chn %dht_mode',
    defaults: [17, 'temperature C']
  }

SpriteMorph.prototype.blocks.bmp280_sensor = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'bmp280 %bmp280_item',
    defaults: ['pressure']
  }

SpriteMorph.prototype.blocks.mpu6050_sensor = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'mpu6050 %mpu6050_item ',
    defaults: ['acceleration x']
  }

SpriteMorph.prototype.blocks.rtc_ds1302_get = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'rtc ds1302 %rtc_ds1302_item ',
    defaults: ['year']
  }

SpriteMorph.prototype.blocks.rtc_ds1302_set = {
    type    : 'command',
    category: 'Modules',
    spec    : 'set rtc ds1302 %br   year: %n %br   mon: %n %br   day: %n %br   hour: %n %br   min: %n %br   sec: %n',
    defaults: [current_datetime.year, current_datetime.mon, current_datetime.day, current_datetime.hour, current_datetime.min, current_datetime.sec]
  }

SpriteMorph.prototype.blocks.is_IR_received = {
    type    : 'predicate',
    category: 'Modules',
    spec    : 'ir received?',
  }

SpriteMorph.prototype.blocks.IR_received_val = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'ir received value',
  }

SpriteMorph.prototype.blocks.IR_key_list = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'remote %remoteKey',
    defaults: '0'
  }

SpriteMorph.prototype.blocks.led_matrix = {
    type    : 'command',
    category: 'Modules',
    spec    : 'led matrix set'
  }

SpriteMorph.prototype.blocks.led_matrix_mod = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'led matrix %br   %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %br   %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %br   %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %br   %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %br   %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %br   %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %br   %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %br   %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx %chkbx'
  }
/*
SpriteMorph.prototype.blocks.ir_receiver_module = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'ir receiver on %rpi_bcm_chn state',
    defaults: ['17']
  }

*/
// Relable
SpriteMorph.prototype.blockAlternatives.light_analog_index = ['light_analog'];
SpriteMorph.prototype.blockAlternatives.light_analog = ['light_analog_index'];
SpriteMorph.prototype.blockAlternatives.line_analog_index = ['line_analog'];
SpriteMorph.prototype.blockAlternatives.line_analog = ['line_analog_index'];
SpriteMorph.prototype.blockAlternatives.ultrasonic_3pin = ['ultrasonic_4pin'];
SpriteMorph.prototype.blockAlternatives.ultrasonic_4pin = ['ultrasonic_3pin'];
SpriteMorph.prototype.blockAlternatives.passive_buzzer_module = ['passive_buzzer_play_note'];
SpriteMorph.prototype.blockAlternatives.passive_buzzer_play_note = ['passive_buzzer_module'];
SpriteMorph.prototype.blockAlternatives.rtc_ds1302_set = ['rtc_ds1302_get'];
SpriteMorph.prototype.blockAlternatives.rtc_ds1302_get = ['rtc_ds1302_set'];
SpriteMorph.prototype.blockAlternatives.i2c_lcd_print = ['i2c_lcd_clear'];
SpriteMorph.prototype.blockAlternatives.i2c_lcd_clear = ['i2c_lcd_print'];
/*SpriteMorph.prototype.blockAlternatives.ds18b20_temper = ['dht11_module', 'mpu6050_sensor', 'bmp280_sensor'];
SpriteMorph.prototype.blockAlternatives.dht11_module = ['ds18b20_temper', 'mpu6050_sensor', 'bmp280_sensor'];
SpriteMorph.prototype.blockAlternatives.mpu6050_sensor = ['dht11_module', 'ds18b20_temper', 'bmp280_sensor'];
SpriteMorph.prototype.blockAlternatives.bmp280_sensor = ['ds18b20_temper', 'mpu6050_sensor', 'dht11_module'];
SpriteMorph.prototype.blockAlternatives.rgb_led = ['i2c_lcd_print'];*/

// SunFounder process
SpriteMorph.prototype.ultrasonic_3pin = function (channel) {
  return requests('modules', 'ultrasonic_3pin', channel)
};

SpriteMorph.prototype.light_analog_index = function (channel) {
  return requests('modules', 'light_follower_analog', channel)
};

SpriteMorph.prototype.light_analog = function () {
  var result = new List()
  raw_result = requests('modules', 'light_follower_analog').split(',');
  for (i=0; i<raw_result.length; i++){
    result.add(raw_result[i])
  }
  return result
};

SpriteMorph.prototype.line_analog_index = function (channel) {
  return requests('modules', 'line_follower_analog', channel)
};

SpriteMorph.prototype.line_analog = function () {
  var result = new List()
  raw_result = requests('modules', 'line_follower_analog').split(',');
  for (i=0; i<raw_result.length; i++){
    result.add(raw_result[i])
  }
  return result
};

// digital input sensors
SpriteMorph.prototype.button_module = function (chn) {
  return requests('raspberry_pi', 'gpio', 'input', chn)
};

SpriteMorph.prototype.touch_switch = function (chn) {
  return requests('raspberry_pi', 'gpio', 'input', chn)
};

SpriteMorph.prototype.tilt_switch = function (chn) {
  return requests('raspberry_pi', 'gpio', 'input', chn)
};

SpriteMorph.prototype.vibration_switch = function (chn) {
  return requests('raspberry_pi', 'gpio', 'input', chn)
};

SpriteMorph.prototype.mercury_switch = function (chn) {
  return requests('raspberry_pi', 'gpio', 'input', chn)
};

SpriteMorph.prototype.reed_switch = function (chn) {
  return requests('raspberry_pi', 'gpio', 'input', chn)
};

SpriteMorph.prototype.photo_interrupter = function (chn) {
  return requests('raspberry_pi', 'gpio', 'input', chn)
};

SpriteMorph.prototype.hall_sensor = function (chn) {
  return requests('raspberry_pi', 'gpio', 'input', chn)
};

SpriteMorph.prototype.ir_obstacle_avoidance_module = function (chn) {
  return requests('raspberry_pi', 'gpio', 'input', chn)
};

SpriteMorph.prototype.ir_receiver_module = function (chn) {
  return requests('raspberry_pi', 'gpio', 'input', chn)
};

// digital output sensors
SpriteMorph.prototype.relay_module = function (chn, state) {
  if (state == "on")
    state = 'LOW';
  else
    state = 'HIGH';
  requests('raspberry_pi', 'gpio', 'output', chn, state)
};

SpriteMorph.prototype.laser_emitter_module = function (chn, state) {
  if (state == "on")
    state = 'LOW';
  else
    state = 'HIGH';
  requests('raspberry_pi', 'gpio', 'output', chn, state)
};

SpriteMorph.prototype.active_buzzer_module = function (chn, state) {
  if (state == "on")
    state = 'LOW';
  else
    state = 'HIGH';
  requests('raspberry_pi', 'gpio', 'output', chn, state)
};

SpriteMorph.prototype.color_auto_flash_led = function (chn, state) {
  if (state == "on")
    state = 'LOW';
  else
    state = 'HIGH';
  requests('raspberry_pi', 'gpio', 'output', chn, state)
};

SpriteMorph.prototype.passive_buzzer_module = function (chn, on_off, frequency) {
  requests('modules', 'passive_buzzer', chn, frequency, on_off)
};

SpriteMorph.prototype.passive_buzzer_play_note = function (chn, note, second) {
  requests('modules', 'buzzer_play', chn, note, second)
};

// pcf8591 module
SpriteMorph.prototype.pcf8591_module = function (addr, chn) {
  if (chn == 'AIN0')      {chn = 0;}
  else if (chn == 'AIN1') {chn = 1;}
  else if (chn == 'AIN2') {chn = 2;}
  else if (chn == 'AIN3') {chn = 3;}
  return requests('modules', 'pcf8591', addr, chn)
};

SpriteMorph.prototype.pcf8591_output = function (addr, value) {
  if (value > 255)    {value = 255;}
  else if (value < 0) {value = 0;}
  return requests('modules', 'pcf8591_write', addr, value)
};

SpriteMorph.prototype.ultrasonic_4pin = function (t_pin, e_pin) {
  return requests('modules', 'ultrasonic_4pin', t_pin, e_pin)
};

// analog input sensors
SpriteMorph.prototype.analog_hall_switch = function (pcf8591_module) {
  return pcf8591_module
};

SpriteMorph.prototype.temperature_sensor = function (pcf8591_module) {
  return requests('modules', 'thermitor', pcf8591_module)
};

SpriteMorph.prototype.tracking_sensor = function (pcf8591_module) {
  return pcf8591_module
};

SpriteMorph.prototype.potentiometer_module = function (pcf8591_module) {
  return pcf8591_module
};

SpriteMorph.prototype.photoresistor_module = function (pcf8591_module) {
  return pcf8591_module
};

SpriteMorph.prototype.rain_detection = function (pcf8591_module) {
  return pcf8591_module
};

SpriteMorph.prototype.sound_sensor = function (pcf8591_module) {
  return pcf8591_module
};

SpriteMorph.prototype.flame_sensor = function (pcf8591_module) {
  return pcf8591_module
};

SpriteMorph.prototype.gas_sensor = function (pcf8591_module) {
  return pcf8591_module
};

/*SpriteMorph.prototype.set_joystick_ps2 = function (addr, x_pin, y_pin, z_pin) {
  var ps2_addr = int(addr)
  var ps2_pin  = new List()
  List.add(x_pin)
  List.add(y_pin)
  List.add(z_pin)
};*/

SpriteMorph.prototype.joystick_ps2 = function (pcf8591_module) {
  return pcf8591_module
};

SpriteMorph.prototype.rgb_led = function (r_pin, g_pin, b_pin, com_pol, rgb) {
  console.log(rgb);
  R_val = rgb.r * 100 /255;
  G_val = rgb.g * 100 /255;
  B_val = rgb.b * 100 /255;
  if (com_pol == "cathode")
  {
    R_val = 100 - R_val;
    G_val = 100 - G_val;
    B_val = 100 - B_val;
  }
  console.log(R_val, G_val, B_val)

  var vol_pin = ""  // vol_pin = 'pin1,pin2,pin3'
  var vol_val = ""  // vol_val = 'val1,val2,val3'
  vol_pin = r_pin + "," + g_pin + "," + b_pin
  vol_val = R_val + "," + G_val + "," + B_val
  requests('raspberry_pi', 'volume_set_pwm', vol_pin, vol_val)
  console.log(vol_pin, vol_val)
  //return rgb
};

SpriteMorph.prototype.dual_color_led = function (r_pin, g_pin, com_pol, color) {
  requests('modules', 'dual_color_led', r_pin, g_pin, com_pol, color)
};

SpriteMorph.prototype.ds18b20_temper = function (index, unit) {
  return requests('modules', 'w1', index, unit)
};

SpriteMorph.prototype.i2c_lcd_clear = function () {
  return requests('modules', 'i2c_lcd_clear')
};

SpriteMorph.prototype.i2c_lcd_print = function (pos_col, pos_row, words) {
  return requests('modules', 'i2c_lcd_print', pos_col, pos_row, words)
};

SpriteMorph.prototype.led_matrix = function (pos_col, pos_row, words) {
  return requests('modules', 'led_matrix', pos_col, pos_row, words)
};

SpriteMorph.prototype.led_matrix_mod = function (box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,box17,box18,box19,box20,box21,box22,box23,box24,box25,box26,box27,box28,box29,box30,box31,box32,box33,box34,box35,box36,box37,box38,box39,box40,box41,box42,box43,box44,box45,box46,box47,box48,box49,box50,box51,box52,box53,box54,box55,box56,box57,box58,box59,box60,box61,box62,box63,box64,box65,box66,box67,box68,box69,box70,box71,box72,box73,box74,box75,box76,box77,box78,box79,box80,box81,box82,box83,box84,box85,box86,box87,box88,box89,box90,box91,box92,box93,box94,box95,box96,box97,box98,box99,box100,box101,box102,box103,box104,box105,box106,box107,box108,box109,box110,box111,box112,box113,box114,box115,box116,box117,box118,box119,box120,box121,box122,box123,box124,box125,box126,box127,box128,box129,box130,box131,box132,box133,box134,box135,box136,box137,box138,box139,box140,box141,box142,box143,box144,box145,box146,box147,box148,box149,box150,box151,box152,box153,box154,box155,box156,box157,box158,box159,box160,box161,box162,box163,box164,box165,box166,box167,box168,box169,box170,box171,box172,box173,box174,box175,box176,box177,box178,box179,box180,box181,box182,box183,box184,box185,box186,box187,box188,box189,box190,box191,box192) {
  temp_map = [box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11,box12,box13,box14,box15,box16,box17,box18,box19,box20,box21,box22,box23,box24,box25,box26,box27,box28,box29,box30,box31,box32,box33,box34,box35,box36,box37,box38,box39,box40,box41,box42,box43,box44,box45,box46,box47,box48,box49,box50,box51,box52,box53,box54,box55,box56,box57,box58,box59,box60,box61,box62,box63,box64,box65,box66,box67,box68,box69,box70,box71,box72,box73,box74,box75,box76,box77,box78,box79,box80,box81,box82,box83,box84,box85,box86,box87,box88,box89,box90,box91,box92,box93,box94,box95,box96,box97,box98,box99,box100,box101,box102,box103,box104,box105,box106,box107,box108,box109,box110,box111,box112,box113,box114,box115,box116,box117,box118,box119,box120,box121,box122,box123,box124,box125,box126,box127,box128,box129,box130,box131,box132,box133,box134,box135,box136,box137,box138,box139,box140,box141,box142,box143,box144,box145,box146,box147,box148,box149,box150,box151,box152,box153,box154,box155,box156,box157,box158,box159,box160,box161,box162,box163,box164,box165,box166,box167,box168,box169,box170,box171,box172,box173,box174,box175,box176,box177,box178,box179,box180,box181,box182,box183,box184,box185,box186,box187,box188,box189,box190,box191,box192];
  byte_list = []
  for (i=0;i<24;i++){
    byte = 0x00
    for (j=0;j<8;j++){
      tmp = temp_map[i*8+j] ? 1 : 0;
      byte = (byte << 1) + tmp;
    }
    byte_list.push(byte)
    console.log("return byte",byte)
  }
  console.log("return byte_list",byte_list)
  return byte_list
};

SpriteMorph.prototype.dht11_module = function (pin, mode) {
  return requests('modules', 'dht11_module', pin, mode)
};

SpriteMorph.prototype.bmp280_sensor = function (item) {
  return requests('modules', 'bmp280_sensor', item)
};

SpriteMorph.prototype.mpu6050_sensor = function (item) {
  return requests('modules', 'mpu6050_sensor', item)
};

SpriteMorph.prototype.rtc_ds1302_get = function (item) {
  return requests('modules', 'rtc_ds1302_get', item)
};

SpriteMorph.prototype.rtc_ds1302_set = function (year,month,day,hour,minute,second) {
  var date = new Array()
  date.push(year,month,day)
  var time = new Array()
  time.push(hour,minute,second)
  return requests('modules', 'rtc_ds1302_set', date, time)
};

SpriteMorph.prototype.is_IR_received = function () {
  result = requests('modules', 'is_IR_received');
  if (result == 1)
    result = true;
  else if (result == 0)
    result = false;
  return result
};

SpriteMorph.prototype.IR_received_val = function () {
  result = requests('modules', 'IR_received_val');
  return result
};

SpriteMorph.prototype.IR_key_list = function (key) {
  return key
};


