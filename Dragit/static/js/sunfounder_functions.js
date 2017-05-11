
SpriteMorph.prototype.loadSunFounderCategories = function(blocks, block, watcherToggle, cat){
  if (cat === 'PiCar_V') {
    this.loadPiCarVCategories(blocks, block, watcherToggle);
  }
  if (cat === 'PiCar_S') {
    this.loadPiCarSCategories(blocks, block, watcherToggle);
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

    case '%sf_cam_dir':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          'up' : ['up'],
          'down' : ['down'],
          'left' : ['left'],
          'center' : ['center'],
          'right' : ['right']
        },
        true // read-only
      );
      break;

    case '%sf_io_state':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          'HIGH' : ['HIGH'],
          'LOW'  : ['LOW']
        },
        true // read-only
      );
      break;

    case '%sf_on_off':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          'on' : ['on'],
          'off'  : ['off']
        },
        true // read-only
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
        true // read-only
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
        true // read-only
      );
      break;

    case '%sf_pwm_chn':
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

    case '%sf_Achn':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          '0' : 0,
          '1' : 1,
          '2' : 2,
          '3' : 3
        },
        false // read-only
      );
      break;

    case '%sf_Dchn':
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

    case '%sf_picarv_cali':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "front wheel" : ["front wheel"],
          "left wheel" : ["left wheel"],
          "right wheel" : ["right wheel"],
          "pan" : ["pan"],
          "tilt" : ["tilt"]
        },
        true // read-only
      );
      break;

    case '%sf_picars_cali':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "front wheel" : ["front wheel"],
          "left wheel" : ["left wheel"],
          "right wheel" : ["right wheel"]
        },
        true // read-only
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
          "0 (BCM 17)"  : 17,
          "1 (BCM 18)"  : 18,
          "2 (BCM 22)"  : 22,
          "3 (BCM 27)"  : 27,
          "4 (BCM 23)"  : 23,
          "5 (BCM 24)"  : 24,
          "6 (BCM 25)"  : 25,
          "7 (BCM 4)"  : 4,
          "21 (BCM 5)"  : 5,
          "22 (BCM 6)"  : 6,
          "23 (BCM 13)"  : 13,
          "24 (BCM 19)"  : 19,
          "25 (BCM 26)"  : 26,
          "26 (BCM 12)"  : 12,
          "27 (BCM 16)"  : 16,
          "28 (BCM 20)"  : 20,
          "29 (BCM 21)"  : 21,
        },
        false // read-only
      );
      break;

    case '%rpi_busnum':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "0"  : 0,
          "1"  : 1
        },
        true // read-only
      );
      break;

    case '%lf_index_chn':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "1"  : 1,
          "2"  : 2,
          "3"  : 3,
          "4"  : 4,
          "5"  : 5,
        },
        false // read-only
      );
      break;

    case '%lt_index_chn':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "0"  : 0,
          "1"  : 1,
          "2"  : 2,
        },
        false // read-only
      );
      break;

    case '%sf_0_1':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "0"  : "0",
          "1"  : "1"
        },
        true // read-only
      );
      break;

    default:
      nop();
  }
  return part
}
