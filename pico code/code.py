from states import MainMenu, SendMenu
from device import Device
import busio
import board
import time

from digitalio import DigitalInOut, Direction

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from reyax.rylr896 import RYLR896


class Driver(object):
    def __init__(self):
        pass


    def main(self):
        lcd_i2c = busio.I2C(scl=board.GP1, sda=board.GP0)
        lcd = LCD(I2CPCF8574Interface(lcd_i2c, 0x27), num_rows=4, num_cols=20)
        lcd.set_backlight(True)
        lora = RYLR896(rx=board.GP5, tx=board.GP4, name="lora", debug=True)
        d = Device(lcd, lora)
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

    def test_led_bulb(self):
        test_led = DigitalInOut(board.GP15)
        test_led.direction = Direction.OUTPUT
        while True:
            print("light on")
            test_led.value = True
            time.sleep(1)
            print("light off")
            test_led.value = False
            time.sleep(1)


if __name__ == "__main__":
    D = Driver()
    D.main()
