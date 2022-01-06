import board
import busio
import time
from digitalio import DigitalInOut, Direction, Pull

class Messages(object):

    def __init__(self):
        self.max_messages = 10
        self.messages = []

    def add(self, d: dict):
        self.messages.append(d)
        if len(self.messages) > self.max_messages:
            self.messages.pop(0)


class Device(object):
    def __init__(self, lcd_to_use, lora_to_use):
        self.__lcd = lcd_to_use
        self.lcd_height = lcd_to_use.height
        self.lcd_width = lcd_to_use.width
        self.lora = lora_to_use
        self.messages = Messages()
        self.current_screen = None
        self.next_screen = " " * 80
        self.function_toggle = False
        self.error_message = None
        self.text_row = 0
        self.text_col = 0
        self.__last_keyboard = None
        self.cursor_row = 0
        self.cursor_col = 0
        self.next_cursor_row = 0
        self.next_cursor_col = 0
        self.data_to_send = dict()

        self.kb_cols = None
        self.kb_rows = None
        self.pins = None

        self.lcd_event_change_detected = False

        self.input_buffer = ""
        self.next_input_buffer = ""

    def get_keyboard_input(self):
        c = 0
        for cpin in self.kb_cols:
            r = 0
            cpin.value = True
            for rpin in self.kb_rows:
                if rpin.value:
                    # print("SOMETHING")
                    keys_input[c][r] = True
                r += 1
            c += 1
            cpin.value = False

    def setup_keyboard(self):
        self.pins = {
            "out":[board.GP7,board.GP9],
            "in":[board.GP6,board.GP8,board.GP11,board.GP10]
        }
        self.kb_rows = []
        self.kb_cols = []
        for k, v in self.pins.items():
            for e in v:
                temp = None
                if k == "in":
                    temp = DigitalInOut(e)
                    temp.direction = Direction.INPUT
                    temp.pull = Pull.DOWN
                    self.kb_rows.append(temp)
                if k == "out":
                    temp = DigitalInOut(e)
                    temp.direction = Direction.OUTPUT
                    temp.value = False
                    self.kb_cols.append(temp)


    def toggle_lcd_event_flag(self):
        self.lcd_event_change_detected = not self.lcd_event_change_detected

    def print_screen(self):
        lcd_redrawn = False
        if len(self.next_screen) >= 80:
            self.next_screen = self.next_screen[:79]
        if self.next_screen != self.current_screen:
            x = 0
            y = 0
            i = 0
            for c in self.next_screen:
                self.__lcd.set_cursor_pos(y, x)
                # logging.debug("{}".format(str(c)))
                self.__lcd.print(str(c))
                i += 1
                y = i / self.__lcd.width
                x = i % self.__lcd.width
            self.current_screen = self.next_screen
            lcd_redrawn = True
        if self.next_cursor_row != self.cursor_row or self.next_cursor_col != self.cursor_col:
            if not lcd_redrawn:
                x = 0
                y = 0
                i = 0
                for c in self.current_screen:
                    self.__lcd.set_cursor_pos(y, x)
                    self.__lcd.print(str(c))
                    i += 1
                    y = i / self.__lcd.width
                    x = i % self.__lcd.width
            self.cursor_row = self.next_cursor_row
            self.cursor_col = self.next_cursor_col
        self.__lcd.set_cursor_pos(self.cursor_row, self.cursor_col)
        self.__lcd.draw_cursor()
        self.toggle_lcd_event_flag()

    def get_message(self):
        data_in = self.lora.read_from_device()
        if data_in is not None:
            self.messages.add(data_in)


if __name__ == "__main__":
    pass