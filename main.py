from fake_rylr896 import RYLR896
from fake_lcd import FakeLCD
from state.main_menu import MainMenu
from device import Device

import keyboard
import logging
import inspect
import sys

FORMAT = "[{%(levelname)s} %(filename)s:%(lineno)s 	- %(funcName)20s() ] %(message)s"
logging.basicConfig(filename='runlog.log', level=logging.INFO, format=FORMAT)

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
        # check lora to see if received
            d.get_message()
        # get keyboard input
            kbi = d.get_keyboard_input()
            if kbi is not None:
                current_state.use_keyboard_input(kbi)
        # check state
            state = current_state.get_next_state()
            if state is not None:
                current_state = state
                del state
        # update screen
            if d.lcd_event_change_detected:
                current_state.screen()
                d.print_screen()
            if keyboard.is_pressed('`'):
                sys.exit()

if __name__ == "__main__":
    D = Driver()
    D.main()
