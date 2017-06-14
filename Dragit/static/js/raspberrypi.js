// SunFounder PiCar-V

modules.cloud = "2017-May-05"

SpriteMorph.prototype.loadRaspberryPiCategories = function(blocks, block, watcherToggle){
    blocks.push(block('rpi_gpio_set'));
    blocks.push(block('rpi_gpio_get'));
    blocks.push(block('rpi_gpio_get_tf'));  //predicate
    blocks.push('=');
    blocks.push(block('rpi_i2cdetect'));
    blocks.push('=');
    blocks.push(block('cpu_temperature'));
    blocks.push(block('gpu_temperature'));
    blocks.push(block('cpu_usage'));
    blocks.push(block('ram_total'));
    blocks.push(block('ram_used'));
    blocks.push(block('disk_total'));
    blocks.push(block('disk_used'));
    blocks.push('=');
    blocks.push(block('bcm_num'));
    blocks.push(block('gpio_num'));
}

// PiCar-V
SpriteMorph.prototype.categories.push('RaspberryPi')   // Add categories

SpriteMorph.prototype.blockColor.RaspberryPi = new Color(56, 142, 60)    // Green 700 rgb(56, 142, 60)

/*
type:   command
        reporter
        predicate
        hat
        ring
 */

SpriteMorph.prototype.blocks.rpi_gpio_set = {    // Define blocks
    type: 'command',
    category: 'RaspberryPi',
    spec: 'gpio %rpi_bcm_chn %sf_io_state',
    defaults: ['17', 'LOW']
  }

SpriteMorph.prototype.blocks.rpi_gpio_get = {    // Define blocks
    type: 'reporter',
    category: 'RaspberryPi',
    spec: 'gpio %rpi_bcm_chn',
    defaults: ['17']
  }

SpriteMorph.prototype.blocks.rpi_gpio_get_tf = {    // Define blocks
    type: 'predicate',
    category: 'RaspberryPi',
    spec: 'gpio %rpi_bcm_chn',
    defaults: ['17']
  }

SpriteMorph.prototype.blocks.rpi_i2cdetect = {    // Define blocks
    type: 'reporter',
    category: 'RaspberryPi',
    spec: 'connected i2c at %rpi_busnum',
    defaults: ['1']
  }

SpriteMorph.prototype.blocks.cpu_temperature = {    // Define blocks
    type: 'reporter',
    category: 'RaspberryPi',
    spec: 'cpu temperature'
  }

SpriteMorph.prototype.blocks.gpu_temperature = {    // Define blocks
    type: 'reporter',
    category: 'RaspberryPi',
    spec: 'gpu temperature'
  }

SpriteMorph.prototype.blocks.cpu_usage = {    // Define blocks
    type: 'reporter',
    category: 'RaspberryPi',
    spec: 'cpu usage'
  }

SpriteMorph.prototype.blocks.ram_total = {    // Define blocks
    type: 'reporter',
    category: 'RaspberryPi',
    spec: 'ram total'
  }

SpriteMorph.prototype.blocks.ram_used = {    // Define blocks
    type: 'reporter',
    category: 'RaspberryPi',
    spec: 'ram used'
  }

SpriteMorph.prototype.blocks.disk_total = {    // Define blocks
    type: 'reporter',
    category: 'RaspberryPi',
    spec: 'disk total'
  }

SpriteMorph.prototype.blocks.disk_used = {    // Define blocks
    type: 'reporter',
    category: 'RaspberryPi',
    spec: 'disk used'
  }

SpriteMorph.prototype.blocks.bcm_num = {    // Define blocks
    type: 'reporter',
    category: 'RaspberryPi',
    spec: 'BCM %rpi_bcm_chn',
    defaults: [17]
  }

SpriteMorph.prototype.blocks.gpio_num = {    // Define blocks
    type: 'reporter',
    category: 'RaspberryPi',
    spec: 'GPIO %rpi_gpio_chn',
    defaults: [0]
  }

SpriteMorph.prototype.rpi_gpio_set = function (channel, status) { // Define process
  requests('raspberry_pi', 'gpio', 'output', channel, status)
};

SpriteMorph.prototype.rpi_gpio_get = function (channel) { // Define process
  return requests('raspberry_pi', 'gpio', 'input', channel)
};

SpriteMorph.prototype.rpi_gpio_get_tf = function (channel) { // Define process
  result = requests('raspberry_pi', 'gpio', 'input', channel);
  if (result == 1)
    result = true;
  else
    result = false;
  return result
};

SpriteMorph.prototype.rpi_i2cdetect = function (busnum) { // Define process
  var result = new List()
  raw_result = requests('raspberry_pi', 'i2cdetect', busnum).split(',');
  for (i=0; i<raw_result.length; i++){
    result.add(raw_result[i])
  }
  return result
};

SpriteMorph.prototype.cpu_temperature = function () { // Define process
  return requests('raspberry_pi', 'cpu_temperature')
};

SpriteMorph.prototype.gpu_temperature = function () { // Define process
  return requests('raspberry_pi', 'gpu_temperature')
};

SpriteMorph.prototype.cpu_usage = function () { // Define process
  return requests('raspberry_pi', 'cpu_usage')
};

SpriteMorph.prototype.ram_total = function () { // Define process
  return requests('raspberry_pi', 'ram_total')
};

SpriteMorph.prototype.ram_used = function () { // Define process
  return requests('raspberry_pi', 'ram_used')
};

SpriteMorph.prototype.disk_total = function () { // Define process
  return requests('raspberry_pi', 'disk_total')
};

SpriteMorph.prototype.disk_used = function () { // Define process
  return requests('raspberry_pi', 'disk_used')
};

SpriteMorph.prototype.bcm_num = function (num) { // Define process
  return num
};

var gpio_to_bcm = {
  0 : 17,
  1 : 18,
  2 : 22,
  3 : 27,
  4 : 23,
  5 : 24,
  6 : 25,
  7 : 4,
  21 : 5,
  22 : 6,
  23 : 13,
  24 : 19,
  25 : 26,
  26 : 12,
  27 : 16,
  28 : 20,
  29 : 21,
};

SpriteMorph.prototype.gpio_num = function (num) { // Define process
  result = gpio_to_bcm[num];
  return result
};
