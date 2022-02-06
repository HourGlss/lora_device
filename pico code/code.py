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

    def main(self, repeater=False):
        lcd_i2c = busio.I2C(scl=board.GP1, sda=board.GP0)
        lcd = LCD(I2CPCF8574Interface(lcd_i2c, 0x27), num_rows=4, num_cols=20)
        lcd.set_backlight(True)
        lora = RYLR896(rx=board.GP5, tx=board.GP4, name="lora")
        lora.lazy_config(address=5, network_id=5, parameters=(10, 7, 1, 7))
        d = Device(lcd, lora, kbsda=board.GP18, kbscl=board.GP19)
        current_state = MainMenu(d)
        while True:
            state_change = False
            # check lora to see if received
            if repeater is True:
                data_in = lora.read_from_device()
                lora.send(data_in["actual_data"], 5)
            else:
                d.get_message()
            # get keyboard input
            if d.use_i2c_kb:
                kbi = d.get_i2c_keyboard_input()
            else:
                kbi = d.get_keyboard_input()
            if kbi is not None:
                current_state.use_keyboard_input(kbi)
            # check state
            state = current_state.get_next_state()
            if state.__class__.__name__ != current_state.__class__.__name__:
                state_change = True
                current_state = state
                del state
            # if the state has changed allow the state to set some things up initially after the first draw
            if state_change:
                current_state.initial()
            # update screen
            if d.lcd_event_change_detected:
                current_state.screen()
                d.print_screen()

    def test_led_bulb(self):
        test_led = DigitalInOut(board.GP15)
        test_led.direction = Direction.OUTPUT
        while True:
            test_led.value = True
            time.sleep(1)
            print("light off")
            test_led.value = False
            time.sleep(1)





if __name__ == "__main__":
    D = Driver()
    D.main()
