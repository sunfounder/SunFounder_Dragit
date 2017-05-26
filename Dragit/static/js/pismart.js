// SunFounder PiSmart

modules.cloud = "2017-May"

SpriteMorph.prototype.loadPiSmartCategories = function(blocks, block, watcherToggle){
    blocks.push(block('pismart_led_bright'));
    blocks.push(block('pismart_led_off'));
    blocks.push('=');
    blocks.push(block('pismart_motor_run'));
    blocks.push('-');
    blocks.push(block('pismart_servo_turn'));
    blocks.push(block('pismart_pwm_output'));
    blocks.push('-');
    blocks.push(block('pismart_get_analog'));
    blocks.push(block('pismart_set_digital'));
    blocks.push(block('pismart_get_digital'));
    blocks.push('=');
    blocks.push(block('pismart_say'));
    blocks.push('=');
    blocks.push(block('pismart_dictionary'));
    blocks.push(block('pismart_set_dictionary'));
    blocks.push('=');
    blocks.push(block('pismart_heard'));
    blocks.push(block('pismart_is_heard'));
    blocks.push(block('pismart_result'));
    blocks.push('=');
    blocks.push(block('pismart_device_status'));
}

// PiCar-S
SpriteMorph.prototype.categories.push('PiSmart')   // Add categories
// Define category colors
SpriteMorph.prototype.blockColor.PiSmart = new Color(121, 85, 72)   // brown 500 #795548
/*
type:   command
        reporter
        predicate
        hat
        <ring></ring>
 */

SpriteMorph.prototype.blocks.pismart_led_bright = {    // Define blocks
    type    : 'command',
    category: 'PiSmart',
    spec    : 'set led to %n',
    defaults: [0]
  }

SpriteMorph.prototype.blocks.pismart_led_off = {
    type    : 'command',
    category: 'PiSmart',
    spec    : 'led off'
  }

SpriteMorph.prototype.blocks.pismart_motor_run = {
    type    : 'command',
    category: 'PiSmart',
    spec    : 'set motor %pismart_motor_chn to %n',
    defaults: ['A', 0]
  }

SpriteMorph.prototype.blocks.pismart_pwm_output = {
    type    : 'command',
    category: 'PiSmart',
    spec    : 'set PWM %pismart_pwm_chn to %n',
    defaults: ['0', 0]
  }

SpriteMorph.prototype.blocks.pismart_servo_turn = {
    type    : 'command',
    category: 'PiSmart',
    spec    : 'set servo %pismart_pwm_chn to %n',
    defaults: ['0', 90]
  }

SpriteMorph.prototype.blocks.pismart_get_analog = {
    type    : 'reporter',
    category: 'PiSmart',
    spec    : 'analog %pismart_Achn',
    defaults: ['0']
  }

SpriteMorph.prototype.blocks.pismart_set_digital = {
    type    : 'command',
    category: 'PiSmart',
    spec    : 'set digital %pismart_Dchn %D_state',
    defaults: ['0', 'HIGH']
  }

SpriteMorph.prototype.blocks.pismart_get_digital = {
    type    : 'reporter',
    category: 'PiSmart',
    spec    : 'get digital %pismart_Dchn',
    defaults: ['0']
  }

SpriteMorph.prototype.blocks.pismart_say = {
    type    : 'command',
    category: 'PiSmart',
    spec    : 'PiSmart say %s',
    defaults: ['Hello!']
  }

SpriteMorph.prototype.blocks.pismart_dictionary = {
    type    : 'reporter',
    category: 'PiSmart',
    spec    : 'dictionary %s : %s',
    defaults: [localize('command'), localize('words')]
  }

SpriteMorph.prototype.blocks.pismart_set_dictionary = {
    type    : 'command',
    category: 'PiSmart',
    spec    : 'set dictionary %exp'
  }

SpriteMorph.prototype.blocks.pismart_heard = {
    type    : 'predicate',
    category: 'PiSmart',
    spec    : 'heard'
  }

SpriteMorph.prototype.blocks.pismart_is_heard = {
    type    : 'predicate',
    category: 'PiSmart',
    spec    : '%s is heard'
  }

SpriteMorph.prototype.blocks.pismart_result = {
    type    : 'reporter',
    category: 'PiSmart',
    spec    : 'hear result'
  }

SpriteMorph.prototype.blocks.pismart_device_status = {
    type    : 'reporter',
    category: 'PiSmart',
    spec    : 'device status'
  }

// Relable

SpriteMorph.prototype.blockAlternatives.pismart_led_bright  = ['pismart_led_off'];
SpriteMorph.prototype.blockAlternatives.pismart_led_off     = ['pismart_led_bright'];
SpriteMorph.prototype.blockAlternatives.pismart_pwm_output  = ['pismart_servo_turn'];
SpriteMorph.prototype.blockAlternatives.pismart_servo_turn  = ['pismart_pwm_output'];
SpriteMorph.prototype.blockAlternatives.pismart_say         = ['pismart_heard'];
SpriteMorph.prototype.blockAlternatives.pismart_heard       = ['pismart_say','pismart_is_heard'];
SpriteMorph.prototype.blockAlternatives.pismart_is_heard    = ['pismart_say','pismart_heard'];
SpriteMorph.prototype.blockAlternatives.pismart_get_analog  = ['pismart_get_digital', 'pismart_set_digital']
SpriteMorph.prototype.blockAlternatives.pismart_get_digital = ['pismart_get_analog', 'pismart_set_digital']
SpriteMorph.prototype.blockAlternatives.pismart_set_digital = ['pismart_get_digital', 'pismart_get_analog']

// SunFounder process

SpriteMorph.prototype.pismart_led_bright = function (brightness) { // Define process
  //reportURL('192.168.0.102:8000/run/pismart/?action=pwmchannel&value=' + value)
  requests('pismart', 'set_led_brightness', brightness)
};

SpriteMorph.prototype.pismart_led_off = function () {
  requests('pismart', 'led_off')
};

SpriteMorph.prototype.pismart_motor_run = function (motor_chn, speed) {
  //reportURL('192.168.0.102:8000/run/pismart/?action=fw_turn&value=' + value)
  requests('pismart', 'motor_run', motor_chn, speed)
};

SpriteMorph.prototype.pismart_pwm_output = function (pwm_channel, value) {
  //reportURL('192.168.0.102:8000/run/pismart/?action=pwmchannel&value=' + value)
  requests('pismart', 'pwm_output', pwm_channel, value)
};

SpriteMorph.prototype.pismart_servo_turn = function (servo_channel, angle) {
  //reportURL('192.168.0.102:8000/run/pismart/?action=servo_turn&value=' + value)
  requests('pismart', 'servo_turn', servo_channel, angle)
};

SpriteMorph.prototype.pismart_get_analog = function (analog_channel) {
  //reportURL('192.168.0.102:8000/run/pismart/?action=get_analog&value=' + value)
  return requests('pismart', 'get_analog', analog_channel)
};

SpriteMorph.prototype.pismart_get_digital = function (digital_channel) {
  //reportURL('192.168.0.102:8000/run/pismart/?action=get_analog&value=' + value)
  return requests('pismart', 'get_digital', digital_channel)
};

SpriteMorph.prototype.pismart_set_digital = function (digital_channel, digital_state) {
  //reportURL('192.168.0.102:8000/run/pismart/?action=get_analog&value=' + value)
  requests('pismart', 'set_digital', digital_channel, digital_state)
};

SpriteMorph.prototype.pismart_say = function (words) {
  //reportURL('192.168.0.102:8000/run/pismart/?action=get_analog&value=' + value)
  return requests('pismart', 'say', words)
};

SpriteMorph.prototype.pismart_dictionary = function (cmd, words) {
  //reportURL('192.168.0.102:8000/run/pismart/?action=get_analog&value=' + value)
  result = cmd + ':' + words;
  return result
};

SpriteMorph.prototype.pismart_set_dictionary = function (dic) {
  //reportURL('192.168.0.102:8000/run/pismart/?action=get_analog&value=' + value)
  dic = dic.asArray();
  result = dic.join(',');
  return requests('pismart', 'set_dictionary', result)
};

SpriteMorph.prototype.pismart_heard = function () {
  //reportURL('192.168.0.102:8000/run/pismart/?action=get_analog&value=' + value)
  result = requests('pismart', 'heard')
  if (result == 'True')
    result = true;
  else
    result = false
  return result
};

SpriteMorph.prototype.pismart_is_heard = function (command) {
  //reportURL('192.168.0.102:8000/run/pismart/?action=get_analog&value=' + value)
  result = this.pismart_result()
  if (result == command)
    result = true;
  else
    result = false
  return result
};

SpriteMorph.prototype.pismart_result = function () {
  //reportURL('192.168.0.102:8000/run/pismart/?action=get_analog&value=' + value)
  return requests('pismart', 'result')
};

SpriteMorph.prototype.pismart_device_status = function () {
  //reportURL('192.168.0.102:8000/run/pismart/?action=get_analog&value=' + value)
  return requests('pismart', 'device_status')
};