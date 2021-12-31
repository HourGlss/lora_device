from abc import ABC, abstractmethod


class AbstractState(ABC):

    def __init__(self, d):
        self.device = d
        self.nextState = None

    def print_menu(self, strings: tuple):
        # strings = ("* Send", "* Messages", "* Settings")
        row = 0
        # loops through the strings and prints each one a row
        for item in strings:
            # sets the cursor where to print
            self.device.lcd.set_cursor_pos(row, 0)
            # prints the string
            self.device.lcd.print(item)
            # increments to the next row
            row += 1

    def print_error(self, error_message: str):
        """
        put an error message on the menu bar
        :param error_message: the error message to use
        :return: None
        """
        # raises an error when the length of the error message is more than 10
        if len(error_message) > 10:
            raise "Error message too long"
        # sets the row to print
        row = 3
        # sets the column to print
        col = 10
        # loops through the characters of the string
        for char in error_message:
            # sets the cursor where to print
            self.device.lcd.set_cursor_pos(row, col)
            # prints the character
            self.device.lcd.print(char)
            # increments the col until it gets to the second to last cell
            if col < 18:
                col += 1
            else:
                # self explanatory
                raise "String cannot print to bottom right cell of LCD. " \
                      "Crashes for some reason and i am too dumb to figure " \
                      "out why so I just don't print that far."
        # sets the cursor back to the users cursor position
        self.device.lcd.set_cursor_pos(self.device.row, self.device.col)

    @abstractmethod
    def use_keyboard_input(self, kb: dict):
        pass

    @abstractmethod
    def print_input_buffer(self):
        pass

    @abstractmethod
    def update_screen(self):
        pass

    def on_up(self):
        if self.device.row > 0:
            # increments the row
            self.device.row -= 1
            # moves the cursor to the users cursor position
            self.device.lcd.set_cursor_pos(self.device.row, self.device.col)

    def on_down(self):
        if self.device.row < self.device.lcd.height - 1:
            # increments the row
            self.device.row += 1
            # moves the cursor to the users cursor position
            self.device.lcd.set_cursor_pos(self.device.row, self.device.col)

    def on_left(self):
        if self.device.col > 0:
            # decrements the column
            self.device.col -= 1
            # moves the cursor to the users cursor position
            self.device.lcd.set_cursor_pos(self.device.row, self.device.col)

    def on_right(self):
        if self.device.col < self.device.lcd.width - 1:
            # increments the column
            self.device.col += 1
            # moves the cursor to the users cursor position
            self.device.lcd.set_cursor_pos(self.device.row, self.device.col)

    @abstractmethod
    def on_enter(self):
        pass

    @abstractmethod
    def write_char(self, c):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def get_next_state(self):
        pass
