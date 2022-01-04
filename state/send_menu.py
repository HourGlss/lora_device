from state.state import AbstractState
from state.compose_menu import ComposeMenu
# from state.main_menu import MainMenu
import logging
import inspect
import sys


class SendMenu(AbstractState):

    def __init__(self, d):
        func = inspect.currentframe().f_back.f_code
        super().__init__(d)
        logging.debug(" ")
        self.addr_to_use = None
        self.device.next_cursor_row = 0
        self.device.next_cursor_col = 0
        self.device.function_toggle = False
        self.device.toggle_lcd_event_flag()
        logging.debug("creating SendMenu")

    def initial(self):
        func = inspect.currentframe().f_back.f_code
        logging.info(" ")
        self.device.next_cursor_row = 0
        self.device.next_cursor_col = 3
        self.device.cursor_row = 0
        self.device.cursor_col = 3
        self.device.toggle_lcd_event_flag()
        self.device.input_buffer = ""
        menu = ("To:", "Compose", " ", "M")
        self.device.next_screen = ""
        for item in menu:
            self.device.next_screen += "{:<20}".format(item)

    def screen(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug("changing device.next_screen")
        if self.device.input_buffer != self.device.next_input_buffer:
            logging.info("input buffer is not empty")
            self.device.next_screen = "{}{:<5}{}".format(self.device.next_screen[0:3], self.device.next_input_buffer,
                                                         self.device.next_screen[8:])
            print(self.device.next_screen)
            logging.info("setting next_screen to {}".format(self.device.next_screen))
            self.device.input_buffer = self.device.next_input_buffer
        logging.debug("Length of next_screen is {}".format(len(self.device.next_screen)))

    def use_keyboard_input(self, kb):
        if kb['right shift']:
            self.device.function_toggle = not self.device.function_toggle
            return
        if self.device.function_toggle:
            if kb['s']:
                self.on_down()
                return
            if kb['w']:
                self.on_up()
                return
        elif kb['backspace']:
            self.delete()
            return
        elif kb['enter']:
            self.on_enter()
            return
        else:
            if self.device.cursor_row == 0:
                for k in kb.keys():
                    if kb[k]:
                        self.write_char(k)
                        break

    def on_enter(self):
        if self.device.cursor_row == 1:
            # checks if the input buffer is empty and if so passes
            if self.device.input_buffer != "":
                # transitions to the compose_menu state
                self.nextState = ComposeMenu(self.device)
                # sets the data_to_send address
                self.device.data_to_send["address"] = self.addr_to_use

        if self.device.cursor_row == 3:
            # transitions to the main_menu state
            # self.nextState = MainMenu(self.device)
            # sets the data_to_send address
            self.device.data_to_send["address"] = int(self.input_buffer)
            # clears the input buffer
            self.device.input_buffer = ""

    def on_up(self):
        func = inspect.currentframe().f_back.f_code
        self.device.toggle_lcd_event_flag()
        if self.device.cursor_row > 0:
            self.device.next_cursor_row = self.device.cursor_row - 1
            if self.device.cursor_row == 3:
                self.device.next_cursor_row -= 1

        if self.device.next_cursor_row == 0:
            if self.device.input_buffer == "":
                self.device.next_cursor_col = 3
            else:
                self.device.next_cursor_col = len(self.device.input_buffer) + 3
        else:
            self.device.next_cursor_col = 0

        logging.debug("up pressed, cursor position ({},{})".format(self.device.cursor_row, self.device.cursor_col))

    def on_down(self):
        func = inspect.currentframe().f_back.f_code
        self.device.toggle_lcd_event_flag()
        if self.device.cursor_row < self.device.lcd_height - 1:
            self.device.next_cursor_row = self.device.cursor_row + 1
            if self.device.next_cursor_row == 1:
                self.device.next_cursor_col = 0
            if self.device.next_cursor_row == 2:
                self.device.next_cursor_row += 1
        self.device.next_cursor_col = 0
        logging.debug("down pressed, cursor position ({},{})".format(self.device.cursor_row, self.device.cursor_col))

    def write_char(self, c):
        func = inspect.currentframe().f_back.f_code

        logging.info("attemping to add {}".format(c))
        addr = None
        if c in [str(e) for e in range(0, 10)]:
            logging.info("yea its a number")
            self.device.next_input_buffer += c
            try:
                addr = int(self.device.next_input_buffer)
                logging.info("addr seems valid")
                if addr > 65535:
                    raise ValueError
                self.device.next_cursor_col = self.device.cursor_col + 1
                self.device.toggle_lcd_event_flag()
                logging.info("nextscreen set")
            except:
                logging.info("wasnt valid")
                self.device.next_input_buffer = self.device.next_input_buffer[:-1]
        if addr is not None:
            self.addr_to_use = addr

    def delete(self):
        pass
