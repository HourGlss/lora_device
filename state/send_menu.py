from state.state import AbstractState
from state.compose_menu import ComposeMenu

class SendMenu(AbstractState):


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

    def print_input_buffer(self):
        # sets the row to print on
        row = 0
        # sets the col to print on
        col = 3
        # sets the cursor where to print
        self.device.__lcd.set_cursor_pos(row, col)
        # loops through the characters in the input buffer
        for char in self.device.input_buffer:
            # checks to make sure its not printing on the last column of the row
            if col <= self.device.__lcd.width - 1:
                # prints the character
                self.device.__lcd.print(char)
                # increments the column
                col += 1
                # moves the cursor to the next col
                self.device.__lcd.set_cursor_pos(row, col)
            # checks to see if we are on the last column in line 1 and if so passes
            elif row == self.device.__lcd.height - 3 and col == self.device.__lcd.width - 1:
                pass
            # passes on every row except the first
            elif row < self.device.__lcd.height - 3:
                pass
            # saves the col of the end of the input buffer
            self.device.text_row = row
            # saves the row of the end of the input buffer
            self.device.text_col = col
        # sets the cursor back to the users cursor position
        self.device.__lcd.set_cursor_pos(self.device.cursor_row, self.device.cursor_col)

    def screen(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug("changing device.next_screen")
        menu = ("To:", "Compose", " ","M")
        self.device.next_screen = ""
        for item in menu:
            self.device.next_screen += "{:<20}".format(item)


    def on_enter(self):
        if self.device.cursor_row == 1:
            # checks if the input buffer is empty and if so passes
            if self.device.input_buffer != "":
                # transitions to the compose_menu state
                self.nextState = ComposeMenu
                # sets the data_to_send address
                self.data_to_send["address"] = int(self.input_buffer)
                # clears the input buffer
                self.input_buffer = ""

    def write_char(self, c):
        pass

    def delete(self):
        pass
