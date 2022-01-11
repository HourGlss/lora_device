import board
import busio
import time
import json

from reyax.rylr896 import RYLR896
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from states import MainMenu,SendMenu
from lcd.lcd import CursorMode


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


lcd.set_backlight(False)
reset_lcd(lcd)
txpin = board.GP4
rxpin = board.GP5
lora = RYLR896(name="lora", rx=rxpin, tx=txpin, timeout=1, debug=True)
lora.set_address(15)
txpin2 = board.GP12
rxpin2 = board.GP13
lorb = RYLR896(name="lorb", rx=rxpin2, tx=txpin2, timeout=1, debug=True)
lorb.set_address(13)
time.sleep(1)
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


from fake_rylr896 import RYLR896
from fake_lcd import FakeLCD
from states import MainMenu
from device import Device

import keyboard
import logging
import inspect
import sys
import os

log_file = "runlog.log"

file_exists = os.path.exists(log_file)
if file_exists:
    os.remove(log_file)
FORMAT = "[{%(levelname)s} %(filename)s:%(lineno)s 	- %(funcName)20s() ] %(message)s"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format=FORMAT)

class Driver:

    def __init__(self):
        pass
    def main(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug("main called")
        txpin = "GP4"
        rxpin = "GP5"
        lora = RYLR896(name="lora", rx=rxpin, tx=txpin, timeout=1, debug=True)
        lcd = FakeLCD(width=20,height=4)

        d = Device(lcd,lora)
        current_state = MainMenu(d)
        while True:
            state_change = False

        # check lora to see if received
            d.get_message()
        # get keyboard input
            kbi = d.get_keyboard_input()
            if kbi is not None:
                current_state.use_keyboard_input(kbi)
        # check state
            state = current_state.get_next_state()
            if state.__class__.__name__ != current_state.__class__.__name__:
                state_change = True
                current_state = state
                del state
        # update screen
            if d.lcd_event_change_detected:
                current_state.screen()
                d.print_screen()
        # if the state has changed allow the state to set some things up initially after the first draw
            if state_change:
                current_state.initial()
        # Quit for only windows version
            if keyboard.is_pressed('`'):
                sys.exit()

if __name__ == "__main__":
    D = Driver()
    D.main()