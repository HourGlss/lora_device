from abc import ABC, abstractmethod
import inspect
import logging



class AbstractState(ABC):

    def __init__(self, d):
        func = inspect.currentframe().f_back.f_code
        logging.debug("created")
        self.device = d
        self.nextState = None

    @abstractmethod
    def initial(self):
        pass

    @abstractmethod
    def use_keyboard_input(self, kb: dict):
        pass

    @abstractmethod
    def screen(self):
        pass

    def on_up(self):
        func = inspect.currentframe().f_back.f_code
        self.device.toggle_lcd_event_flag()
        if self.device.cursor_row > 0:
            self.device.next_cursor_row = self.device.cursor_row - 1
        logging.debug("up pressed, cursor position ({},{})".format(self.device.cursor_row, self.device.cursor_col))

    def on_down(self):
        func = inspect.currentframe().f_back.f_code
        self.device.toggle_lcd_event_flag()
        if self.device.cursor_row < self.device.lcd_height - 1:
            self.device.next_cursor_row = self.device.cursor_row + 1
        logging.info("down pressed, cursor position ({},{})".format(self.device.cursor_row, self.device.cursor_col))

    def on_left(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug("left pressed")
        self.device.toggle_lcd_event_flag()
        if self.device.cursor_col > 0:
            # decrements the column
            self.device.next_cursor_col = self.device.cursor_col - 1
        logging.debug("left pressed, cursor position ({},{})".format(self.device.cursor_row, self.device.cursor_col))

    def on_right(self):
        func = inspect.currentframe().f_back.f_code
        self.device.toggle_lcd_event_flag()
        if self.device.cursor_col < self.device.lcd_width - 1:
            # increments the column
            self.device.next_cursor_col = self.device.cursor_col + 1
        logging.debug("right pressed, cursor position ({},{})".format(self.device.cursor_row, self.device.cursor_col))

    @abstractmethod
    def on_enter(self):
        pass

    @abstractmethod
    def write_char(self, c):
        pass

    @abstractmethod
    def delete(self):
        pass

    def get_next_state(self):
        if self.nextState is None:
            return self
        else:
            return self.nextState


class ComposeMenu(AbstractState):
    """
    TODO
    """

    def __init__(self, d):
        func = inspect.currentframe().f_back.f_code
        logging.debug("ComposeMenu initialized")
        super().__init__(d)
        self.device.next_cursor_row = 0
        self.device.next_cursor_col = 5
        self.device.function_toggle = False
        self.device.toggle_lcd_event_flag()
        logging.debug("creating ComposeMenu")

    def initial(self):
        func = inspect.currentframe().f_back.f_code
        logging.info("intial setup for ComposeMenu")
        self.device.initial_cursor_row = 0
        self.device.initial_cursor_col = 5
        self.device.next_cursor_row = self.device.initial_cursor_row
        self.device.next_cursor_col = self.device.initial_cursor_col
        self.device.toggle_lcd_event_flag()
        self.device.input_buffer = ""
        self.device.next_input_buffer = ""
        menu = ("Send:", "", "", "M B")
        self.device.next_screen = ""
        for item in menu:
            self.device.next_screen += "{:<20}".format(item)

    def screen(self):
        func = inspect.currentframe().f_back.f_code
        if self.device.input_buffer != self.device.next_input_buffer:
            logging.info("input buffer is not empty")
            self.device.next_screen = "{}{}{}".format(self.device.current_screen[0:5], self.device.next_input_buffer,
                                                         self.device.current_screen[59:])
            self.device.input_buffer = self.device.next_input_buffer

            logging.debug("Length of next_screen is {}".format(len(self.device.next_screen)))
        else:
            pass


    def use_keyboard_input(self, kb):
        if kb['enter']:
            self.on_enter()
            return
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
            if kb['a']:
                self.on_left()
                return
            if kb['d']:
                self.on_right()
                return
        if kb['backspace']:
            self.delete()
            return

        for k in kb.keys():
            if kb[k]:
                self.write_char(k)
                break

    def on_enter(self):
        # checks if the the cursor is at 3,0
        if self.device.cursor_row == 3 and self.device.cursor_col == 0:
            # transitions to the main_menu state
            self.nextState = MainMenu(self.device)

        # checks if the the cursor is at 3,2
        elif self.device.cursor_row == 3 and self.device.cursor_col == 2:
            # transitions to the send_menu state
            self.nextState = SendMenu(self.device)

        # checks if the the cursor is at 3,4
        elif self.device.cursor_row == 0 and self.device.cursor_col <= 5:
            # transitions to the sending_message state
            if self.device.input_buffer is not None:
                self.nextState = SendingMessage(self.device)
                self.device.data_to_send["data"] = str(self.device.input_buffer)

    def write_char(self, c):
        func = inspect.currentframe().f_back.f_code
        logging.info("attempting to add {}".format(c))

        text_col = int(len(self.device.input_buffer) + self.device.initial_cursor_col)
        text_row = int((len(self.device.input_buffer) + self.device.initial_cursor_row) / 20)

        # if c == 'space':
        #     c = ' '

    def delete(self):
        string_num = self.device.cursor_col + (self.device.cursor_row * self.device.lcd_width) - self.device.initial_cursor_col
        if len(self.device.next_input_buffer) > 0:

            if self.device.cursor_col > 0:
                self.device.next_input_buffer = self.device.next_input_buffer[:string_num - 1] + self.device.next_input_buffer[string_num:]
                self.device.toggle_lcd_event_flag()
                self.device.next_cursor_col = self.device.cursor_col - 1
            elif self.device.cursor_row == 0 and self.device.cursor_col == 0:
                pass
            else:
                self.device.next_cursor_col = self.device.lcd_width - 1
                self.device.next_cursor_row = self.device.cursor_row - 1
                self.device.toggle_lcd_event_flag()


    def get_next_state(self):
        if self.nextState is None:
            return self
        else:
            return self.nextState

class SendingMessage(AbstractState):

    def __init__(self, d):
        super().__init__(d)

    def get_next_state(self):
        pass

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
        pass

    def print_input_buffer(self):
        pass

    def update_screen(self):
        pass

    def on_enter(self):
        pass

    def write_char(self, c):
        pass

    def delete(self):
        pass

class SettingsMenu(AbstractState):

    def __init__(self, d):
        super().__init__(d)

    def get_next_state(self):
        pass

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
        pass

    def print_input_buffer(self):
        pass

    def update_screen(self):
        pass

    def on_enter(self):
        pass

    def write_char(self, c):
        pass

    def delete(self):
        pass


class ReceivedMenu(AbstractState):

    def __init__(self, d):
        super().__init__(d)

    def get_next_state(self):
        pass

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
        pass

    def print_input_buffer(self):
        pass

    def update_screen(self):
        pass

    def on_enter(self):
        pass

    def write_char(self, c):
        pass

    def delete(self):
        pass


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
        self.device.initial_cursor_row = 0
        self.device.initial_cursor_col = 3
        self.device.next_cursor_row = self.device.initial_cursor_row
        self.device.next_cursor_col = self.device.initial_cursor_col
        self.device.toggle_lcd_event_flag()
        self.device.input_buffer = ""
        self.device.next_input_buffer = ""
        menu = ("To:", "Compose", " ", "M")
        self.device.next_screen = ""
        for item in menu:
            self.device.next_screen += "{:<20}".format(item)

    def screen(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug("changing device.next_screen")
        logging.debug("device.current_screen {}".format(self.device.current_screen))
        logging.debug("device.next_screen {}".format(self.device.next_screen))
        if self.device.input_buffer != self.device.next_input_buffer:
            logging.info("input buffer is not empty")
            self.device.next_screen = "{}{:<5}{}".format(self.device.current_screen[0:3], self.device.next_input_buffer,
                                                         self.device.current_screen[8:])
            print(self.device.next_screen)
            logging.info("setting next_screen to {}".format(self.device.next_screen))
            self.device.input_buffer = self.device.next_input_buffer
        logging.debug("Length of next_screen is {}".format(len(self.device.next_screen)))

    def use_keyboard_input(self, kb):
        if kb['enter']:
            self.on_enter()
            return
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
        if kb['backspace']:
            self.delete()
            return

        if self.device.cursor_row == 0:
            for k in kb.keys():
                if kb[k]:
                    self.write_char(k)
                    break

    def on_enter(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug("on_enter call")
        if self.device.cursor_row == 1:
            # checks if the input buffer is empty and if so passes
            if self.device.input_buffer != "":
                # transitions to the compose_menu state
                self.nextState = ComposeMenu(self.device)
                # sets the data_to_send address
                self.device.data_to_send["address"] = self.addr_to_use

        if self.device.cursor_row == 3:
            logging.debug("nextstate set to mainmenu")
            # transitions to the main_menu state
            self.nextState = MainMenu(self.device)

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
        if self.device.cursor_row == 0:
            if len(self.device.next_input_buffer) > 0:
                self.device.next_input_buffer = self.device.next_input_buffer[:-1]
                self.device.toggle_lcd_event_flag()
                self.device.next_cursor_col = self.device.cursor_col - 1


class MainMenu(AbstractState):

    def initial(self):
        pass

    def __init__(self, d):
        super().__init__(d)
        self.device.function_toggle = False
        self.device.next_cursor_row = 0
        self.device.next_cursor_col = 0
        self.lowest_row = 2
        self.device.toggle_lcd_event_flag()

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

    def screen(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug("changing device.next_screen")
        menu = ("* Send", "* Messages", "* Settings", " ")
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
            logging.debug(
                "down pressed, cursor position ({},{})".format(self.device.cursor_row, self.device.cursor_col))
        else:
            logging.debug("down pressed but NOT MOVING, cursor position ({},{})".format(self.device.cursor_row,
                                                                                        self.device.cursor_col))
