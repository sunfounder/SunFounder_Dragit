class LiquidCrystal_I2C():
    # Commands
    LCD_CLEARDISPLAY   = 0x01
    LCD_RETURNHOME     = 0x02
    LCD_ENTRYMODESET   = 0x04
    LCD_DISPLAYCONTROL = 0x08
    LCD_CURSORSHIFT    = 0x10
    LCD_FUNCTIONSET    = 0x20
    LCD_SETCGRAMADDR   = 0x40
    LCD_SETDDRAMADDR   = 0x80

    # Flags for display entry mode
    LCD_ENTRYRIGHT = 0x00
    LCD_ENTRYLEFT  = 0x02
    LCD_ENTRYSHIFTINCREMENT = 0x01
    LCD_ENTRYSHIFTDECREMENT = 0x00

    # Flags for display on/off control
    LCD_DISPLAYON  = 0x04
    LCD_DISPLAYOFF = 0x00
    LCD_CURSORON   = 0x02
    LCD_CURSOROFF  = 0x00
    LCD_BLINKON    = 0x01
    LCD_BLINKOFF   = 0x00

    # Flags for display/cursor shift
    LCD_DISPLAYMOVE = 0x08
    LCD_CURSORMOVE  = 0x00
    LCD_MOVERIGHT   = 0x04
    LCD_MOVELEFT    = 0x00

    # Flags for function set
    LCD_8BITMODE = 0x10
    LCD_4BITMODE = 0x00
    LCD_2LINE    = 0x08
    LCD_1LINE    = 0x00
    LCD_5x10DOTS = 0x04
    LCD_5x8DOTS  = 0x00

    # Flags for backlight control
    LCD_BACKLIGHT   = 0x08
    LCD_NOBACKLIGHT = 0x00

    En = 0b00000100  # Enable bit
    Rw = 0b00000010  # Read/Write bit
    Rs = 0b00000001  # Register select bit

    import smbus
    import time

    def __init__(self, lcd_addr, lcd_cols, lcd_rows, bus_num=1):
        self._addr = lcd_addr
        self._cols = lcd_cols
        self._rows = lcd_rows
        self._bus_num = bus_num
        self._backlightval = self.LCD_NOBACKLIGHT

        self.bus = self.smbus.SMBus(self._bus_num)
        self._displayfunction = self.LCD_4BITMODE | self.LCD_1LINE | self.LCD_5x8DOTS
        self.begin(self._cols, self._rows)
        print('init finished!')

    def delay(self, ms):
        self.time.sleep(float(ms)/1000)

    def delayMicroseconds(self, us):
        self.delay(float(us)/1000)

    def begin(self, cols, lines, dotsize=0):
        if lines > 1:
            self._displayfunction |= self.LCD_2LINE
        self._numlines = lines

        # For some 1 line displays you can select a 10 pixel high font
        if dotsize != 0 and lines == 1:
            self._displayfunction |= self.LCD_5x10DOTS

        # SEE PAGE 45/46 FOR INITIALIZATION SPECIFICATION!
        # according to datasheet, we need at least 40ms after power rises above 2.7V
        # before sending commands. Arduino can turn on way befer 4.5V so we'll wait 50
        self.delay(50)

        # Now we pull both RS and R/W low to begin commands
        self.expanderWrite(self._backlightval)   # reset expanderand turn backlight off (Bit 8 =1)
        self.delay(1000)

        #put the LCD into 4 bit mode
        # this is according to the hitachi HD44780 datasheet
        # figure 24, pg 46

          # we start in 8bit mode, try to set 4 bit mode
        self.write4bits(0x03 << 4)
        self.delayMicroseconds(4500) # wait min 4.1ms

        # second try
        self.write4bits(0x03 << 4)
        self.delayMicroseconds(4500) # wait min 4.1ms

        # third go!
        self.write4bits(0x03 << 4)
        self.delayMicroseconds(150)

        # finally, set to 4-bit interface
        self.write4bits(0x02 << 4)


        # set # lines, font size, etc.
        self.command(self.LCD_FUNCTIONSET | self._displayfunction)

        # turn the display on with no cursor or blinking default
        self._displaycontrol = self.LCD_DISPLAYON | self.LCD_CURSOROFF | self.LCD_BLINKOFF
        self.display()

        # clear it off
        self.clear()

        # Initialize to default text direction (for roman languages)
        self._displaymode = self.LCD_ENTRYLEFT | self.LCD_ENTRYSHIFTDECREMENT

        # set the entry mode
        self.command(self.LCD_ENTRYMODESET | self._displaymode)

        self.home()

    # High level commands, for the user!
    def clear(self):
        self.command(self.LCD_CLEARDISPLAY)  # clear display, set cursor position to zero
        self.delayMicroseconds(2000)         # this command takes a long time!

    def home(self):
        self.command(self.LCD_RETURNHOME)   # set cursor position to zero
        self.delayMicroseconds(2000)        # this command takes a long time!

    def setCursor(self, col, row):
        row_offsets = [0x00, 0x40, 0x14, 0x54]
        if row > self._numlines - 1:
            row = self._numlines - 1    # we count rows starting w/0
        self.command(self.LCD_SETDDRAMADDR | (col + row_offsets[row]))

    # Turn the display on/off (quickly)
    def noDisplay(self):
        self._displaycontrol &= ~self.LCD_DISPLAYON
        self.command(self.LCD_DISPLAYCONTROL | self._displaycontrol)

    def display(self):
        self._displaycontrol |= self.LCD_DISPLAYON
        self.command(self.LCD_DISPLAYCONTROL | self._displaycontrol)

    # Turns the underline cursor on/off
    def noCursor(self):
        self._displaycontrol &= ~self.LCD_CURSORON
        self.command(self.LCD_DISPLAYCONTROL | self._displaycontrol)

    def cursor(self):
        self._displaycontrol |= self.LCD_CURSORON
        self.command(self.LCD_DISPLAYCONTROL | self._displaycontrol)


    # Turn on and off the blinking cursor
    def noBlink(self):
        self._displaycontrol &= ~self.LCD_BLINKON
        self.command(self.LCD_DISPLAYCONTROL | self._displaycontrol)

    def blink(self):
        self._displaycontrol |= self.LCD_BLINKON
        self.command(self.LCD_DISPLAYCONTROL | self._displaycontrol)


    # These commands scroll the display without changing the RAM
    def scrollDisplayLeft(self):
        self.command(self.LCD_CURSORSHIFT | self.LCD_DISPLAYMOVE | self.LCD_MOVELEFT)

    def scrollDisplayRight(self):
        self.command(self.LCD_CURSORSHIFT | self.LCD_DISPLAYMOVE | self.LCD_MOVERIGHT)

    # This is for text that flows Left to Right
    def leftToRight(self):
        self._displaymode |= self.LCD_ENTRYLEFT
        self.command(self.LCD_ENTRYMODESET | self._displaymode)

    # This is for text that flows Right to Left
    def rightToLeft(self):
        self._displaymode &= ~self.LCD_ENTRYLEFT
        self.command(self.LCD_ENTRYMODESET | self._displaymode)

    # This will 'right justify' text from the cursor
    def autoscroll(self):
        self._displaymode |= self.LCD_ENTRYSHIFTINCREMENT
        self.command(self.LCD_ENTRYMODESET | self._displaymode)

    # This will 'left justify' text from the cursor
    def noAutoscroll(self):
        self._displaymode &= ~self.LCD_ENTRYSHIFTINCREMENT
        self.command(self.LCD_ENTRYMODESET | self._displaymode)

    # Allows us to fill the first 8 CGRAM locations
    # with custom characters
    def createChar(self, location, charmap):
        location &= 0x7 # we only have 8 locations 0-7
        self.command(self.LCD_SETCGRAMADDR | (location << 3))
        for i in range(8):
            self.write(charmap[i])


    def printStr(self, string):
        for char in string:
            self.write(ord(char))

    def show(self, value):
        value = str(value)
        self.printStr(value)


    # Turn the (optional) backlight off/on
    def noBacklight(self):
        self._backlightval = self.LCD_NOBACKLIGHT
        self.expanderWrite(0);

    def backlight(self):
        self._backlightval = self.LCD_BACKLIGHT
        self.expanderWrite(0);

    # Mid level commands, for sending data/cmds
    def command(self, value):
        self.send(value, 0)

    # Low level data pushing commands

    # write either command or data
    def write(self, value):
        self.send(value, self.Rs)

    def send(self, value, mode):
        highnib = value & 0xf0
        lownib = (value<<4) & 0xf0
        self.write4bits((highnib)|mode)
        self.write4bits((lownib)|mode)

    def write4bits(self, value):
        self.expanderWrite(value)
        self.pulseEnable(value)

    def expanderWrite(self, _data):
        self.bus.write_byte(self._addr, int(_data) | self._backlightval)

    def pulseEnable(self, _data):
        self.expanderWrite(_data | self.En)  # self.En high
        self.delayMicroseconds(1)       # enable pulse must be >450ns

        self.expanderWrite(_data & ~self.En) # self.En low
        self.delayMicroseconds(50)      # commands need > 37us to settle


    # Alias functions
    def cursor_on(self):
        self.cursor()

    def cursor_off(self):
        self.noCursor()

    def blink_on(self):
        self.blink()

    def blink_off(self):
        self.noBlink()

    def load_custom_character(self, char_num, rows):
        self.createChar(char_num, rows)

    def setBacklight(self, new_val):
        if(new_val):
            self.backlight()        # turn backlight on
        else:
            self.noBacklight()      # turn backlight off

def main():
    lcd = LCD_I2C(0x27, 20, 4)
    lcd.backlight()                    # open the backlight 

    lcd.setCursor(0, 0)                # Go to the top left corner
    lcd.show("    Hello,world!    ")  # Write this string on the top row
    lcd.setCursor(0, 1)                # Go to the 2nd row
    lcd.show("   IIC/I2C LCD2004  ")  # Pad string with spaces for centering
    lcd.setCursor(0, 2)                # Go to the third row
    lcd.show("  20 cols, 4 rows   ")  # Pad with spaces for centering
    lcd.setCursor(0, 3)                # Go to the fourth row
    lcd.show(" www.sunfounder.com ")

if __name__ == '__main__':
    main()
