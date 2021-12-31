import board
import busio
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

from lcd.lcd import CursorMode
from reyax.rylr896 import RYLR896


def reset_lcd(this_lcd):
    this_lcd.clear()
    this_lcd.set_cursor_pos(0, 0)


lcd_i2c = busio.I2C(scl=board.GP1, sda=board.GP0)
# Talk to the LCD at I2C address 0x27.
# The number of rows and columns defaults to 4x20, so those
# arguments could be omitted in this case.
lcd = LCD(I2CPCF8574Interface(lcd_i2c, 0x27), num_rows=4, num_cols=20)

# lcd.set_cursor_mode(CursorMode.LINE)
### LCD SPECIAL CHARACTERS ###
# RIGHT ARROW = ~
# LEFT ARROW = ''
# SETUP STUFF TO PRINT

start = 32
end = 500
to_print = [chr(i) for i in range(start, end)]
# LOOP THROUGH IT
for i in range(0, len(to_print) + 80, 80):
    start_on_screen = i
    end_on_screen = i + 80
    if end_on_screen >= len(to_print):
        end_on_screen = len(to_print) - 1
    # RESET LCD
    lcd.clear()
    lcd.set_cursor_pos(0, 0)
    # PRINT STUFF
    to_send = "".join(to_print[start_on_screen:end_on_screen])
    for index in range(0, len(to_send), 20):
        print(to_send[index:index + 20])
    lcd.print(to_send)

    # WAIT
    time.sleep(20)

# Make the cursor visible as a line.
#

lcd.set_backlight(True)
reset_lcd(lcd)
print("Setting up")
txpin = board.GP4
rxpin = board.GP5
lora = RYLR896(name="lora", rx=rxpin, tx=txpin, timeout=1, debug=True)
lora.set_address(15)
txpin2 = board.GP12
rxpin2 = board.GP13
lorb = RYLR896(name="lorb", rx=rxpin2, tx=txpin2, timeout=1, debug=True)
lorb.set_address(13)
time.sleep(1)
print("Sending")
lora.send(data="Hello world!", address=13)
time.sleep(1)
data = None

while True:
    data = lorb.uart.read()
    if data is not None:
        break

reset_lcd(lcd)
print(data)
time.sleep(2)
reset_lcd(lcd)
print("Done")

import time
import board
import busio
from digitalio import DigitalInOut, Direction, Pull

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

from lcd.lcd import CursorMode

row0 = DigitalInOut(board.GP6)
row0.direction = Direction.INPUT
row0.pull = Pull.DOWN

row1 = DigitalInOut(board.GP8)
row1.direction = Direction.INPUT
row1.pull = Pull.DOWN

col0 = DigitalInOut(board.GP7)
col0.direction = Direction.OUTPUT
col0.value = False

col1 = DigitalInOut(board.GP9)
col1.direction = Direction.OUTPUT
col1.value = False

# lcd_i2c = busio.I2C(scl=board.GP1, sda=board.GP0)
# lcd = LCD(I2CPCF8574Interface(lcd_i2c, 0x27), num_rows=4, num_cols=20)
# lcd.set_backlight(False)

cols = [col0, col1]
rows = [row0, row1]

keys_input = {0: {0: False, 1: False}, 1: {0: False, 1: False}}
keys_dict = {0: {0: "c", 1: "a"}, 1: {0: "d", 1: "b"}}
while True:
    c = 0
    for cpin in cols:
        r = 0
        cpin.value = True
        for rpin in rows:
            if rpin.value:
                # print("SOMETHING")
                keys_input[c][r] = True
            time.sleep(0.01)
            r += 1
        c += 1
        cpin.value = False
    # print("======")
    for x, v in keys_input.items():
        for y, data in v.items():
            # print("x {}".format(x))
            # print("y {}".format(y))
            # print("v {}".format(v))
            # print("data {}".format(data))
            if keys_input[x][y]:
                print("---> {}".format(keys_dict[x][y]))
    keys_input = {0: {0: False, 1: False}, 1: {0: False, 1: False}}

import time
import board
import busio
import pulseio
import pwmio
from reyax.rylr896 import RYLR896
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode

row0 = DigitalInOut(board.GP6)
row0.direction = Direction.INPUT
row0.pull = Pull.DOWN

row1 = DigitalInOut(board.GP8)
row1.direction = Direction.INPUT
row1.pull = Pull.DOWN

row2 = DigitalInOut(board.GP10)
row2.direction = Direction.INPUT
row2.pull = Pull.DOWN

row3 = DigitalInOut(board.GP11)
row3.direction = Direction.INPUT
row3.pull = Pull.DOWN

slow_switch_in = DigitalInOut(board.GP13)
slow_switch_in.direction = Direction.INPUT
slow_switch_in.pull = Pull.DOWN

slow_switch_out = DigitalInOut(board.GP12)
slow_switch_out.direction = Direction.OUTPUT
slow_switch_out.value = True
slow = None
if slow_switch_in.value:
    slow = True
else:
    slow = False
print("Slow is {}".format(slow))

buzzer = pwmio.PWMOut(board.GP14, duty_cycle=2 ** 15, frequency=440, variable_frequency=True)

buzzer.frequency = 550

col0 = DigitalInOut(board.GP7)
col0.direction = Direction.OUTPUT
col0.value = False

col1 = DigitalInOut(board.GP9)
col1.direction = Direction.OUTPUT
col1.value = False

led = DigitalInOut(board.GP15)
led.direction = Direction.OUTPUT
led.value = False

lcd_i2c = busio.I2C(scl=board.GP1, sda=board.GP0)
lcd = LCD(I2CPCF8574Interface(lcd_i2c, 0x27), num_rows=4, num_cols=20)
lcd.set_backlight(False)

cols = [col0, col1]
rows = [row0, row1, row2, row3]

keys_actual_input = {'a':False,'b':False}

keys_input = {0: {0: False, 1: False, 2: False, 3: False}, 1: {0: False, 1: False, 2: False, 3: False}}
keys_dict = {0: {0: "c", 1: "a", 2: "W", 3: "N"}, 1: {0: "d", 1: "b", 2: "S", 3: "E"}}
'''
while True:
    led.value = True
    c = 0
    for cpin in cols:
        r = 0
        cpin.value = True
        for rpin in rows:
            if rpin.value:
                #print("SOMETHING")
                keys_input[c][r] = True
            if slow:
                time.sleep(.1)
            else:
                time.sleep(.01)
            r += 1
        c += 1
        cpin.value = False
    led.value = False
    #print("======")

    for x, v in keys_input.items():
        for y, data in v.items():
            if slow:

                time.sleep(.1)
            #print("x {}".format(x))
            #print("y {}".format(y))
            #print("v {}".format(v))
            #print("data {}".format(data))
            if keys_input[x][y]:
                lcd.print(keys_dict[x][y])
                if keys_dict[x][y] == "W":
                    buzzer.frequency = 333
                if keys_dict[x][y] == "E":
                    buzzer.frequency = 294
                if keys_dict[x][y] == "S":
                    buzzer.frequency = 349
                if keys_dict[x][y] == "N":
                    buzzer.frequency = 262
                if keys_dict[x][y] == "a":
                    buzzer.frequency = 392
                if keys_dict[x][y] == "b":
                    buzzer.frequency = 440
                if keys_dict[x][y] == "c":
                    buzzer.frequency = 494
                if keys_dict[x][y] == "d":
                    buzzer.frequency = 523

    keys_input = {0: {0: False, 1: False}, 1: {0: False, 1: False}}
'''
'''
lora = RYLR896(rx=board.GP5,tx=board.GP4,name="lora",debug=True,timeout=.05)
lora.set_address(50)
lora.set_rf_parameters(12,9,4,7)

while True:
    data = None
    data = lora.uart.read()
    if data is not None:
        print(data)
'''
