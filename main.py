from fake_rylr896 import RYLR896
from fake_lcd import Fake_lcd as LCD
from state.main_menu import MainMenu
from device import Device


txpin = "GP4"
rxpin = "GP5"
lora = RYLR896(name="lora", rx=rxpin, tx=txpin, timeout=1, debug=True)
lcd = LCD()

d = Device(lcd,lora)
current_state = MainMenu(d)
while True:
# check lora to see if received
    d.get_message()
# get keyboard input
    kbi = d.get_keyboard_input()
    current_state.use_keyboard_input(kbi)
# check state
    state = current_state.get_next_state()
    if state is not None:
        current_state = state(d)
# update screen
    current_state.update_screen()

