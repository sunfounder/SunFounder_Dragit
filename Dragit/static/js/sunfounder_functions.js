var myDate = new Date();
current_datetime = {
  'year' : myDate.getFullYear(),
  'mon'  : myDate.getMonth()+1,
  'day'  : myDate.getDate(),
  'hour' : myDate.getHours(),
  'min'  : myDate.getMinutes(),
  'sec'  : myDate.getSeconds()
}

SpriteMorph.prototype.loadSunFounderCategories = function(blocks, block, watcherToggle, cat){
  if (cat === 'PiCar_V') {
    this.loadPiCarVCategories(blocks, block, watcherToggle);
  }
  else if (cat === 'PiCar_S') {
    this.loadPiCarSCategories(blocks, block, watcherToggle);
  }
  else if (cat === 'RaspberryPi') {
    this.loadRaspberryPiCategories(blocks, block, watcherToggle);
  }
  else if (cat === 'PiSmart') {
    this.loadPiSmartCategories(blocks, block, watcherToggle);
  }
  else if (cat === 'Modules') {
    this.loadModulesCategories(blocks, block, watcherToggle);
  }
  else if (cat === 'PiPlus') {
    this.loadPiPlusCategories(blocks, block, watcherToggle);
  }
}

function requests(device, action, value0=null, value1=null, value2=null, value3=null, value4=null){
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
  if (value3 != null){
    url = url + "&value3=" + value3;
  }
  if (value4 != null){
    url = url + "&value4=" + value4;
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

    case '%pismart_motor_chn':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          'A' : ['A'],
          'B' : ['B'],
          'both' : ['both']
        },
        true // read-only
      );
      break;

    case '%sf_cam_dir':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          'up'    : ['up'],
          'down'  : ['down'],
          'left'  : ['left'],
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
          'on'  : ['on'],
          'off' : ['off'],
        },
        true // read-only
      );
      break;

    case '%sf_cw_ccw':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          'cw'  : ['cw'],
          'ccw' : ['ccw'],
        },
        true // read-only
      );
      break

    case '%sf_fw_dir':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          'straight' : ['straight'],
          'left'     : ['left'],
          'right'    : ['right']
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
          '0'  : [0],
          '1'  : [1],
          '2'  : [2],
          '3'  : [3],
          '4'  : [4],
          '5'  : [5],
          '6'  : [6],
          '7'  : [7],
          '8'  : [8],
          '9'  : [9],
          '10' : [10],
          '11' : [11],
          '12' : [12],
          '13' : [13],
          '14' : [14],
          '15' : [15],
        },
        false // read-only
      );
      break;

    case '%pismart_pwm_chn':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          '0' : [0],
          '1' : [1],
          '2' : [2],
          '3' : [3],
          '4' : [4],
          '5' : [5],
          '6' : [6],
          '7' : [7],
        },
        true // read-only
      );
      break;

    case '%sf_Achn':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          '0' : [0],
          '1' : [1],
          '2' : [2],
          '3' : [3],
        },
        true // read-only
      );
      break;

    case '%pismart_Achn':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          '0' : [0],
          '1' : [1],
          '2' : [2],
          '3' : [3],
          '4' : [4]
        },
        true // read-only
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
        true // read-only
      );
      break;

    case '%pismart_Dchn':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "0" : [0],
          "1" : [1],
          "2" : [2],
          "3" : [3],
          "4" : [4],
          "5" : [5],
          "6" : [6],
          "7" : [7]
        },
        true // read-only
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
        true // read-only
      );
      break;

    case '%rpi_gpio_chn':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "0"  : [0],
          "1"  : [1],
          "2"  : [2],
          "3"  : [3],
          "4"  : [4],
          "5"  : [5],
          "6"  : [6],
          "7"  : [7],
          "21" : [21],
          "22" : [22],
          "23" : [23],
          "24" : [24],
          "25" : [25],
          "26" : [26],
          "27" : [27],
          "28" : [28],
          "29" : [29],
        },
        true // read-only
      );
      break;

    case '%rpi_busnum':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "0"  : [0],
          "1"  : [1],
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
        true // read-only
      );
      break;

    case '%lt_index_chn':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "0"  : [0],
          "1"  : [1],
          "2"  : [2],
        },
        true // read-only
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

    case '%D_state':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "HIGH" : "HIGH",
          "LOW"  : "LOW"
        },
        true // read-only
      );
      break;

    case '%pcf8591_ain':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "AIN0"  : "AIN0",
          "AIN1"  : "AIN1",
          "AIN2"  : "AIN2",
          "AIN3"  : "AIN3"
        },
        true // read-only
      );
      break;

    case '%pcf8591_addr':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "0x48"  : '0x48',
          "0x49"  : '0x49',
          "0x4A"  : '0x4A',
          "0x4B"  : '0x4B',
          "0x4C"  : '0x4C',
          "0x4D"  : '0x4D',
          "0x4E"  : '0x4E',
          "0x4F"  : '0x4F'
        },
        true // read-only
      );
      break;

    case '%joystick_ps2_pin':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "X"  : "X",
          "Y"  : "Y",
          "Bt" : "Bt"
        },
        true // read-only
      );
      break;

    case '%unit':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "c"  : "c",
          "f"  : "f"
        },
        true // read-only
      );
      break;

    case '%week':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "mon."  : "mon.",
          "tue."  : "tue.",
          "wed."  : "wed.",
          "thu."  : "thu.",
          "fri."  : "fri.",
          "sat."  : "sat.",
          "sun."  : "sun.",
        },
        true // read-only
      );
      break;

    case '%col_1602':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "0"  : [0],
          "1"  : [1],
          "2"  : [2],
          "3"  : [3],
          "4"  : [4],
          "5"  : [5],
          "6"  : [6],
          "6"  : [6],
          "7"  : [7],
          "8"  : [8],
          "9"  : [9],
          "10" : [10],
          "11" : [11],
          "12" : [12],
          "13" : [13],
          "14" : [14],
          "15" : [15],
        },
        true // read-only
      );
      break;

    case '%row_1602':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "0"  : [0],
          "1"  : [1],
        },
        true // read-only
      );
      break;

    case '%col_2004':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "0"  : [0],
          "1"  : [1],
          "2"  : [2],
          "3"  : [3],
          "4"  : [4],
          "5"  : [5],
          "6"  : [6],
          "6"  : [6],
          "7"  : [7],
          "8"  : [8],
          "9"  : [9],
          "10" : [10],
          "11" : [11],
          "12" : [12],
          "13" : [13],
          "14" : [14],
          "15" : [15],
          "16" : [16],
          "17" : [17],
          "18" : [18],
          "19" : [19],
        },
        true // read-only
      );
      break;

    case '%row_2004':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "0"  : [0],
          "1"  : [1],
          "2"  : [2],
          "3"  : [3],
        },
        true // read-only
      );
      break;

    case '%RGBcolors':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "red"    : '0xFF0000',
          "green"  : '0x00FF00',
          "blue"   : '0x0000FF',
          "yellow" : '0xFFFF00',
          "purple" : '0xFF00FF',
          "cyan"   : '0x00FFFF',
          "white"  : '0xFFFFFF',
        },
        false // read-only
      );
      break;

    case '%common_polarity':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "cathode" : "cathode",
          "anode"   : "anode",
        },
        true // read-only
      );
      break;

    case '%DUALcolors':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "red"   : "red",
          "green" : "green",
          "off"   : "off",
        },
        true // read-only
      );
      break;

    case '%buzzer':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "beep" : 'beep',
          "off"  : 'off',
        },
        false // read-only
      );
      break;

    case '%dht_mode':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "temperature C" : 'temperature C',
          "temperature F" : 'temperature F',
          "humidity"  : 'humidity',
        },
        true // read-only
      );
      break;

    case '%mpu6050_item':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "gyroscope x"    : 'gyroscope x',
          "gyroscope y"    : 'gyroscope y',
          "gyroscope z"    : 'gyroscope z',
          "acceleration x" : 'acceleration x',
          "acceleration y" : 'acceleration y',
          "acceleration z" : 'acceleration z',
          "x rotation"     : 'x rotation',
          "y rotation"     : 'y rotation',
        },
        true // read-only
      );
      break;

    case '%bmp280_item':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "temperature" : 'temperature',
          "pressure"    : 'pressure',
        },
        true // read-only
      );
      break;

    case '%rtc_ds1302_item':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "year"  : 'year',
          "month" : 'month',
          "day"   : 'day',
          "hour"  : 'hour',
          "minute": 'minute',
          "second": 'second',
        },
        true // read-only
      );
      break;

    case '%remoteKey':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "power"     : 'power',
          "mode"      : 'mode',
          "mute"      : 'mute',
          "playpause" : 'playpause',
          "previous"  : 'previous',
          "next"      : 'next',
          "-"         : '-',
          "+"         : '+',
          "EQ"        : 'EQ',
          "0"         : '0',
          "1"         : '1',
          "2"         : '2',
          "3"         : '3',
          "4"         : '4',
          "5"         : '5',
          "6"         : '6',
          "7"         : '7',
          "8"         : '8',
          "9"         : '9',
          "swap"      : 'swap',
          "u/sd"      : 'u/sd',
        },
        true // read-only
      );
      break;

    case '%chkbx':
      part = new CheckboxSlotMorph();
      part.isStatic = true;
      break;

    case '%buzzer_note':
      part = new InputSlotMorph(
        null, // text
        false, // numeric?
        {
          "C"  : 'C',
          "D"  : 'D',
          "E"  : 'E',
          "F"  : 'F',
          "G"  : 'G',
          "A"  : 'A',
          "B"  : 'B',
          "C2" :'C2',
        },
        true // read-only
      );
      break;

    case '%piplus_port':
      part = new InputSlotMorph(
        null,  // text
        false, // numeric?
        {
          'A' : 'A',
          'B' : 'B',
          //'Analog Port'    : 'Analog Port',
          //'Communication Port' : 'Communication Port',
        },
        true   // read-only
      );
      break;

    case '%piplus_morse_speed':
      part = new InputSlotMorph(
        null,  // text
        false, // numeric?
        {
          'fast' : 'fast',
          'slow' : 'slow',
          //'Analog Port'    : 'Analog Port',
          //'Communication Port' : 'Communication Port',
        },
        true   // read-only
      );
      break;

    case '%piplus_ring_style':
      part = new InputSlotMorph(
        null,  // text
        false, // numeric?
        {
          'ALL_BRIGHT' : 'ALL_BRIGHT',
          'ALL_DIM' : 'ALL_DIM',
          'ALL_OFF' : 'ALL_OFF',
          'SINGLE'  : 'SINGLE',
          'STAR'    : 'STAR',
          'ARC'     : 'ARC',
        },
        true   // read-only
      );
      break;

    case '%piplus_slide':
      part = new InputSlotMorph(
        null,  // text
        false, // numeric?
        {
          'sp1' : 'sp1',
          'sp2' : 'sp2',
          'sp3' : 'sp3',
        },
        true   // read-only
      );
      break;

    case '%datetime_names':
      part = new InputSlotMorph(
        null,  // text
        false, // numeric?
        {
          'year'         :'year',
          'month'        :'month',
          'day of month' :'day of month',
          'hour'         :'hour',
          'minute'       :'minute',
          'second'       :'second',
          'weekday'      :'weekday',
          'day of year'  :'day of year'
        },
        true   // read-only
      );
      break;

    default:
      nop();
  }
  return part
}


// CheckboxSlotMorph //////////////////////////////////////////////////////

/*
    my block spec is %chkbx
*/

// CheckboxSlotMorph  inherits from ArgMorph:

CheckboxSlotMorph.prototype = new ArgMorph();
CheckboxSlotMorph.prototype.constructor = CheckboxSlotMorph;
CheckboxSlotMorph.uber = ArgMorph.prototype;

// CheckboxSlotMorph  instance creation:

function CheckboxSlotMorph(flag) {
  this.init(flag);
}

CheckboxSlotMorph.prototype.init = function (flag) {
    this.flag = flag
    CheckboxSlotMorph.uber.init.call(this, null, true); // silently
    if (this.flag)
        this.setColor(new Color(225, 225, 225));
    else
        this.flag = false
        this.setColor(new Color(35, 35, 35));
};

CheckboxSlotMorph.prototype.getSpec = function () {
    return '%chkbx';
};

CheckboxSlotMorph.prototype.setContents = function (flag) {
    this.flag = flag;
};

// CheckboxSlotMorph  color sensing:
CheckboxSlotMorph.prototype.mouseClickLeft = function () {
    var myself = this,
        world = this.world(),
        hand = world.hand;
    this.flag = !this.flag;
    if (this.flag)
        this.setColor(new Color(225, 225, 225));
    else
        this.setColor(new Color(35, 35, 35));
};

// CheckboxSlotMorph evaluating:

CheckboxSlotMorph.prototype.evaluate = function () {
    return this.flag;
};

// CheckboxSlotMorph drawing:

CheckboxSlotMorph.prototype.drawNew = function () {
    var context, borderColor, side;

    side = this.fontSize + this.edge * 2 + this.typeInPadding * 2;
    this.silentSetExtent(new Point(side, side));

    // initialize my surface property
    this.image = newCanvas(this.extent());
    context = this.image.getContext('2d');
    if (this.parent) {
        borderColor = this.parent.color;
    } else {
        borderColor = new Color(120, 120, 120);
    }
    context.fillStyle = this.color.toString();

    // cache my border colors
    this.cachedClr = borderColor.toString();
    this.cachedClrBright = borderColor.lighter(this.contrast)
        .toString();
    this.cachedClrDark = borderColor.darker(this.contrast).toString();

    context.fillRect(
        this.edge,
        this.edge,
        this.width() - this.edge * 2,
        this.height() - this.edge * 2
    );
    if (!MorphicPreferences.isFlat) {
        this.drawRectBorder(context);
    }
};

CheckboxSlotMorph.prototype.drawRectBorder =
    InputSlotMorph.prototype.drawRectBorder;
