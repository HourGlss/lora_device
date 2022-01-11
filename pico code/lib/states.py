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
        print("Comp init called")
        self.device.next_cursor_row = 0
        self.device.next_cursor_col = 5
        self.device.function_toggle = False
        self.device.toggle_lcd_event_flag()

    def initial(self):
        print("comp initial called")
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
            print("Compose typed a char")
            self.device.next_screen = "{}{:<55}{}".format(self.device.next_screen[0:5],
                                                          self.device.next_input_buffer,
                                                          self.device.next_screen[60:])
            self.device.input_buffer = self.device.next_input_buffer
        if self.device.next_input_buffer == "":
            self.device.next_screen = ""
            menu = ("Send:", "", "", "M B")
            for item in menu:
                self.device.next_screen += "{:<20}".format(item)

    def use_keyboard_input(self, kb):
        if kb['enter']:
            self.on_enter()
            return
        if kb['right shift']:
            self.device.function_toggle = not self.device.function_toggle
            self.device.toggle_lcd_event_flag()
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
                temp = str(self.device.next_input_buffer)
                temp = temp.strip()
                temp = temp.replace("\r\n","")
                temp = temp.replace("\n","")
                self.device.data_to_send["data"] = temp
                del temp

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


class SendingMenu(AbstractState):

    def __init__(self, d):
        super().__init__(d)
        self.addr_to_use = None
        self.device.next_cursor_row = 0
        self.device.next_cursor_col = 0
        self.device.function_toggle = False
        self.device.toggle_lcd_event_flag()

    def initial(self):
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
            self.last_sent = self.device.data_to_send
            self.nextState = SendSuccessful(self.device)
            self.device.data_to_send = {}
        else:
            self.nextState = SendingMenu(self.device)


class SendSuccessful(AbstractState):

    def __init__(self, d):
        super().__init__(d)
        self.addr_to_use = None
        self.device.next_cursor_row = 0
        self.device.next_cursor_col = 0
        self.device.function_toggle = False
        self.device.toggle_lcd_event_flag()

    def initial(self):
        self.device.initial_cursor_row = 0
        self.device.initial_cursor_col = 0
        self.device.toggle_lcd_event_flag()
        self.device.input_buffer = ""
        self.device.next_input_buffer = ""
        menu = ("Send Successful", "", "", "")
        self.device.next_screen = ""
        for item in menu:
            self.device.next_screen += "{:<20}".format(item)

    def use_keyboard_input(self, kb):
        if kb['enter']:
            self.on_enter()
            return

    def on_enter(self):
        self.nextState = MainMenu(self.device)
        pass


class SettingsMenu(AbstractState):

    def __init__(self, d):
        super().__init__(d)
        self.addr_to_use = None
        self.device.next_cursor_row = 0
        self.device.next_cursor_col = 0
        self.device.toggle_lcd_event_flag()

    def initial(self):
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
        if self.device.cursor_row == 0:
            self.nextState = SetAddress(self.device)
        if self.device.cursor_row == 1:
            self.nextState = SetNetworkid(self.device)
        if self.device.cursor_row == 3:
            self.nextState = MainMenu(self.device)

    def on_up(self):
        self.device.toggle_lcd_event_flag()
        if self.device.cursor_row > 0:
            self.device.next_cursor_row = self.device.cursor_row - 1
            if self.device.next_cursor_row == 2:
                self.device.next_cursor_row -= 1

    def on_down(self):
        self.device.toggle_lcd_event_flag()
        if self.device.cursor_row < self.device.lcd_height - 1:
            self.device.next_cursor_row = self.device.cursor_row + 1
            if self.device.next_cursor_row == 2:
                self.device.next_cursor_row += 1
        self.device.next_cursor_col = 0


class SetAddress(AbstractState):

    def __init__(self, d):
        super().__init__(d)
        self.device.function_toggle = False
        self.device.next_cursor_row = 0
        self.device.next_cursor_col = 0
        self.device.toggle_lcd_event_flag()
        self.device.input_buffer = ""
        self.device.next_input_buffer = ""
        self.addr_to_use = None

    def initial(self):
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
            self.device.toggle_lcd_event_flag()
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
        if self.device.input_buffer != self.device.next_input_buffer:
            self.device.next_screen = "{}{:<5}{}".format(self.device.current_screen[0:20],
                                                         self.device.next_input_buffer,
                                                         self.device.current_screen[25:])
            self.device.input_buffer = self.device.next_input_buffer

    def on_enter(self):
        # checks if the the cursor is at 0,0
        if self.device.next_cursor_row == 2 and self.device.next_cursor_col <= 5:
            self.nextState = MainMenu(self.device)
            self.device.lora.set_address(self.addr_to_use)

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
        self.device.toggle_lcd_event_flag()
        if self.device.cursor_row < self.device.lcd_height - 1:
            self.device.next_cursor_row = self.device.cursor_row + 1
            if self.device.next_cursor_row == 1:
                self.device.next_cursor_col = len(self.device.input_buffer)
            else:
                self.device.next_cursor_col = 0


class SetNetworkid(AbstractState):

    def __init__(self, d):
        super().__init__(d)
        self.device.function_toggle = False
        self.device.next_cursor_row = 0
        self.device.next_cursor_col = 0
        self.device.toggle_lcd_event_flag()
        self.device.input_buffer = ""
        self.device.next_input_buffer = ""
        self.addr_to_use = None

    def initial(self):
        self.device.next_cursor_row = 1
        self.device.next_cursor_col = 0
        self.device.toggle_lcd_event_flag()
        self.device.next_screen = ""
        menu = ("* Set ntwk (0-16)", "", "enter", "M")
        for item in menu:
            self.device.next_screen += "{:<20}".format(item)

    def use_keyboard_input(self, kb):
        if kb['enter']:
            self.on_enter()
            return
        if kb['right shift']:
            self.device.function_toggle = not self.device.function_toggle
            self.device.toggle_lcd_event_flag()

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
        if self.device.input_buffer != self.device.next_input_buffer:
            self.device.next_screen = "{}{:<2}{}".format(self.device.current_screen[0:20],
                                                         self.device.next_input_buffer,
                                                         self.device.current_screen[22:])
            self.device.input_buffer = self.device.next_input_buffer

    def on_enter(self):
        if self.device.next_cursor_row == 2 and self.device.next_cursor_col <= 5:
            self.nextState = MainMenu(self.device)
            self.device.lora.set_network_id(self.addr_to_use)

    def write_char(self, c):
        addr = None
        if c in [str(e) for e in range(0, 10)]:
            self.device.next_input_buffer += c
            try:
                addr = int(self.device.next_input_buffer)
                if addr > 16:
                    raise ValueError
                self.device.next_cursor_col = self.device.cursor_col + 1
                self.device.toggle_lcd_event_flag()
            except:
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
        self.device.toggle_lcd_event_flag()
        if self.device.cursor_row < self.device.lcd_height - 1:
            self.device.next_cursor_row = self.device.cursor_row + 1
            if self.device.next_cursor_row == 1:
                self.device.next_cursor_col = len(self.device.input_buffer)
            else:
                self.device.next_cursor_col = 0


class ReceivedMenu(AbstractState):

    def __init__(self, d):
        super().__init__(d)
        self.device.next_cursor_row = 0
        self.device.next_cursor_col = 0
        self.device.function_toggle = False
        self.device.toggle_lcd_event_flag()

    def initial(self):
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

        if self.device.messages.last_message() is None:
            last_message = " "
        else:
            last_message = "L"

        if self.device.messages.next_message() is None:
            next_message = " "
        else:
            next_message = "N"

        if self.device.messages.current_message() is not None:
            address = str(self.device.messages.current_message()["address"])
            data = self.device.messages.current_message()["data"]
            # there is a current_message to draw
            self.device.next_screen = "{}{:<6}{:<40}{:<2} {} {}{}".format(self.device.next_screen[0:14], address,
                                                               data, self.device.next_screen[60:62], last_message,
                                                                      next_message,self.device.next_screen[66:])

    def use_keyboard_input(self, kb):
        if kb['d']:
            if self.device.messages.next_message() is not None:
                # allow them to press the button
                self.device.messages.index += 1
                self.device.toggle_lcd_event_flag()
                return
        if kb['a']:
            if self.device.messages.last_message() is not None:
                self.device.messages.index -= 1
                self.device.toggle_lcd_event_flag()
            return
        if kb['enter']:
            self.on_enter()
            return

    def on_enter(self):
        if self.device.next_cursor_row == 3:
            self.nextState = MainMenu(self.device)


class SendMenu(AbstractState):

    def __init__(self, d):
        super().__init__(d)
        print("States init called")
        self.addr_to_use = None
        self.device.next_cursor_row = 0
        self.device.next_cursor_col = 0
        self.device.function_toggle = False
        self.device.toggle_lcd_event_flag()

    def initial(self):
        print("States initial called")
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
            self.device.toggle_lcd_event_flag()

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
        if self.device.cursor_row == 0:
            self.nextState = SendMenu(self.device)
        if self.device.cursor_row == 1:
            self.nextState = ReceivedMenu(self.device)
        if self.device.cursor_row == 2:
            self.nextState = SettingsMenu(self.device)

    def on_down(self):
        if self.device.cursor_row < self.lowest_row:
            self.device.next_cursor_row = self.device.cursor_row + 1
            self.device.toggle_lcd_event_flag()
