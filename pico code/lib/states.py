class AbstractState(object):

    def __init__(self, d):
        self.device = d
        self.nextState = None

    def initial(self):
        pass

    def use_keyboard_input(self, kb: dict):
        pass

    def screen(self):
        pass

    def on_up(self):
        self.device.toggle_lcd_event_flag()
        if self.device.cursor_row > 0:
            self.device.next_cursor_row = self.device.cursor_row - 1

    def on_down(self):
        self.device.toggle_lcd_event_flag()
        if self.device.cursor_row < self.device.lcd_height - 1:
            self.device.next_cursor_row = self.device.cursor_row + 1

    def on_left(self):
        self.device.toggle_lcd_event_flag()
        if self.device.cursor_col > 0:
            # decrements the column
            self.device.next_cursor_col = self.device.cursor_col - 1

    def on_right(self):
        self.device.toggle_lcd_event_flag()
        if self.device.cursor_col < self.device.lcd_width - 1:
            # increments the column
            self.device.next_cursor_col = self.device.cursor_col + 1

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
        super().__init__(d)
        self.device.next_cursor_row = 0
        self.device.next_cursor_col = 5
        self.device.function_toggle = False
        self.device.toggle_lcd_event_flag()

    def initial(self):
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
        if self.device.input_buffer != self.device.next_input_buffer:
            self.device.next_screen = "{}{:<55}{}".format(self.device.current_screen[0:5],
                                                          self.device.next_input_buffer,
                                                          self.device.current_screen[60:])
            self.device.input_buffer = self.device.next_input_buffer

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
        if self.device.cursor_row == 3 and self.device.cursor_col == 0:
            self.nextState = MainMenu(self.device)
        elif self.device.cursor_row == 3 and self.device.cursor_col == 2:
            self.nextState = SendMenu(self.device)
        elif self.device.cursor_row == 0 and self.device.cursor_col <= 5:
            if self.device.input_buffer is not None:
                self.nextState = SendingMenu(self.device)
                self.device.data_to_send["data"] = str(self.device.next_input_buffer)

    def write_char(self, c):
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

    def get_next_state(self):
        if self.nextState is None:
            return self
        else:
            return self.nextState


class SendingMenu(AbstractState):

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
        super().__init__(d)
        self.addr_to_use = None
        self.device.next_cursor_row = 0
        self.device.next_cursor_col = 0
        self.device.function_toggle = False
        self.device.toggle_lcd_event_flag()

    def initial(self):
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
        if self.device.input_buffer != self.device.next_input_buffer:
            self.device.next_screen = "{}{:<5}{}".format(self.device.current_screen[0:3], self.device.next_input_buffer,
                                                         self.device.current_screen[8:])
            self.device.input_buffer = self.device.next_input_buffer

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
        if self.device.cursor_row == 1:
            if self.device.input_buffer != "":
                self.nextState = ComposeMenu(self.device)
                self.device.data_to_send["address"] = self.addr_to_use

        if self.device.cursor_row == 3:
            self.nextState = MainMenu(self.device)

    def on_up(self):
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

    def on_down(self):
        self.device.toggle_lcd_event_flag()
        if self.device.cursor_row < self.device.lcd_height - 1:
            self.device.next_cursor_row = self.device.cursor_row + 1
            if self.device.next_cursor_row == 1:
                self.device.next_cursor_col = 0
            if self.device.next_cursor_row == 2:
                self.device.next_cursor_row += 1
        self.device.next_cursor_col = 0

    def write_char(self, c):
        addr = None
        if c in [str(e) for e in range(0, 10)]:
            self.device.next_input_buffer += c
            try:
                addr = int(self.device.next_input_buffer)
                if addr > 65535:
                    raise ValueError
                self.device.next_cursor_col = self.device.cursor_col + 1
                self.device.toggle_lcd_event_flag()
            except:
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
        menu = ("* Send", "* Messages", "* Settings", " ")
        self.device.next_screen = ""
        for item in menu:
            self.device.next_screen += "{:<20}".format(item)

    def on_enter(self):
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
        if self.device.cursor_row < self.lowest_row:
            # increments the row
            self.device.next_cursor_row = self.device.cursor_row + 1
            self.device.toggle_lcd_event_flag()
