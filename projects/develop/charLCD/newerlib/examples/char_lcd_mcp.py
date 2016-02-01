#!/usr/bin/python
# Example using an RGB character LCD connected to an MCP23017 GPIO extender.
import time

print "char_lcd_mcp.py import CharLCD"
import Adafruit_CharLCD as LCD
print "char_lcd_mcp.py import MCP230xx"
import Adafruit_GPIO.MCP230xx as MCP


# Define MCP pins connected to the LCD.
lcd_rs        = 0
lcd_en        = 1
lcd_d4        = 2
lcd_d5        = 3
lcd_d6        = 4
lcd_d7        = 5
lcd_red       = 6
lcd_green     = 7
lcd_blue      = 8

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Alternatively specify a 20x4 LCD.
# lcd_columns = 20
# lcd_rows    = 4

# Initialize MCP23017 device using its default 0x20 I2C address.
print "char_lcd_mcp.py init gpio"
gpio = MCP.MCP23017()

# Alternatively you can initialize the MCP device on another I2C address or bus.
# gpio = MCP.MCP23017(0x24, busnum=1)

# Initialize the LCD using the pins 
lcd = LCD.Adafruit_RGBCharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, 
							lcd_columns, lcd_rows, lcd_red, lcd_green, lcd_blue, gpio=gpio)

# Print a two line message
print 'sending Hello world! to LCD'
lcd.message('Hello\nworld!')

# Wait 5 seconds
time.sleep(2.0)

# Demo showing the cursor.
print 'Show cursor'
lcd.clear()
lcd.show_cursor(True)
lcd.message('Show cursor')

time.sleep(2.0)

# Demo showing the blinking cursor.
print 'Blink cursor'
lcd.clear()
lcd.blink(True)
lcd.message('Blink cursor')

time.sleep(2.0)

# Stop blinking and showing cursor.
lcd.show_cursor(False)
lcd.blink(False)

# Demo scrolling message right/left.
lcd.clear()
message = 'Scroll'
lcd.message(message)
print 'Scroll right'
for i in range(lcd_columns-len(message)):
	time.sleep(0.3)
	lcd.move_right()
print 'Scroll left'
for i in range(lcd_columns-len(message)):
	time.sleep(0.3)
	lcd.move_left()

# Demo turning backlight off and on.
print 'Flash backlight'
lcd.clear()
lcd.message('Flash backlight\nin 5 seconds...')
time.sleep(2.0)
# Turn backlight off.
print 'backlight off'
lcd.set_backlight(0)
time.sleep(2.0)
# Change message.
lcd.clear()
lcd.message('Goodbye!')
# Turn backlight on.
lcd.set_backlight(1)
