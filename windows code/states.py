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
        logging.debug("down pressed, cursor position ({},{})".format(self.device.cursor_row, self.device.cursor_col))

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

    def on_enter(self):
        pass

    def write_char(self, c):
        pass

    def delete(self):
        pass

    def get_next_state(self):
        if self.nextState is None:
            return self
        else:
            return self.nextState


class ComposeMenu(AbstractState):

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
        logging.debug("intial setup for ComposeMenu")
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
            logging.debug("input buffer is not empty")
            self.device.next_screen = "{}{:<55}{}".format(self.device.current_screen[0:5],
                                                          self.device.next_input_buffer,
                                                          self.device.current_screen[60:])
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
        func = inspect.currentframe().f_back.f_code
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
                self.nextState = SendingMenu(self.device)
                self.device.data_to_send["data"] = str(self.device.next_input_buffer)
                logging.debug(self.device.data_to_send["data"])

    def write_char(self, c):
        func = inspect.currentframe().f_back.f_code
        logging.debug("attempting to add {}".format(c))
        """
        Shelved for later
        
        text_col = int(len(self.device.input_buffer) + self.device.initial_cursor_col)
        text_row = int((len(self.device.input_buffer) + self.device.initial_cursor_row) / 20)
        string_num = self.device.cursor_col + (self.device.cursor_row * 20) - self.device.initial_cursor_col
        if c == 'space':
            c = ' '
        logging.debug(self.device.next_cursor_col)
        logging.debug(self.device.next_cursor_row)
        if len(self.device.input_buffer) < 40:
            self.device.next_input_buffer = self.device.input_buffer[:string_num] + c + self.device.input_buffer[string_num:]
            if self.device.next_cursor_col == self.device.lcd_width - 1:
                logging.debug("went to next line")
                self.device.next_cursor_col = 0
                self.device.next_cursor_row = self.device.next_cursor_row + 1

            else:
                logging.debug("printing on line")
                self.device.next_cursor_col = self.device.next_cursor_col + 1
        else:
            logging.debug("stripping last char")
            self.device.next_input_buffer = self.device.input_buffer[:-1]
            self.device.next_cursor_col = self.device.next_cursor_col - 1
        """
        if c == 'space':
            c = ' '
        if len(self.device.input_buffer) < 54:
            self.device.next_input_buffer = self.device.next_input_buffer + c
            if self.device.next_cursor_col == self.device.lcd_width - 1:
                self.device.next_cursor_col = 0
                self.device.next_cursor_row = self.device.next_cursor_row + 1
            else:
                self.device.next_cursor_col = self.device.next_cursor_col + 1
        else:
            self.device.next_input_buffer = self.device.input_buffer[:-1]
            self.device.next_cursor_col = self.device.next_cursor_col - 1
        self.device.toggle_lcd_event_flag()

    def delete(self):
        if len(self.device.next_input_buffer) > 0:
            self.device.next_input_buffer = self.device.next_input_buffer[:-1]
            self.device.toggle_lcd_event_flag()
            if self.device.next_cursor_col > 0:
                self.device.next_cursor_col = self.device.cursor_col - 1
            elif self.device.next_cursor_row > 0:
                self.device.next_cursor_col = self.device.lcd_width - 1
                self.device.next_cursor_row = self.device.cursor_row - 1
            else:
                pass


class SendingMenu(AbstractState):

    def __init__(self, d):
        func = inspect.currentframe().f_back.f_code
        super().__init__(d)
        self.addr_to_use = None
        self.device.next_cursor_row = 0
        self.device.next_cursor_col = 0
        self.device.function_toggle = False
        self.device.toggle_lcd_event_flag()
        logging.debug("creating SendingMessage")

    def initial(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug("intial setup for SendingMessage")
        self.device.initial_cursor_row = 0
        self.device.initial_cursor_col = 0
        self.device.toggle_lcd_event_flag()
        self.device.input_buffer = ""
        self.device.next_input_buffer = ""
        menu = ("Sending message", "", "", "")
        self.device.next_screen = ""
        for item in menu:
            self.device.next_screen += "{:<20}".format(item)

        if self.device.lora.send(str(self.device.data_to_send["data"]), self.device.data_to_send["address"]):
            # saves the data as last_sent for future use
            self.last_sent = self.device.data_to_send
            # transitions to the send_successful state
            self.nextState = SendSuccessful(self.device)
            # clears data_to_send for the next message
            self.device.data_to_send = {}
        else:
            # if False transitions to the send_failed state
            self.nextState = SendingMenu(self.device)


class SendSuccessful(AbstractState):

    def __init__(self, d):
        func = inspect.currentframe().f_back.f_code
        super().__init__(d)
        self.addr_to_use = None
        self.device.next_cursor_row = 0
        self.device.next_cursor_col = 0
        self.device.function_toggle = False
        self.device.toggle_lcd_event_flag()
        logging.debug("creating SendSuccessful")

    def initial(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug("intial setup for SendSuccessful")
        self.device.initial_cursor_row = 0
        self.device.initial_cursor_col = 0
        self.device.toggle_lcd_event_flag()
        self.device.input_buffer = ""
        self.device.next_input_buffer = ""
        menu = ("Send Successful", "", "", "")
        self.device.next_screen = ""
        for item in menu:
            self.device.next_screen += "{:<20}".format(item)

    def get_next_state(self):
        if self.nextState is None:
            return self
        else:
            return self.nextState

    def use_keyboard_input(self, kb):
        if kb['enter']:
            self.on_enter()
            return

    def on_enter(self):
        self.nextState = MainMenu(self.device)
        pass


class SettingsMenu(AbstractState):

    def __init__(self, d):
        func = inspect.currentframe().f_back.f_code
        super().__init__(d)
        self.addr_to_use = None
        self.device.next_cursor_row = 0
        self.device.next_cursor_col = 0
        self.device.toggle_lcd_event_flag()
        logging.debug("creating SettingsMenu")

    def initial(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug(" ")
        self.device.toggle_lcd_event_flag()
        self.device.next_screen = ""
        menu = ("* Set addr (0-65535)", "* Set ntwk (0-16)", "", "M")
        for item in menu:
            self.device.next_screen += "{:<20}".format(item)

    def use_keyboard_input(self, kb):
        if kb['enter']:
            self.on_enter()
            return
        if kb['s']:
            self.on_down()
            return
        if kb['w']:
            self.on_up()
            return

    def on_enter(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug("enter pressed")
        # checks if the the cursor is at 0,0
        if self.device.cursor_row == 0:
            # transitions to the send_new state
            self.nextState = SetAddress(self.device)
        # checks if the the cursor is at 1,0
        if self.device.cursor_row == 1:
            # transitions to the received_menu state
            self.nextState = SetNetworkid(self.device)
        # checks if the the cursor is at 2,0
        if self.device.cursor_row == 3:
            # transitions to the received_menu state
            self.nextState = MainMenu(self.device)

    def on_up(self):
        func = inspect.currentframe().f_back.f_code
        self.device.toggle_lcd_event_flag()
        if self.device.cursor_row > 0:
            self.device.next_cursor_row = self.device.cursor_row - 1
            if self.device.next_cursor_row == 2:
                self.device.next_cursor_row -= 1
        logging.debug("up pressed, cursor position ({},{})".format(self.device.cursor_row, self.device.cursor_col))

    def on_down(self):
        func = inspect.currentframe().f_back.f_code
        self.device.toggle_lcd_event_flag()
        if self.device.cursor_row < self.device.lcd_height - 1:
            self.device.next_cursor_row = self.device.cursor_row + 1
            if self.device.next_cursor_row == 2:
                self.device.next_cursor_row += 1
        self.device.next_cursor_col = 0
        logging.debug("down pressed, cursor position ({},{})".format(self.device.cursor_row, self.device.cursor_col))

    def write_char(self, c):
        pass

    def delete(self):
        pass

    def get_next_state(self):
        if self.nextState is None:
            return self
        else:
            return self.nextState


class SetAddress(AbstractState):

    def __init__(self, d):
        super().__init__(d)
        self.device.function_toggle = False
        self.device.next_cursor_row = 0
        self.device.next_cursor_col = 0
        self.device.toggle_lcd_event_flag()
        self.device.input_buffer = ""
        self.device.next_input_buffer = ""

    def get_next_state(self):
        if self.nextState is None:
            return self
        else:
            return self.nextState

    def initial(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug(" ")
        self.device.next_cursor_row = 1
        self.device.next_cursor_col = 0
        self.device.toggle_lcd_event_flag()
        self.device.next_screen = ""
        menu = ("Set addr (0-65535)", "", "enter", "M")
        for item in menu:
            self.device.next_screen += "{:<20}".format(item)

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

        for k in kb.keys():
            if kb[k]:
                self.write_char(k)
                break

    def screen(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug("changing device.next_screen")
        logging.debug("device.current_screen {}".format(self.device.current_screen))
        logging.debug("device.next_screen {}".format(self.device.next_screen))
        if self.device.input_buffer != self.device.next_input_buffer:
            logging.debug("input buffer is not empty")
            self.device.next_screen = "{}{:<5}{}".format(self.device.current_screen[0:20],
                                                         self.device.next_input_buffer,
                                                         self.device.current_screen[25:])
            print(self.device.next_screen)
            logging.debug("setting next_screen to {}".format(self.device.next_screen))
            self.device.input_buffer = self.device.next_input_buffer
        logging.debug("Length of next_screen is {}".format(len(self.device.next_screen)))

    def on_enter(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug("enter pressed")
        # checks if the the cursor is at 0,0
        if self.device.next_cursor_row == 2 and self.device.next_cursor_col <= 5:
            # transitions to the main_menu state
            self.nextState = MainMenu(self.device)
            # saves the address to the data_to_send
            self.device.data_to_send["address_to_use"] = int(self.device.input_buffer)
            logging.debug(self.device.data_to_send)
            self.device.data_to_send = {}

    def write_char(self, c):
        func = inspect.currentframe().f_back.f_code
        logging.debug("attemping to add {}".format(c))
        addr = None
        if c in [str(e) for e in range(0, 10)]:
            logging.debug("yea its a number")
            self.device.next_input_buffer += c
            try:
                addr = int(self.device.next_input_buffer)
                logging.debug("addr seems valid")
                if addr > 65535:
                    raise ValueError
                self.device.next_cursor_col = self.device.cursor_col + 1
                self.device.toggle_lcd_event_flag()
                logging.debug("nextscreen set")
            except:
                logging.debug("wasnt valid")
                self.device.next_input_buffer = self.device.next_input_buffer[:-1]
        if addr is not None:
            self.addr_to_use = addr

    def delete(self):
        if self.device.cursor_row == 1:
            if len(self.device.next_input_buffer) > 0:
                self.device.next_input_buffer = self.device.next_input_buffer[:-1]
                self.device.toggle_lcd_event_flag()
                self.device.next_cursor_col = self.device.cursor_col - 1

    def on_up(self):
        self.device.toggle_lcd_event_flag()
        if self.device.cursor_row > 0:
            self.device.next_cursor_row = self.device.cursor_row - 1
            if self.device.next_cursor_row == 1:
                self.device.next_cursor_col = len(self.device.input_buffer)
            else:
                self.device.next_cursor_col = 0

    def on_down(self):
        func = inspect.currentframe().f_back.f_code
        self.device.toggle_lcd_event_flag()
        if self.device.cursor_row < self.device.lcd_height - 1:
            self.device.next_cursor_row = self.device.cursor_row + 1
            if self.device.next_cursor_row == 1:
                self.device.next_cursor_col = len(self.device.input_buffer)
            else:
                self.device.next_cursor_col = 0
        logging.debug("down pressed, cursor position ({},{})".format(self.device.cursor_row, self.device.cursor_col))


class SetNetworkid(AbstractState):

    def __init__(self, d):
        super().__init__(d)
        self.device.function_toggle = False
        self.device.next_cursor_row = 0
        self.device.next_cursor_col = 0
        self.device.toggle_lcd_event_flag()
        self.device.input_buffer = ""
        self.device.next_input_buffer = ""

    def initial(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug(" ")
        self.device.next_cursor_row = 1
        self.device.next_cursor_col = 0
        self.device.toggle_lcd_event_flag()
        self.device.next_screen = ""
        menu = ("* Set ntwk (0-16)", "", "enter", "M")
        for item in menu:
            self.device.next_screen += "{:<20}".format(item)

    def get_next_state(self):
        if self.nextState is None:
            return self
        else:
            return self.nextState

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

        for k in kb.keys():
            if kb[k]:
                self.write_char(k)
                break

    def screen(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug("changing device.next_screen")
        logging.debug("device.current_screen {}".format(self.device.current_screen))
        logging.debug("device.next_screen {}".format(self.device.next_screen))
        if self.device.input_buffer != self.device.next_input_buffer:
            logging.debug("input buffer is not empty")
            self.device.next_screen = "{}{:<2}{}".format(self.device.current_screen[0:20],
                                                         self.device.next_input_buffer,
                                                         self.device.current_screen[22:])
            print(self.device.next_screen)
            logging.debug("setting next_screen to {}".format(self.device.next_screen))
            self.device.input_buffer = self.device.next_input_buffer
        logging.debug("Length of next_screen is {}".format(len(self.device.next_screen)))

    def on_enter(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug("enter pressed")
        # checks if the the cursor is at 0,0
        if self.device.next_cursor_row == 2 and self.device.next_cursor_col <= 5:
            # transitions to the main_menu state
            self.nextState = MainMenu(self.device)
            # saves the address to the data_to_send
            self.device.data_to_send["networkid_to_use"] = int(self.device.input_buffer)
            logging.debug(self.device.data_to_send)
            self.device.data_to_send = {}

    def write_char(self, c):
        func = inspect.currentframe().f_back.f_code
        logging.debug("attemping to add {}".format(c))
        addr = None
        if c in [str(e) for e in range(0, 10)]:
            logging.debug("yea its a number")
            self.device.next_input_buffer += c
            try:
                addr = int(self.device.next_input_buffer)
                logging.debug("networkid seems valid")
                if addr > 16:
                    raise ValueError
                self.device.next_cursor_col = self.device.cursor_col + 1
                self.device.toggle_lcd_event_flag()
                logging.debug("nextscreen set")
            except:
                logging.debug("wasnt valid")
                self.device.next_input_buffer = self.device.next_input_buffer[:-1]
        if addr is not None:
            self.addr_to_use = addr

    def delete(self):
        if self.device.cursor_row == 1:
            if len(self.device.next_input_buffer) > 0:
                self.device.next_input_buffer = self.device.next_input_buffer[:-1]
                self.device.toggle_lcd_event_flag()
                self.device.next_cursor_col = self.device.cursor_col - 1

    def on_up(self):
        self.device.toggle_lcd_event_flag()
        if self.device.cursor_row > 0:
            self.device.next_cursor_row = self.device.cursor_row - 1
            if self.device.next_cursor_row == 1:
                self.device.next_cursor_col = len(self.device.input_buffer)
            else:
                self.device.next_cursor_col = 0

    def on_down(self):
        func = inspect.currentframe().f_back.f_code
        self.device.toggle_lcd_event_flag()
        if self.device.cursor_row < self.device.lcd_height - 1:
            self.device.next_cursor_row = self.device.cursor_row + 1
            if self.device.next_cursor_row == 1:
                self.device.next_cursor_col = len(self.device.input_buffer)
            else:
                self.device.next_cursor_col = 0
        logging.debug("down pressed, cursor position ({},{})".format(self.device.cursor_row, self.device.cursor_col))


class ReceivedMenu(AbstractState):

    def __init__(self, d):
        func = inspect.currentframe().f_back.f_code
        super().__init__(d)
        logging.debug(" ")
        self.addr_to_use = None
        self.last_sender = None
        self.sender = None
        self.message = ""
        self.current_message = 0
        self.device.next_cursor_row = 0
        self.device.next_cursor_col = 0
        self.device.function_toggle = False
        logging.info("input_buffer {}".format(self.device.input_buffer))
        logging.info("next_input_buffer".format(self.device.next_input_buffer))
        logging.info("next screen ".format(self.device.next_screen))

        logging.info("end init")

    def initial(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug(" ")
        self.device.initial_cursor_row = 3
        self.device.initial_cursor_col = 0
        self.device.next_cursor_row = self.device.initial_cursor_row
        self.device.next_cursor_col = self.device.initial_cursor_col
        self.device.toggle_lcd_event_flag()
        self.device.input_buffer = ""
        self.device.next_input_buffer = ""
        menu = ("Message from:", "", "", "M")
        self.device.next_screen = ""
        for item in menu:
            self.device.next_screen += "{:<20}".format(item)

    def screen(self):
        func = inspect.currentframe().f_back.f_code
        logging.info("changing device.next_screen")
        logging.info("device.current_screen {}".format(self.device.current_screen))
        logging.info("device.next_screen {}".format(self.device.next_screen))
        if self.sender != self.last_sender:
            logging.info("input buffer is not empty")
            self.device.next_screen = "{}{:<6}{:<40}{:<20}".format(self.device.current_screen[0:14], str(self.sender),
                                                                   self.message,
                                                                   self.device.current_screen[60:])
            print(self.device.next_screen)
            logging.info("setting next_screen to {}".format(self.device.next_screen))
            self.device.last_sender = self.sender
        logging.info("Length of next_screen is {}".format(len(self.device.next_screen)))

    def use_keyboard_input(self, kb):
        func = inspect.currentframe().f_back.f_code
        logging.info("keyboard used {}".format(kb))
        if kb['s']:
            self.next_message()
            return
        if kb['w']:
            self.last_message()
            return
        if kb['enter']:
            self.on_enter()
            return

    def on_enter(self):
        func = inspect.currentframe().f_back.f_code
        logging.info("enter pressed")
        if self.device.next_cursor_row == 3:
            # transitions to the main_menu state
            self.nextState = MainMenu(self.device)
        logging.info("end enter")

    def next_message(self):
        func = inspect.currentframe().f_back.f_code
        logging.info(" ")
        self.device.toggle_lcd_event_flag()
        if self.current_message < len(self.device.messages)-1:
            self.current_message += 1
            logging.info("Current message is: {}".format(self.current_message))
        self.sender = self.device.messages[self.current_message]['address']
        self.message = self.device.messages[self.current_message]['data']
        logging.info("end next_message")

    def last_message(self):
        func = inspect.currentframe().f_back.f_code
        logging.info(" ")
        self.device.toggle_lcd_event_flag()
        if self.current_message > 0:
            self.current_message -= 1
            logging.info("Current message is: {}".format(self.current_message))
        self.sender = self.device.messages[self.current_message]['address']
        self.message = self.device.messages[self.current_message]['data']
        logging.info("last message")

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
        logging.debug(" ")
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
            logging.debug("input buffer is not empty")
            self.device.next_screen = "{}{:<5}{}".format(self.device.current_screen[0:3], self.device.next_input_buffer,
                                                         self.device.current_screen[8:])
            print(self.device.next_screen)
            logging.debug("setting next_screen to {}".format(self.device.next_screen))
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

        logging.debug("attemping to add {}".format(c))
        addr = None
        if c in [str(e) for e in range(0, 10)]:
            logging.debug("yea its a number")
            self.device.next_input_buffer += c
            try:
                addr = int(self.device.next_input_buffer)
                logging.debug("addr seems valid")
                if addr > 65535:
                    raise ValueError
                self.device.next_cursor_col = self.device.cursor_col + 1
                self.device.toggle_lcd_event_flag()
                logging.debug("nextscreen set")
            except:
                logging.debug("wasnt valid")
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
