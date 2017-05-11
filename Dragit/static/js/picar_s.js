// SunFounder PiCar-S

modules.cloud = "2017-May-05"

SpriteMorph.prototype.loadPiCarSCategories = function(blocks, block, watcherToggle){
    blocks.push(block('picar_s_rw_run'));
    blocks.push(block('picar_s_rw_stop'));
    blocks.push(block('picar_s_fw_turn'));
    //blocks.push(block('picar_s_pan_turn'));
    //blocks.push(block('picar_s_tilt_turn'));
    blocks.push('=');
    blocks.push(block('picar_s_servo_turn'));
    blocks.push(block('picar_s_pwm_output'));
    //blocks.push(watcherToggle('picar_s_get_analog'));
    blocks.push(block('picar_s_set_digital'));
    //blocks.push(watcherToggle('picar_s_get_digital'));
    blocks.push(block('picar_s_get_digital'));
    //blocks.push(watcherToggle('picar_s_get_analog'));
    blocks.push(block('picar_s_get_analog'));
    blocks.push('=');
    blocks.push(block('picar_s_cali_front_wheels'));
    blocks.push(block('picar_s_cali_left_wheel'));
    blocks.push(block('picar_s_cali_right_wheel'));
    blocks.push('=');
    //blocks.push(watcherToggle('picar_s_ultra_get_distance'));
    blocks.push(block('picar_s_ultra_get_distance'));
    blocks.push(watcherToggle('picar_s_light_analog'));
    blocks.push(block('picar_s_light_analog'));
    blocks.push(watcherToggle('picar_s_line_analog'));
    blocks.push(block('picar_s_line_analog'));
    blocks.push('-');
    blocks.push(block('picar_s_light_analog_index'));
    blocks.push(block('picar_s_line_analog_index'));
    blocks.push('=');
    blocks.push(block('picar_s_device_status'));

}

// PiCar-S
SpriteMorph.prototype.categories.push('PiCar_S')   // Add categories
// Define category colors
SpriteMorph.prototype.blockColor.PiCar_S = new Color(240, 98, 146)   // pink 300 #F06292
/*
type:   command
        reporter
        predicate
        hat
        ring
 */

SpriteMorph.prototype.blocks.picar_s_rw_run = {    // Define blocks
    type    : 'command',
    category: 'PiCar_S',
    //spec: 'rear wheel %br    channel: %sf_motor_dir %br    direction: %sf_rw_dir %br    speed: %n',
    spec    : 'move %sf_rw_dir at %n',
    defaults: ['forward', 0]
  }

SpriteMorph.prototype.blocks.picar_s_rw_stop = {
    type    : 'command',
    category: 'PiCar_S',
    spec    : 'stop'
  }

SpriteMorph.prototype.blocks.picar_s_cam_turn = {
    type    : 'command',
    category: 'PiCar_S',
    //spec: '[PiCar-V]  Pan servo %br    angle: %n',
    spec    : 'camera turn %sf_cam_dir',
    defaults: ['center']
  }

SpriteMorph.prototype.blocks.picar_s_fw_turn = {
    type    : 'command',
    category: 'PiCar_S',
    //spec: '[PiCar-V]  Front wheels %br    turn: %sf_fw_dir',
    spec    : 'turn %sf_fw_dir',
    defaults: ['straight']
  }

SpriteMorph.prototype.blocks.picar_s_pwm_output = {
    type    : 'command',
    category: 'PiCar_S',
    spec    : 'set PWM %sf_pwm_chn to %n',
    defaults: ['0', 0]
  }

SpriteMorph.prototype.blocks.picar_s_servo_turn = {
    type    : 'command',
    category: 'PiCar_S',
    spec    : 'set servo %sf_pwm_chn to %n',
    defaults: ['0', 90]
  }

SpriteMorph.prototype.blocks.picar_s_get_analog = {
    type    : 'reporter',
    category: 'PiCar_S',
    spec    : 'analog %sf_Achn',
    defaults: ['0']
  }

SpriteMorph.prototype.blocks.picar_s_get_digital = {
    type    : 'reporter',
    category: 'PiCar_S',
    spec    : 'digital %sf_Dchn',
    defaults: ['B20']
  }

SpriteMorph.prototype.blocks.picar_s_set_digital = {
    type    : 'command',
    category: 'PiCar_S',
    spec    : 'set digital %sf_Dchn to %sf_io_state',
    defaults: ['B20','HIGH']
  }

SpriteMorph.prototype.blocks.picar_s_cali_front_wheels = {
    type    : 'command',
    category: 'PiCar_S',
    spec    : 'set steering offset to %n',
    defaults: [0]
  }

SpriteMorph.prototype.blocks.picar_s_cali_left_wheel = {
    type    : 'command',
    category: 'PiCar_S',
    spec    : 'set left wheel forward to %sf_0_1',
    defaults: [0]
  }

SpriteMorph.prototype.blocks.picar_s_cali_right_wheel = {
    type    : 'command',
    category: 'PiCar_S',
    spec    : 'set right wheel forward to %sf_0_1',
    defaults: [0]
  }

SpriteMorph.prototype.blocks.picar_s_ultra_get_distance = {
    type    : 'reporter',
    category: 'PiCar_S',
    spec    : 'ultrasonic distance %sf_Dchn',
    defaults: ['20']
  }

SpriteMorph.prototype.blocks.picar_s_light_analog_index = {
    type    : 'reporter',
    category: 'PiCar_S',
    spec    : 'light_follower state %lt_index_chn',
    defaults: ["0"]
  }

SpriteMorph.prototype.blocks.picar_s_light_analog = {
    type    : 'reporter',
    category: 'PiCar_S',
    spec    : 'light_follower state'
  }

SpriteMorph.prototype.blocks.picar_s_line_analog_index = {
    type    : 'reporter',
    category: 'PiCar_S',
    spec    : 'line_follower state %lf_index_chn',
    defaults: [1]
  }

SpriteMorph.prototype.blocks.picar_s_line_analog = {
    type    : 'reporter',
    category: 'PiCar_S',
    spec    : 'line_follower state'
  }

SpriteMorph.prototype.blocks.picar_s_device_status = {
    type    : 'reporter',
    category: 'PiCar_S',
    spec    : 'device status'
  }

// Relable

SpriteMorph.prototype.blockAlternatives.picar_s_rw_run = ['picar_s_rw_stop'];
SpriteMorph.prototype.blockAlternatives.picar_s_rw_stop = ['picar_s_rw_run'];
SpriteMorph.prototype.blockAlternatives.picar_s_light_analog_index = ['picar_s_light_analog'];
SpriteMorph.prototype.blockAlternatives.picar_s_light_analog = ['picar_s_light_analog_index'];
SpriteMorph.prototype.blockAlternatives.picar_s_line_analog_index = ['picar_s_line_analog'];
SpriteMorph.prototype.blockAlternatives.picar_s_line_analog = ['picar_s_line_analog_index'];
SpriteMorph.prototype.blockAlternatives.picar_s_pwm_output = ['picar_s_servo_turn'];
SpriteMorph.prototype.blockAlternatives.picar_s_servo_turn = ['picar_s_pwm_output'];
SpriteMorph.prototype.blockAlternatives.picar_s_cali_front_wheels = ['picar_s_cali_left_wheel', 'picar_s_cali_right_wheel'];
SpriteMorph.prototype.blockAlternatives.picar_s_cali_left_wheel = ['picar_s_cali_front_wheels', 'picar_s_cali_right_wheel'];
SpriteMorph.prototype.blockAlternatives.picar_s_cali_right_wheel = ['picar_s_cali_front_wheels', 'picar_s_cali_left_wheel'];

// SunFounder process

SpriteMorph.prototype.picar_s_rw_run = function (direction, speed) { // Define process
  //reportURL('192.168.0.102:8000/run/picar-s/?action=pwmchannel&value=' + value)
  requests('picar-s', 'rw_run', 'both', direction, speed)
};

SpriteMorph.prototype.picar_s_rw_stop = function () {
  requests('picar-s', 'rw_stop')
};

SpriteMorph.prototype.picar_s_fw_turn = function (value) {
  //reportURL('192.168.0.102:8000/run/picar-s/?action=fw_turn&value=' + value)
  requests('picar-s', 'fw_turn', value)
};

SpriteMorph.prototype.picar_s_pwm_output = function (pwm_channel, value) {
  //reportURL('192.168.0.102:8000/run/picar-s/?action=pwmchannel&value=' + value)
  requests('picar-s', 'pwm_output', pwm_channel, value)
};

SpriteMorph.prototype.picar_s_servo_turn = function (servo_channel, angle) {
  //reportURL('192.168.0.102:8000/run/picar-s/?action=servo_turn&value=' + value)
  requests('picar-s', 'servo_turn', servo_channel, angle)
};

SpriteMorph.prototype.picar_s_get_analog = function (analog_channel) {
  //reportURL('192.168.0.102:8000/run/picar-s/?action=get_analog&value=' + value)
  return requests('picar-s', 'get_analog', analog_channel)
};

SpriteMorph.prototype.picar_s_get_digital = function (digital_channel) {
  //reportURL('192.168.0.102:8000/run/picar-s/?action=get_digital&value=' + value)
  return requests('raspberry_pi', 'gpio', 'input', digital_channel)
};

SpriteMorph.prototype.picar_s_set_digital = function (digital_channel, value) {
  //reportURL('192.168.0.102:8000/run/picar-s/?action=set_digital&value=' + value)
  requests('raspberry_pi', 'gpio', 'output', digital_channel, value)
};

SpriteMorph.prototype.picar_s_cali_front_wheels = function (offset) {
  //reportURL('192.168.0.102:8000/run/picar-s/?action=set_digital&value=' + value)
  requests('picar-s', 'calibrate', 'front_wheels', offset)
};

SpriteMorph.prototype.picar_s_cali_left_wheel = function (offset) {
  //reportURL('192.168.0.102:8000/run/picar-s/?action=set_digital&value=' + value)
  requests('picar-s', 'calibrate', 'left_wheel', offset)
};

SpriteMorph.prototype.picar_s_cali_right_wheel = function (offset) {
  //reportURL('192.168.0.102:8000/run/picar-s/?action=set_digital&value=' + value)
  requests('picar-s', 'calibrate', 'right_wheel', offset)
};

SpriteMorph.prototype.picar_s_ultra_get_distance = function (channel) {
  //reportURL('192.168.0.102:8000/run/picar-s/?action=set_digital&value=' + value)
  return requests('picar-s', 'ultra_distance', channel)
};

SpriteMorph.prototype.picar_s_light_analog_index = function (channel) {
  //reportURL('192.168.0.102:8000/run/picar-s/?action=get_analog&value=' + value)
  return requests('picar-s', 'light_follower_analog', channel)
};

SpriteMorph.prototype.picar_s_light_analog = function (channel) {
  //reportURL('192.168.0.102:8000/run/picar-s/?action=get_analog&value=' + value)
  var result = new List()
  raw_result = requests('picar-s', 'light_follower_analog').split(',');
  for (i=0; i<raw_result.length; i++){
    result.add(raw_result[i])
  }
  return result
};

SpriteMorph.prototype.picar_s_line_analog_index = function (channel) {
  //reportURL('192.168.0.102:8000/run/picar-s/?action=get_analog&value=' + value)
  return requests('picar-s', 'line_follower_analog', channel)
};

SpriteMorph.prototype.picar_s_line_analog = function (channel) {
  //reportURL('192.168.0.102:8000/run/picar-s/?action=get_analog&value=' + value)
  var result = new List()
  raw_result = requests('picar-s', 'line_follower_analog').split(',');
  for (i=0; i<raw_result.length; i++){
    result.add(raw_result[i])
  }
  return result
};

SpriteMorph.prototype.picar_s_device_status = function () {
  //reportURL('192.168.0.102:8000/run/picar-s/?action=get_analog&value=' + value)
  return requests('picar-s', 'device_status')
};