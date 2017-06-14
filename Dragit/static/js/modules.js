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
    blocks.push(block('ds18b20_temper'));
    blocks.push(block('bmp280_sensor'));
    blocks.push(block('dht11_module'));
    blocks.push(block('mpu6050_sensor'));

    blocks.push('=');
    blocks.push(block('pcf8591_module'));

    blocks.push('=');
    blocks.push(block('ir_codes'));
    blocks.push('-');
    blocks.push(block('passive_buzzer_module'));
    blocks.push('=');

    blocks.push(block('rgb_led'));
    blocks.push(block('i2c_lcd_print'));
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
    blocks.push(block('temperature_sensor'));
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

SpriteMorph.prototype.blocks.ir_codes = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'ir receiver code'
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
    defaults: ['17', 'off', 131]
  }

// PCF9685
SpriteMorph.prototype.blocks.pcf8591_module = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'adc pcf8591 %br  addr: %pcf8591_addr %br  chn: %pcf8591_ain',
    defaults: ['0x48', 'AIN0']
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
    spec    : 'temperature sensor %s',
    //defaults: ['pcf8591_mod']
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
    defaults: [17, 18, 27, 'anode']
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
    spec    : 'ds18b20 %n %br unit %unit',
    defaults: [0, 'c']
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
    defaults: [2017, 06, 09, 09, 15, 00]
  }

SpriteMorph.prototype.blocks.ir_codes = {
    type    : 'predicate',
    category: 'Modules',
    spec    : 'key %remoteKey pressed ?',
    defaults: ['0']
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

// SunFounder process
SpriteMorph.prototype.ultrasonic_3pin = function (channel) {
  //reportURL('192.168.0.102:8000/run/modules/?action=set_digital&value=' + value)
  return requests('modules', 'ultra_distance', channel)
};

SpriteMorph.prototype.light_analog_index = function (channel) {
  //reportURL('192.168.0.102:8000/run/modules/?action=get_analog&value=' + value)
  return requests('modules', 'light_follower_analog', channel)
};

SpriteMorph.prototype.light_analog = function () {
  //reportURL('192.168.0.102:8000/run/modules/?action=get_analog&value=' + value)
  var result = new List()
  raw_result = requests('modules', 'light_follower_analog').split(',');
  for (i=0; i<raw_result.length; i++){
    result.add(raw_result[i])
  }
  return result
};

SpriteMorph.prototype.line_analog_index = function (channel) {
  //reportURL('192.168.0.102:8000/run/modules/?action=get_analog&value=' + value)
  return requests('modules', 'line_follower_analog', channel)
};

SpriteMorph.prototype.line_analog = function () {
  //reportURL('192.168.0.102:8000/run/modules/?action=get_analog&value=' + value)
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


// pcf8591 module
SpriteMorph.prototype.pcf8591_module = function (addr, chn) {
  if (chn == 'AIN0')      {chn = 0;}
  else if (chn == 'AIN1') {chn = 1;}
  else if (chn == 'AIN2') {chn = 2;}
  else if (chn == 'AIN3') {chn = 3;}
  return requests('modules', 'pcf8591', addr, chn)
};

SpriteMorph.prototype.ultrasonic_4pin = function (t_pin, e_pin) {
  return requests('modules', 'ultrasonic_4pin', t_pin, e_pin)
};

// analog input sensors
SpriteMorph.prototype.analog_hall_switch = function (pcf8591_module) {
  return pcf8591_module
};

SpriteMorph.prototype.temperature_sensor = function (pcf8591_module) {
  return pcf8591_module
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
  requests('modules', 'rgb_led', r_pin, g_pin, b_pin, com_pol, rgb)
  //return rgb
};

SpriteMorph.prototype.dual_color_led = function (r_pin, g_pin, com_pol, color) {
  requests('modules', 'dual_color_led', r_pin, g_pin, com_pol, color)
};

SpriteMorph.prototype.ds18b20_temper = function (index, unit) {
  return requests('modules', 'w1', index, unit)
};

SpriteMorph.prototype.i2c_lcd_print = function (pos_col, pos_row, words) {
  return requests('modules', 'i2c_lcd', pos_col, pos_row, words)
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

SpriteMorph.prototype.ir_codes = function (key) {
  result = requests('modules', 'ir_codes');
  if (result == key)
    result = true;
  else
    result = false;
  return result
};


