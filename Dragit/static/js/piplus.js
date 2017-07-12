// SunFounder piplus

modules.cloud = "2017-July-05"

SpriteMorph.prototype.loadPiPlusCategories = function(blocks, block, watcherToggle){
    //blocks.push(watcherToggle('light_analog'));

    // Digital port
    blocks.push('-');
    blocks.push(block('plus_buzzer_on_off'));
    blocks.push(block('plus_buzzer_morsecode'));
    blocks.push('-');
    blocks.push(block('plus_led_ring_on'));
    blocks.push(block('plus_led_ring_pwm'));
    blocks.push(block('plus_led_ring_spin'));
    blocks.push(block('plus_led_ring_breath'));
    blocks.push(block('plus_led_ring_meter'));
    blocks.push('-');
    blocks.push(block('plus_led_bar_graph_meter'));
    blocks.push(block('plus_led_bar_graph_pulse'));
    blocks.push('-');
    blocks.push(block('plus_rgb_off'));
    blocks.push(block('plus_rgb_rgb'));
    blocks.push(block('plus_rgb_hsb'));
    blocks.push(block('plus_rgb_breath'));
    blocks.push('-');
    blocks.push(block('plus_buttons'));
    blocks.push('-');
    blocks.push(block('plus_rotaryEncoder_start'));
    blocks.push(block('plus_rotaryEncoder_rotation'));
    blocks.push(block('plus_rotaryEncoder_button'));
    blocks.push(block('plus_rotaryEncoder_end'));
    blocks.push('=');

    // Analog port
    blocks.push(block('plus_joystick'));
    blocks.push('-');
    blocks.push(block('plus_photoresistor'));
    blocks.push('-');
    blocks.push(block('plus_slide_potentiometers'));
    blocks.push('-');
    blocks.push(block('plus_sound_sensor'));
    blocks.push('=');

    // Modules with Communication Port
    blocks.push(block('plus_lcd1602_clear'));
    blocks.push(block('plus_lcd1602_print'));
    blocks.push(block('plus_motion_sensor'));
    blocks.push(block('plus_ds18b20'));
    blocks.push('=');

}

// piplus
SpriteMorph.prototype.categories.push('PiPlus')   // Add categories

SpriteMorph.prototype.blockColor.PiPlus = new Color(0, 96, 100)    // Cyan 900 rgb(0, 96, 100)

/*
type:   command
        reporter
        predicate
        hat
        ring
 */


// Digital port
//------------------------  buzzer  ------------------------------------
SpriteMorph.prototype.blocks.plus_buzzer_on_off = {
    type    : 'command',
    category: 'PiPlus',
    spec    : 'plus buzzer %piplus_port %sf_on_off',
    defaults: ['B', 'off']
  }

SpriteMorph.prototype.blocks.plus_buzzer_morsecode = {
    type    : 'command',
    category: 'PiPlus',
    spec    : 'plus buzzer %piplus_port morsecode %br   words %s  speed %piplus_morse_speed',
    defaults: ['B', 'SMS', 'fast']
  }


//-------------------------  led ring -------------------------------------
SpriteMorph.prototype.blocks.plus_led_ring_pwm = {
    type    : 'command',
    category: 'PiPlus',
    spec    : 'plus led ring %piplus_port %br %n %n %n %n %n %n %n %n',
    defaults: ['B', '0', '100', '0', '100', '0', '100', '0', '100']
  }
SpriteMorph.prototype.blocks.plus_led_ring_on = {
    type    : 'command',
    category: 'PiPlus',
    spec    : 'plus led ring %piplus_port %br       %chkbx %br    %chkbx   %chkbx %br %chkbx         %chkbx %br    %chkbx   %chkbx %br       %chkbx ',
    defaults: ['B']
  }

SpriteMorph.prototype.blocks.plus_led_ring_spin = {
    type    : 'command',
    category: 'PiPlus',
    spec    : 'plus led ring %piplus_port spin %br   style %piplus_ring_style %br   dirct %sf_cw_ccw %br   delay %n ',
    defaults: ['B', 'SINGLE', 'cw', '0.2']
  }

SpriteMorph.prototype.blocks.plus_led_ring_breath = {
    type    : 'command',
    category: 'PiPlus',
    spec    : 'plus led ring %piplus_port breath %br   delay %n ',
    defaults: ['B', '0.03']
  }

SpriteMorph.prototype.blocks.plus_led_ring_meter = {
    type    : 'command',
    category: 'PiPlus',
    spec    : 'plus led ring %piplus_port meter %br   value %n %br   brightness %n ',
    defaults: ['B', '40', '40']
  }


//------------------------  led bar graph  -----------------------------
SpriteMorph.prototype.blocks.plus_led_bar_graph_meter = {
    type    : 'command',
    category: 'PiPlus',
    spec    : 'led bar graph %piplus_port meter %br   value %n',
    defaults: ['B', '6']
  }

SpriteMorph.prototype.blocks.plus_led_bar_graph_pulse = {
    type    : 'command',
    category: 'PiPlus',
    spec    : 'led bar graph %piplus_port pulse %br   value %n',
    defaults: ['B', '6']
  }


//--------------------------  rgb  -------------------------------------
SpriteMorph.prototype.blocks.plus_rgb_off = {
    type    : 'command',
    category: 'PiPlus',
    spec    : 'plus rgb led %piplus_port off',
    defaults: ['B']
  }

SpriteMorph.prototype.blocks.plus_rgb_rgb = {
    type    : 'command',
    category: 'PiPlus',
    spec    : 'plus rgb led %piplus_port rgb %br   %n %n %n',
    defaults: ['B', '60', '60', '60']
  }

SpriteMorph.prototype.blocks.plus_rgb_hsb = {
    type    : 'command',
    category: 'PiPlus',
    spec    : 'plus rgb led %piplus_port hsb %br   %n %n %n',
    defaults: ['B', '60', '1.0', '1.0']
  }

SpriteMorph.prototype.blocks.plus_rgb_breath = {
    type    : 'command',
    category: 'PiPlus',
    spec    : 'plus rgb led %piplus_port breath %br   rgb %n %n %n %br   delay %n',
    defaults: ['B', '60', '60', '60', '0.01']
  }


//--------------------------  buttons  -------------------------------------
SpriteMorph.prototype.blocks.plus_buttons = {
    type    : 'reporter',
    category: 'PiPlus',
    spec    : 'plus buttons %piplus_port ',
    defaults: ['B']
  }

//------------------------  rotary encoder  ---------------------------
SpriteMorph.prototype.blocks.plus_rotaryEncoder_start = {
    type    : 'command',
    category: 'PiPlus',
    spec    : 'plus encoder %piplus_port rotation',
    defaults: ['B']
  }

SpriteMorph.prototype.blocks.plus_rotaryEncoder_rotation = {
    type    : 'reporter',
    category: 'PiPlus',
    spec    : 'rotary encoder rotation'
  }

SpriteMorph.prototype.blocks.plus_rotaryEncoder_button = {
    type    : 'reporter',
    category: 'PiPlus',
    spec    : 'rotary encoder button '
  }

SpriteMorph.prototype.blocks.plus_rotaryEncoder_end = {
    type    : 'command',
    category: 'PiPlus',
    spec    : 'end encoder '
  }


// Analog port
//------------------------  joystick  ---------------------------------
SpriteMorph.prototype.blocks.plus_joystick = {
    type    : 'reporter',
    category: 'PiPlus',
    spec    : 'plus joystick '
  }


//------------------------  photoresistor  -----------------------------
SpriteMorph.prototype.blocks.plus_photoresistor = {
    type    : 'reporter',
    category: 'PiPlus',
    spec    : 'plus photoresistor '
  }


//------------------------  potentiometer  -----------------------------
SpriteMorph.prototype.blocks.plus_slide_potentiometers = {
    type    : 'reporter',
    category: 'PiPlus',
    spec    : 'plus slide potentiometers %piplus_slide',
    defaults: ['sp1']
  }

//------------------------  sound sensor  ------------------------------
SpriteMorph.prototype.blocks.plus_sound_sensor = {
    type    : 'reporter',
    category: 'PiPlus',
    spec    : 'plus sound sensor ',
  }


// Modules with Communication Port
SpriteMorph.prototype.blocks.plus_lcd1602_clear = {
    type    : 'command',
    category: 'PiPlus',
    spec    : 'i2c lcd1602 clear',
  }

SpriteMorph.prototype.blocks.plus_lcd1602_print = {
    type    : 'command',
    category: 'PiPlus',
    spec    : 'plus lcd1602 print %br   r0 col %col_1602 words %s %br   r1 col %col_1602 words %s ',
    defaults: [0, 'Greetings!!', 1, 'From SunFounder']
  }

SpriteMorph.prototype.blocks.plus_motion_sensor = {
    type    : 'reporter',
    category: 'PiPlus',
    spec    : 'plus motion sensor %mpu6050_item ',
    defaults: ['acceleration x']
  }

SpriteMorph.prototype.blocks.plus_ds18b20 = {
    type    : 'reporter',
    category: 'PiPlus',
    spec    : 'plus ds18b20 %br unit %unit',
    defaults: ['c']
  }

// Relable

/*SpriteMorph.prototype.blockAlternatives.ds18b20_temper = ['dht11_module', 'mpu6050_sensor', 'bmp280_sensor'];
SpriteMorph.prototype.blockAlternatives.dht11_module = ['ds18b20_temper', 'mpu6050_sensor', 'bmp280_sensor'];
SpriteMorph.prototype.blockAlternatives.mpu6050_sensor = ['dht11_module', 'ds18b20_temper', 'bmp280_sensor'];
SpriteMorph.prototype.blockAlternatives.bmp280_sensor = ['ds18b20_temper', 'mpu6050_sensor', 'dht11_module'];
SpriteMorph.prototype.blockAlternatives.rgb_led = ['i2c_lcd_print'];*/

// Digital port
SpriteMorph.prototype.plus_buzzer_on_off = function (port, status) {
  return requests('piplus', 'plus_buzzer_on_off', port, status);
};

SpriteMorph.prototype.plus_buzzer_morsecode = function (port, morsecode, speed) {
  return requests('piplus', 'plus_buzzer_morsecode', port, morsecode, speed);
};

SpriteMorph.prototype.plus_led_ring_on = function (port, led0, led1, led2, led3, led4, led5, led6, led7) {
  if (port == 'A') {vol_pin = [17, 18, 5, 27, 25, 22, 24, 23]}
  if (port == 'B') {vol_pin = [6, 13, 21, 19, 20, 26, 16, 12]}
  vol_val = [led0, led1, led2, led3, led4, led5, led6, led7]
  for (var i = vol_val.length - 1; i >= 0; i--) {
    if (vol_val[i])
      vol_val[i] = 0
    else
      vol_val[i] = 100
  }
  console.log(vol_val)
  requests('raspberry_pi', 'volume_set_pwm', vol_pin, vol_val)
};

SpriteMorph.prototype.plus_led_ring_pwm = function (port, led0, led1, led2, led3, led4, led5, led6, led7) {
  if (port == 'A') {vol_pin = [17, 18, 27, 22, 23, 24, 25, 5]}
  if (port == 'B') {vol_pin = [6, 13, 19, 26, 12, 16, 20, 21]}
  vol_val = [100-led0, 100-led1, 100-led2, 100-led3, 100-led4, 100-led5, 100-led6, 100-led7]
  console.log(vol_val)
  requests('raspberry_pi', 'volume_set_pwm', vol_pin, vol_val)
};

SpriteMorph.prototype.plus_led_ring_spin = function (port, style, direction, delaytime) {
  return requests('piplus', 'plus_led_ring_spin', port, style, direction, delaytime);
};

SpriteMorph.prototype.plus_led_ring_breath = function (port, delaytime) {
  return requests('piplus', 'plus_led_ring_breath', port, delaytime);
};

SpriteMorph.prototype.plus_led_ring_meter = function (port, value, brightness) {
  return requests('piplus', 'plus_led_ring_meter', port, value, brightness);
};

SpriteMorph.prototype.plus_led_bar_graph_meter = function (port, value) {
  return requests('piplus', 'plus_led_bar_graph_meter', port, value)
};

SpriteMorph.prototype.plus_led_bar_graph_pulse = function (port, value) {
  return requests('piplus', 'plus_led_bar_graph_pulse', port, value)
};

SpriteMorph.prototype.plus_rgb_off = function (port) {
  if (port == 'A') {
    r_pin = 23;
    g_pin = 24;
    b_pin = 25;
  }
  if (port == 'B') {
    r_pin = 12;
    g_pin = 16;
    b_pin = 20;
  }
  requests('raspberry_pi', 'stop_pwm', r_pin);
  requests('raspberry_pi', 'stop_pwm', g_pin);
  requests('raspberry_pi', 'stop_pwm', b_pin);
};

SpriteMorph.prototype.plus_rgb_rgb = function (port, r, g, b) {
  if (port == 'A') {
    r_pin = 23
    g_pin = 24
    b_pin = 25
  }
  if (port == 'B') {
    r_pin = 12
    g_pin = 16
    b_pin = 20
  }
  R_val = r * 100 /255;
  G_val = g * 100 /255;
  B_val = b * 100 /255;
  var vol_pin = ""  // vol_pin = 'pin1,pin2,pin3'
  var vol_val = ""  // vol_val = 'val1,val2,val3'
  vol_pin = r_pin + "," + g_pin + "," + b_pin
  vol_val = R_val + "," + G_val + "," + B_val
  requests('raspberry_pi', 'volume_set_pwm', vol_pin, vol_val)
  console.log(vol_pin, vol_val)
};

SpriteMorph.prototype.plus_rgb_hsb = function (port, h, s, b) {
  if (port == 'A') {
    r_pin = 23
    g_pin = 24
    b_pin = 25
  }
  if (port == 'B') {
    r_pin = 12
    g_pin = 16
    b_pin = 20
  }

  if (h > 360) { h = h%360}
  else if (h < 0) {h = 0}
  if (s > 1)    {s = 1}
  else if (s < 0) {s = 0}
  if (b > 1)    {b = 1}
  else if (b < 0) {b = 0}

  _hi = (h/60)%6
  _f = h / 60.0 - _hi
  _p = b * (1 - s)
  _q = b * (1 - _f * s)
  _t = b * (1 - (1 - _f) * s)

  console.log(_hi, _f, _p, _q, _t)

  if (_hi == 0) {
    _R_val = b
    _G_val = _t
    _B_val = _p
  }
  if (_hi == 1) {
    _R_val = _q
    _G_val = b
    _B_val = _p
  }
  if (_hi == 2) {
    _R_val = _p
    _G_val = b
    _B_val = _t
  }
  if (_hi == 3) {
    _R_val = _p
    _G_val = _q
    _B_val = b
  }
  if (_hi == 4) {
    _R_val = _t
    _G_val = _p
    _B_val = b
  }
  if (_hi == 5) {
    _R_val = b
    _G_val = _p
    _B_val = _q
  }

  var vol_pin = ""  // vol_pin = 'pin1,pin2,pin3'
  var vol_val = ""  // vol_val = 'val1,val2,val3'
  vol_pin = r_pin + "," + g_pin + "," + b_pin
  vol_val = _R_val*255.0 + "," + _G_val*255.0 + "," + _B_val*255.0
  console.log(vol_val)
  requests('raspberry_pi', 'volume_set_pwm', vol_pin, vol_val)
};

SpriteMorph.prototype.plus_rgb_breath = function (port, r, g, b, dt) {
  return requests('piplus', 'plus_rgb_breath', port, r, g, b, dt)
};

SpriteMorph.prototype.plus_buttons = function (port) {
  if (port == 'A') {
    c1 = 17;
    c2 = 18;
    c3 = 27;
    c4 = 22;
  }
  if (port == 'B') {
    c1 = 6;
    c2 = 13;
    c3 = 19;
    c4 = 26;
  }
  // pull up input value:
  requests('raspberry_pi', 'gpio', 'output', c1, 'HIGH')
  requests('raspberry_pi', 'gpio', 'output', c2, 'HIGH')
  requests('raspberry_pi', 'gpio', 'output', c3, 'HIGH')
  requests('raspberry_pi', 'gpio', 'output', c4, 'HIGH')
  result = 'None'
  if (requests('raspberry_pi', 'gpio', 'input', c1) == 0)
    result = "up"
  if (requests('raspberry_pi', 'gpio', 'input', c2) == 0)
    result = "left"
  if (requests('raspberry_pi', 'gpio', 'input', c3) == 0)
    result = "down"
  if (requests('raspberry_pi', 'gpio', 'input', c4) == 0)
    result = "right"
  return result
};

SpriteMorph.prototype.plus_rotaryEncoder_start = function (port) {
  if (port == 'A') {
    A_PIN  = 17
    B_PIN  = 18
    SW     = 27
  }
  if (port == 'B') {
    A_PIN  = 6
    B_PIN  = 13
    SW     = 19
  }
  requests('modules', 'encoder_start', A_PIN, B_PIN, SW)
};

SpriteMorph.prototype.plus_rotaryEncoder_rotation = function () {
  return requests('modules', 'encoder_rotation')
};

SpriteMorph.prototype.plus_rotaryEncoder_button = function () {
  return requests('modules', 'encoder_button')
};

SpriteMorph.prototype.plus_rotaryEncoder_end = function () {
  return requests('modules', 'encoder_end')
};


// Analog port
SpriteMorph.prototype.plus_joystick = function () {
  return requests('piplus', 'plus_joystick' )
};

SpriteMorph.prototype.plus_photoresistor = function () {
  return requests('piplus', 'plus_photoresistor')
};

SpriteMorph.prototype.plus_slide_potentiometers = function (item) {
  return requests('piplus', 'plus_slide_potentiometers', item)
};

SpriteMorph.prototype.plus_sound_sensor = function () {
  return requests('piplus', 'plus_sound_sensor')
};

// Modules with Communication Port
SpriteMorph.prototype.plus_lcd1602_print = function (col1, words1, col2, word2) {
  return requests('piplus', 'plus_lcd1602_print', col1, words1, col2, word2)
};

SpriteMorph.prototype.plus_lcd1602_clear = function () {
  return requests('piplus', 'plus_lcd1602_clear')
};

SpriteMorph.prototype.plus_motion_sensor = function (item) {
  return requests('piplus', 'plus_motion_sensor', item)
};

SpriteMorph.prototype.plus_ds18b20 = function (unit) {
  return requests('piplus', 'plus_ds18b20', unit)
};