
SpriteMorph.prototype.loadSunFounderCategories = function(blocks, block, watcherToggle, cat){
  if (cat === 'PiCar_V') {
    this.loadPiCarVCategories(blocks, block, watcherToggle);
  }
  if (cat === 'RaspberryPi') {
    this.loadRaspberryPiCategories(blocks, block, watcherToggle);
  }
}

function requests(device, action, value0=null, value1=null, value2=null){
  var xmlHttp  = new XMLHttpRequest();
  var protocol  = window.location.protocol;
  var host      = window.location.host;
  var pathname  = window.location.pathname;
  url = protocol + "//" + host + '/run/' + device + "/?action=" + action;
  if (value0 != null){
    url = url + "&value0=" + value0;
  }
  if (value1 != null){
    url = url + "&value1=" + value1;
  }
  if (value2 != null){
    url = url + "&value2=" + value2;
  }
  //document.getElementById("debug").innerHTML=url;
  xmlHttp.open( "GET", url, false );
  xmlHttp.send( null );
  return xmlHttp.responseText;
}

SyntaxElementMorph.prototype.loadSunFounderSymbols = function(spec){
  switch (spec){
    case '%sf_motor_dir':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          'left' : ['left'],
          'right' : ['right']
        },
        false // read-only
      );
      break;

    case '%sf_io_state_dir':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          'HIGH' : ['HIGH'],
          'LOW'  : ['LOW']
        },
        false // read-only
      );
      break;

    case '%sf_fw_dir':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          'straight' : ['straight'],
          'left' : ['left'],
          'right' : ['right']
        },
        false // read-only
      );
      break;

    case '%sf_rw_dir':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          'forward'  : ['forward'],
          'backward' : ['backward']
        },
        false // read-only
      );
      break;

    case '%sf_pwmchn_dir':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          '0' : ['0'],
          '1' : ['1'],
          '2' : ['2'],
          '3' : ['3'],
          '4' : ['4'],
          '5' : ['5'],
          '6' : ['6'],
          '7' : ['7'],
          '8' : ['8'],
          '9' : ['9'],
          '10' : ['10'],
          '11' : ['11'],
          '12' : ['12'],
          '13' : ['13'],
          '14' : ['14'],
          '15' : ['15']
        },
        false // read-only
      );
      break;

    case '%sf_Achn_dir':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          'A0' : ['A0'],
          'A1' : ['A1'],
          'A2' : ['A2'],
          'A3' : ['A3']
        },
        false // read-only
      );
      break;

    case '%sf_Dchn_dir':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "B20" : [20],
          "B16" : [16],
          "B12" : [12],
          "B26" : [26],
          "B19" : [19],
          "B13" : [13],
          "B6"  : [6],
          "B5"  : [5]
        },
        false // read-only
      );
      break;

    case '%sf_cali_dir':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "front wheel" : ["front wheel"],
          "left wheel"  : ["left wheel"],
          "right wheel" : ["right wheel"],
          "pan"         : ["pan"],
          "tilt"        : ["tilt"]
        },
        false // read-only
      );
      break;

    case '%rpi_bcm_chn':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "17" : 17,
          "18" : 18,
          "22" : 22,
          "27" : 27,
          "23" : 23,
          "24" : 24,
          "25" : 25,
          "4"  : 4,
          "5"  : 5,
          "6"  : 6,
          "13" : 13,
          "19" : 19,
          "26" : 26,
          "12" : 12,
          "16" : 16,
          "20" : 20,
          "21" : 21,
        },
        false // read-only
      );
      break;

    case '%rpi_io_chn':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "0"  : 17,
          "1"  : 18,
          "2"  : 22,
          "3"  : 27,
          "4"  : 23,
          "5"  : 24,
          "6"  : 25,
          "7"  : 4,
          "21" : 5,
          "22" : 6,
          "23" : 13,
          "24" : 19,
          "25" : 26,
          "26" : 12,
          "27" : 16,
          "28" : 20,
          "29" : 21,
        },
        false // read-only
      );
      break;
    default:
      nop();
  }
  return part
}
