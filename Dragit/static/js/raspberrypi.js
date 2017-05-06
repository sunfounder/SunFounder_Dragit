// SunFounder PiCar-V

modules.cloud = "2017-May-05"

SpriteMorph.prototype.loadRaspberryPiCategories = function(blocks, block, watcherToggle){
    blocks.push(block('rpi_gpio_set'));
    blocks.push(block('rpi_gpio_get'));
    blocks.push('=');
    blocks.push(block('cpu_temperature'));
    blocks.push(block('gpu_temperature'));
    blocks.push(block('cpu_usage'));
    blocks.push(block('ram_total'));
    blocks.push(block('ram_used'));
    blocks.push(block('disk_total'));
    blocks.push(block('disk_used'));
}

// PiCar-V
SpriteMorph.prototype.categories.push('RaspberryPi')   // Add categories

SpriteMorph.prototype.blockColor.RaspberryPi = new Color(51, 204, 51)    // Define category colors

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
    spec: 'GPIO %rpi_io_chn %sf_io_state_dir',
    defaults: ['0', 'LOW']
  }

SpriteMorph.prototype.blocks.rpi_gpio_get = {    // Define blocks
    type: 'reporter',
    category: 'RaspberryPi',
    spec: 'GPIO %rpi_io_chn',
    defaults: ['0']
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
// SunFounder process


SpriteMorph.prototype.rpi_gpio_set = function (channel, status) { // Define process
  //reportURL('192.168.0.102:8000/run/picar-v/?action=pwmchannel&value=' + value)
  requests('raspberry_pi', 'gpio', 'output', channel, status)
};

SpriteMorph.prototype.rpi_gpio_get = function (channel) { // Define process
  //reportURL('192.168.0.102:8000/run/picar-v/?action=pwmchannel&value=' + value)
  return requests('raspberry_pi', 'gpio', 'input', channel)
};

SpriteMorph.prototype.cpu_temperature = function () { // Define process
  //reportURL('192.168.0.102:8000/run/picar-v/?action=pwmchannel&value=' + value)
  return requests('raspberry_pi', 'cpu_temperature')
};

SpriteMorph.prototype.gpu_temperature = function () { // Define process
  //reportURL('192.168.0.102:8000/run/picar-v/?action=pwmchannel&value=' + value)
  return requests('raspberry_pi', 'gpu_temperature')
};

SpriteMorph.prototype.cpu_usage = function () { // Define process
  //reportURL('192.168.0.102:8000/run/picar-v/?action=pwmchannel&value=' + value)
  return requests('raspberry_pi', 'cpu_usage')
};

SpriteMorph.prototype.ram_total = function () { // Define process
  //reportURL('192.168.0.102:8000/run/picar-v/?action=pwmchannel&value=' + value)
  return requests('raspberry_pi', 'ram_total')
};

SpriteMorph.prototype.ram_used = function () { // Define process
  //reportURL('192.168.0.102:8000/run/picar-v/?action=pwmchannel&value=' + value)
  return requests('raspberry_pi', 'ram_used')
};

SpriteMorph.prototype.disk_total = function () { // Define process
  //reportURL('192.168.0.102:8000/run/picar-v/?action=pwmchannel&value=' + value)
  return requests('raspberry_pi', 'disk_total')
};

SpriteMorph.prototype.disk_used = function () { // Define process
  //reportURL('192.168.0.102:8000/run/picar-v/?action=pwmchannel&value=' + value)
  return requests('raspberry_pi', 'disk_used')
};
