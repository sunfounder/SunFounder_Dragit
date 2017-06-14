// SunFounder PiCar-V

modules.cloud = "2017-May-05"

SpriteMorph.prototype.loadPiCarVCategories = function(blocks, block, watcherToggle){
    blocks.push(block('picar_v_rw_run'));
    blocks.push(block('picar_v_rw_stop'));
    blocks.push(block('picar_v_fw_turn'));
    blocks.push('=');
    blocks.push(block('picar_v_cam_switch'));
    blocks.push(block('picar_v_cam_turn'));
    blocks.push(block('picar_v_cam_reset'));
    blocks.push(block('picar_v_pan_turn'));
    blocks.push(block('picar_v_tilt_turn'));
    blocks.push('=');
    blocks.push(block('picar_v_servo_turn'));
    blocks.push(block('picar_v_pwm_output'));
    blocks.push(block('picar_v_set_digital'));
    blocks.push(block('picar_v_get_digital'));
    blocks.push(block('picar_v_get_analog'));
    blocks.push('=');
    blocks.push(block('picar_v_cali_front_wheels'));
    blocks.push(block('picar_v_cali_left_wheel'));
    blocks.push(block('picar_v_cali_right_wheel'));
    blocks.push(block('picar_v_cali_pan_servo'));
    blocks.push(block('picar_v_cali_tilt_servo'));
    blocks.push('=');
    blocks.push(block('picar_v_device_status'));
}

// PiCar-V
SpriteMorph.prototype.categories.push('PiCar_V')   // Add categories

SpriteMorph.prototype.blockColor.PiCar_V = new Color(229, 115, 115)    // rgb(229, 115, 115) Define category colors rgb(211, 47, 47)
/*
type:   command
        reporter
        predicate
        hat
        ring
 */

SpriteMorph.prototype.blocks.picar_v_rw_run = {    // Define blocks
    type    : 'command',
    category: 'PiCar_V',
    spec    : 'move %sf_rw_dir at %n',
    defaults: ['forward', 0]
  }

SpriteMorph.prototype.blocks.picar_v_rw_stop = {
    type    : 'command',
    category: 'PiCar_V',
    spec    : 'stop'
  }

SpriteMorph.prototype.blocks.picar_v_cam_switch = {
    type    : 'command',
    category: 'PiCar_V',
    spec    : 'camera switch %sf_on_off',
    defaults: ['off']
  }

SpriteMorph.prototype.blocks.picar_v_cam_turn = {
    type    : 'command',
    category: 'PiCar_V',
    spec    : 'camera turn %sf_cam_dir',
    defaults: ['up']
  }

SpriteMorph.prototype.blocks.picar_v_cam_reset = {
    type    : 'command',
    category: 'PiCar_V',
    spec    : 'camera reset'
  }

SpriteMorph.prototype.blocks.picar_v_fw_turn = {
    type    : 'command',
    category: 'PiCar_V',
    spec    : 'turn %sf_fw_dir',
    defaults: ['straight']
  }

SpriteMorph.prototype.blocks.picar_v_pan_turn = {
    type    : 'command',
    category: 'PiCar_V',
    spec    : 'camera pan %n',
    defaults: [0]
  }

SpriteMorph.prototype.blocks.picar_v_tilt_turn = {
    type    : 'command',
    category: 'PiCar_V',
    spec    : 'camera tilt %n',
    defaults: [0]
  }

SpriteMorph.prototype.blocks.picar_v_pwm_output = {
    type    : 'command',
    category: 'PiCar_V',
    spec    : 'set PWM %sf_pwm_chn to %n',
    defaults: ['0', 0]
  }

SpriteMorph.prototype.blocks.picar_v_servo_turn = {
    type    : 'command',
    category: 'PiCar_V',
    spec    : 'set servo %sf_pwm_chn to %n',
    defaults: ['0', 90]
  }

SpriteMorph.prototype.blocks.picar_v_get_analog = {
    type    : 'reporter',
    category: 'PiCar_V',
    spec    : 'analog %sf_Achn',
    defaults: ['0']
  }

SpriteMorph.prototype.blocks.picar_v_get_digital = {
    type    : 'reporter',
    category: 'PiCar_V',
    spec    : 'digital %sf_Dchn',
    defaults: ['B20']
  }

SpriteMorph.prototype.blocks.picar_v_set_digital = {
    type    : 'command',
    category: 'PiCar_V',
    spec    : 'set digital %sf_Dchn to %sf_io_state',
    defaults: ['B20','HIGH']
  }

SpriteMorph.prototype.blocks.picar_v_cali_front_wheels = {
    type    : 'command',
    category: 'PiCar_V',
    spec    : 'set steering offset to %n',
    defaults: [0]
  }

SpriteMorph.prototype.blocks.picar_v_cali_left_wheel = {
    type    : 'command',
    category: 'PiCar_V',
    spec    : 'set left wheel forward to %sf_0_1',
    defaults: [0]
  }

SpriteMorph.prototype.blocks.picar_v_cali_right_wheel = {
    type    : 'command',
    category: 'PiCar_V',
    spec    : 'set right wheel forward to %sf_0_1',
    defaults: [0]
  }

SpriteMorph.prototype.blocks.picar_v_cali_pan_servo = {
    type    : 'command',
    category: 'PiCar_V',
    spec    : 'set camera pan offset to %n',
    defaults: [0]
  }

SpriteMorph.prototype.blocks.picar_v_cali_tilt_servo = {
    type    : 'command',
    category: 'PiCar_V',
    spec    : 'set camera tilt offset to %n',
    defaults: [0]
  }

SpriteMorph.prototype.blocks.picar_v_find_blob = {
    type    : 'command',
    category: 'PiCar_V',
    spec    : 'find red blob'
  }

SpriteMorph.prototype.blocks.picar_v_get_blob = {
    type    : 'reporter',
    category: 'PiCar_V',
    spec    : 'blob %sf_blob_dir',
    defaults: ["x"]
  }

SpriteMorph.prototype.blocks.picar_v_device_status = {
    type    : 'reporter',
    category: 'PiCar_V',
    spec    : 'device status'
  }

// Relable
SpriteMorph.prototype.blockAlternatives.picar_v_rw_run = ['picar_v_rw_stop'];
SpriteMorph.prototype.blockAlternatives.picar_v_rw_stop = ['picar_v_rw_run'];
SpriteMorph.prototype.blockAlternatives.picar_v_pan_turn = ['picar_v_tilt_turn'];
SpriteMorph.prototype.blockAlternatives.picar_v_tilt_turn = ['picar_v_pan_turn'];
SpriteMorph.prototype.blockAlternatives.picar_v_light_analog_index = ['picar_v_light_analog'];
SpriteMorph.prototype.blockAlternatives.picar_v_light_analog = ['picar_v_light_analog_index'];
SpriteMorph.prototype.blockAlternatives.picar_v_line_analog_index = ['picar_v_line_analog'];
SpriteMorph.prototype.blockAlternatives.picar_v_line_analog = ['picar_v_line_analog_index'];
SpriteMorph.prototype.blockAlternatives.picar_v_pwm_output = ['picar_v_servo_turn'];
SpriteMorph.prototype.blockAlternatives.picar_v_servo_turn = ['picar_v_pwm_output'];
SpriteMorph.prototype.blockAlternatives.picar_v_cali_front_wheels = ['picar_v_cali_left_wheel', 'picar_v_cali_right_wheel', 'picar_v_cali_pan_servo', 'picar_v_cali_tilt_servo'];
SpriteMorph.prototype.blockAlternatives.picar_v_cali_left_wheel = ['picar_v_cali_front_wheels', 'picar_v_cali_right_wheel', 'picar_v_cali_pan_servo', 'picar_v_cali_tilt_servo'];
SpriteMorph.prototype.blockAlternatives.picar_v_cali_right_wheel = ['picar_v_cali_front_wheels', 'picar_v_cali_left_wheel', 'picar_v_cali_pan_servo', 'picar_v_cali_tilt_servo'];
SpriteMorph.prototype.blockAlternatives.picar_v_cali_pan_servo = ['picar_v_cali_front_wheels', 'picar_v_cali_left_wheel', 'picar_v_cali_right_wheel', 'picar_v_cali_tilt_servo'];
SpriteMorph.prototype.blockAlternatives.picar_v_cali_tilt_servo = ['picar_v_cali_front_wheels', 'picar_v_cali_left_wheel', 'picar_v_cali_right_wheel', 'picar_v_cali_pan_servo'];

// SunFounder process

SpriteMorph.prototype.picar_v_rw_run = function (direction, speed) { // Define process
  //reportURL('192.168.0.102:8000/run/picar-v/?action=pwmchannel&value=' + value)
  return requests('picar-v', 'rw_run', 'both', direction, speed)
};

SpriteMorph.prototype.picar_v_rw_stop = function () {
  return requests('picar-v', 'rw_stop')
};

SpriteMorph.prototype.picar_v_fw_turn = function (value) {
  //reportURL('192.168.0.102:8000/run/picar-v/?action=fw_turn&value=' + value)
  return requests('picar-v', 'fw_turn', value)
};

SpriteMorph.prototype.picar_v_cam_switch = function (value) {
  //reportURL('192.168.0.102:8000/run/picar-v/?action=fw_turn&value=' + value)
  return requests('picar-v', 'cam_switch', value)
};

SpriteMorph.prototype.picar_v_cam_turn = function (value) {
  //reportURL('192.168.0.102:8000/run/picar-v/?action=fw_turn&value=' + value)
  return requests('picar-v', 'cam_turn', value)
};

SpriteMorph.prototype.picar_v_cam_reset = function () {
  //reportURL('192.168.0.102:8000/run/picar-v/?action=fw_turn&value=' + value)
  return requests('picar-v', 'cam_turn', 'center')
};

SpriteMorph.prototype.picar_v_pan_turn = function (value) {
  //reportURL('192.168.0.102:8000/run/picar-v/?action=pan_turn&value=' + value)
  return requests('picar-v', 'pan_turn', value)
};

SpriteMorph.prototype.picar_v_tilt_turn = function (value) {
  //reportURL('192.168.0.102:8000/run/picar-v/?action=tilt_turn&value=' + value)
  return requests('picar-v', 'tilt_turn', value)
};

SpriteMorph.prototype.picar_v_pwm_output = function (pwm_channel, value) {
  //reportURL('192.168.0.102:8000/run/picar-v/?action=pwmchannel&value=' + value)
  return requests('picar-v', 'pwm_output', pwm_channel, value)
};

SpriteMorph.prototype.picar_v_servo_turn = function (servo_channel, angle) {
  //reportURL('192.168.0.102:8000/run/picar-v/?action=servo_turn&value=' + value)
  return requests('picar-v', 'servo_turn', servo_channel, angle)
};

SpriteMorph.prototype.picar_v_get_analog = function (analog_channel) {
  //reportURL('192.168.0.102:8000/run/picar-v/?action=get_analog&value=' + value)
  return requests('picar-v', 'get_analog', analog_channel)
};

SpriteMorph.prototype.picar_v_get_digital = function (digital_channel) {
  //reportURL('192.168.0.102:8000/run/picar-v/?action=get_digital&value=' + value)
  return requests('raspberry_pi', 'gpio', 'input', digital_channel)
};

SpriteMorph.prototype.picar_v_set_digital = function (digital_channel, value) {
  //reportURL('192.168.0.102:8000/run/picar-v/?action=set_digital&value=' + value)
  return requests('raspberry_pi', 'gpio', 'output', digital_channel, value)
};

SpriteMorph.prototype.picar_v_cali_front_wheels = function (offset) {
  //reportURL('192.168.0.102:8000/run/picar-v/?action=set_digital&value=' + value)
  return requests('picar-v', 'calibrate', 'front_wheels', offset)
};

SpriteMorph.prototype.picar_v_cali_left_wheel = function (offset) {
  //reportURL('192.168.0.102:8000/run/picar-v/?action=set_digital&value=' + value)
  return requests('picar-v', 'calibrate', 'left_wheel', offset)
};

SpriteMorph.prototype.picar_v_cali_right_wheel = function (offset) {
  //reportURL('192.168.0.102:8000/run/picar-v/?action=set_digital&value=' + value)
  return requests('picar-v', 'calibrate', 'right_wheel', offset)
};

SpriteMorph.prototype.picar_v_cali_pan_servo = function (offset) {
  //reportURL('192.168.0.102:8000/run/picar-v/?action=set_digital&value=' + value)
  return requests('picar-v', 'calibrate', 'pan_servo', offset)
};

SpriteMorph.prototype.picar_v_cali_tilt_servo = function (offset) {
  //reportURL('192.168.0.102:8000/run/picar-v/?action=set_digital&value=' + value)
  return requests('picar-v', 'calibrate', 'tilt_servo', offset)
};


SpriteMorph.prototype.picar_v_find_blob = function () {
  //reportURL('192.168.0.102:8000/run/picar-v/?action=set_digital&value=' + value)
  return requests('picar-v', 'find_blob')
};

SpriteMorph.prototype.picar_v_get_blob = function (state) {
  //reportURL('192.168.0.102:8000/run/picar-v/?action=get_analog&value=' + value)
  return requests('picar-v', 'get_blob', state)
};

SpriteMorph.prototype.picar_v_device_status = function () {
  //reportURL('192.168.0.102:8000/run/picar-v/?action=get_analog&value=' + value)
  return requests('picar-v', 'device_status')
};
