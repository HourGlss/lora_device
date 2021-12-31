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
    def print_input_buffer(self):
        # sets the row to print on
        row = 0
        # sets the col to print on
        col = 3
        # sets the cursor where to print
        self.device.lcd.set_cursor_pos(row, col)
        # loops through the characters in the input buffer
        for char in self.device.input_buffer:
            # checks to make sure its not printing on the last column of the row
            if col <= self.device.lcd.width - 1:
                # prints the character
                self.device.lcd.print(char)
                # increments the column
                col += 1
                # moves the cursor to the next col
                self.device.lcd.set_cursor_pos(row, col)
            # checks to see if we are on the last column in line 1 and if so passes
            elif row == self.device.lcd.height - 3 and col == self.device.lcd.width - 1:
                pass
            # passes on every row except the first
            elif row < self.device.lcd.height - 3:
                pass
            # saves the col of the end of the input buffer
            self.device.text_row = row
            # saves the row of the end of the input buffer
            self.device.text_col = col
        # sets the cursor back to the users cursor position
        self.device.lcd.set_cursor_pos(self.device.row, self.device.col)

    def update_screen(self):
        self.print_menu(("To:", "Compose", "", "M"))
        # if there is an error it will display it on the bottom line
        if self.device.error_message is not None:
            # prints the error message
            self.print_error(self.device.error_message)

    def on_enter(self):
        if self.device.row == 1 and self.device.col <= 7:
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
