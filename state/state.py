from abc import ABC, abstractmethod
import inspect
import logging
class AbstractState(ABC):

    def __init__(self, d):
        func = inspect.currentframe().f_back.f_code
        logging.debug("created")
        self.device = d
        self.nextState = None

    def print_error(self, error_message: str):
        pass

    @abstractmethod
    def use_keyboard_input(self, kb: dict):
        pass

    @abstractmethod
    def print_input_buffer(self):
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
