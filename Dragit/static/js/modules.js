// SunFounder modules

modules.cloud = "2017-May-05"

SpriteMorph.prototype.loadModulesCategories = function(blocks, block, watcherToggle){
    blocks.push(block('ultra_get_distance'));
    blocks.push('-');
    blocks.push(watcherToggle('light_analog'));
    blocks.push(block('light_analog'));
    blocks.push('-');
    blocks.push(watcherToggle('line_analog'));
    blocks.push(block('line_analog'));
    blocks.push('-');
    blocks.push(block('light_analog_index'));
    blocks.push(block('line_analog_index'));
}

// modules
SpriteMorph.prototype.categories.push('Modules')   // Add categories

SpriteMorph.prototype.blockColor.Modules = new Color(56, 142, 60)    // Green 700 rgb(56, 142, 60)

/*
type:   command
        reporter
        predicate
        hat
        ring
 */

SpriteMorph.prototype.blocks.ultra_get_distance = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'ultrasonic distance %rpi_io_chn',
    defaults: ['17']
  }

SpriteMorph.prototype.blocks.light_analog_index = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'light_follower state %lt_index_chn',
    defaults: ["0"]
  }

SpriteMorph.prototype.blocks.light_analog = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'light_follower state'
  }

SpriteMorph.prototype.blocks.line_analog_index = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'line_follower state %lf_index_chn',
    defaults: [1]
  }

SpriteMorph.prototype.blocks.line_analog = {
    type    : 'reporter',
    category: 'Modules',
    spec    : 'line_follower state'
  }

// Relable
SpriteMorph.prototype.blockAlternatives.light_analog_index = ['light_analog'];
SpriteMorph.prototype.blockAlternatives.light_analog = ['light_analog_index'];
SpriteMorph.prototype.blockAlternatives.line_analog_index = ['line_analog'];
SpriteMorph.prototype.blockAlternatives.line_analog = ['line_analog_index'];

// SunFounder process

SpriteMorph.prototype.ultra_get_distance = function (channel) {
  //reportURL('192.168.0.102:8000/run/modules/?action=set_digital&value=' + value)
  return requests('modules', 'ultra_distance', channel)
};

SpriteMorph.prototype.light_analog_index = function (channel) {
  //reportURL('192.168.0.102:8000/run/modules/?action=get_analog&value=' + value)
  return requests('modules', 'light_follower_analog', channel)
};

SpriteMorph.prototype.light_analog = function (channel) {
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

SpriteMorph.prototype.line_analog = function (channel) {
  //reportURL('192.168.0.102:8000/run/modules/?action=get_analog&value=' + value)
  var result = new List()
  raw_result = requests('modules', 'line_follower_analog').split(',');
  for (i=0; i<raw_result.length; i++){
    result.add(raw_result[i])
  }
  return result
};

