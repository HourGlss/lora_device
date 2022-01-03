from state.state import AbstractState
from state.send_menu import SendMenu
from state.received_menu import ReceivedMenu
from state.settings_menu import SettingsMenu

class MainMenu(AbstractState):

    def __init__(self, d):
        super().__init__(d)

    def get_next_state(self):
        if self.nextState is None:
            return self
        else:
            return self.nextState

    def use_keyboard_input(self, kb):
        if kb['enter']:
            self.on_enter()
        if kb['left']:
            self.on_left()
        if kb['right']:
            self.on_right()
        if kb['up']:
            self.on_up()
        if kb['down']:
            self.on_down()
        if kb['esc']:
            self.exit()


    def print_input_buffer(self):
        pass


    def screen(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug("changing device.next_screen")
        menu = ("* Send", "* Messages", "* Settings")
        self.device.next_screen = ""
        for item in menu:
            self.device.next_screen += "{:<20}".format(item)

    def on_enter(self):
        # checks if the the cursor is at 0,0
        if self.device.row == 0 and self.device.col == 0:
            # transitions to the send_new state
            self.nextState = SendMenu
        # checks if the the cursor is at 1,0
        if self.device.row == 1 and self.device.col == 0:
            # transitions to the received_menu state
            self.nextState = ReceivedMenu
        # checks if the the cursor is at 2,0
        if self.device.row == 2 and self.device.col == 0:
            # transitions to the received_menu state
            self.nextState = SettingsMenu
        else:
            print('Error, enter on valid option')

    def write_char(self, c):
        pass

    def delete(self):
        pass
