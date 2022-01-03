from state.state import AbstractState
from state.send_menu import SendMenu
from state.received_menu import ReceivedMenu
from state.settings_menu import SettingsMenu
import inspect
import logging

class MainMenu(AbstractState):

    def __init__(self, d):
        super().__init__(d)
        self.device.function_toggle = False
        self.device.next_cursor_row = 0
        self.device.next_cursor_col = 0
        self.lowest_row = 2
        self.device.toggle_lcd_event_flag()

    def get_next_state(self):
        if self.nextState is None:
            return self
        else:
            return self.nextState

    def use_keyboard_input(self, kb):
        func = inspect.currentframe().f_back.f_code
        if kb['s']:
            self.on_down()
            return
        if kb['w']:
            self.on_up()
            return
        if kb['enter']:
            self.on_enter()
            return


    def print_input_buffer(self):
        pass


    def screen(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug("changing device.next_screen")
        menu = ("* Send", "* Messages", "* Settings"," ")
        self.device.next_screen = ""
        for item in menu:
            self.device.next_screen += "{:<20}".format(item)
        logging.debug("Length of next_screen is {}".format(len(self.device.next_screen)))

    def on_enter(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug("enter pressed")
        # checks if the the cursor is at 0,0
        if self.device.cursor_row == 0:
            # transitions to the send_new state
            self.nextState = SendMenu(self.device)
        # checks if the the cursor is at 1,0
        if self.device.cursor_row == 1:
            # transitions to the received_menu state
            self.nextState = ReceivedMenu(self.device)
        # checks if the the cursor is at 2,0
        if self.device.cursor_row == 2:
            # transitions to the received_menu state
            self.nextState = SettingsMenu(self.device)

    def write_char(self, c):
        pass

    def delete(self):
        pass

    def on_down(self):
        func = inspect.currentframe().f_back.f_code
        if self.device.cursor_row < self.lowest_row:
            # increments the row
            self.device.next_cursor_row = self.device.cursor_row + 1
            self.device.toggle_lcd_event_flag()
            logging.debug("down pressed, cursor position ({},{})".format(self.device.cursor_row, self.device.cursor_col))
        else:
            logging.debug("down pressed but NOT MOVING, cursor position ({},{})".format(self.device.cursor_row, self.device.cursor_col))