'''
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

from lcd.lcd import CursorMode

lcd_i2c = busio.I2C(scl=board.GP1, sda=board.GP0)

# Talk to the LCD at I2C address 0x27.
# The number of rows and columns defaults to 4x20, so those
# arguments could be omitted in this case.
lcd = LCD(I2CPCF8574Interface(lcd_i2c, 0x27), num_rows=4, num_cols=20)
lcd.set_backlight(False)
lcd.print("abc ")
lcd.print("This is quite long and will wrap onto the next line automatically.")
time.sleep(5)
lcd.clear()

# Start at the second line, fifth column (numbering from zero).
lcd.set_cursor_pos(1, 4)
lcd.print("Here I am")

# Make the cursor visible as a line.
lcd.set_cursor_mode(CursorMode.LINE)
'''
import time
import busio
import board


txpin = board.GP12
rxpin = board.GP13

from reyax.rylr896 import RYLR896
lora = RYLR896(rx=rxpin,tx=txpin)
print("ya")
