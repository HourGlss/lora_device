import board
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import CursorMode
import busio


class Messages(object):

    def __init__(self):
        self.max_messages = 10
        self.messages = []
        self.index = 0

    def add(self, d: dict):
        self.messages.append(d)
        if len(self.messages) > self.max_messages:
            self.messages.pop(0)

    def __getitem__(self, item):
        return self.messages[item]

    def __len__(self):
        return len(self.messages)

    def current_message(self):
        if self.index > len(self.messages) - 1:
            return None
        if self.index < 0:
            return None
        return self.messages[self.index]

    def next_message(self):
        if self.index + 1 > len(self.messages) - 1:
            return None
        return self.messages[self.index + 1]

    def last_message(self):
        if self.index - 1 < 0:
            return None
        return self.messages[self.index - 1]


class Device(object):
    def __init__(self, lcd_to_use, lora_to_use, testled=None, kbsda=None, kbscl=None):
        self.__lcd = lcd_to_use
        self.lcd_height = lcd_to_use.num_rows
        self.lcd_width = lcd_to_use.num_cols
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
        if testled is not None:
            self.test_led = testled
        else:
            self.test_led = None

        self.lcd_event_change_detected = False

        self.input_buffer = ""
        self.next_input_buffer = ""
        if kbscl is not None and kbsda is not None:
            self.use_i2c_kb = True
            self.setup_i2c_keyboard(scl=kbscl, sda=kbsda)
            self.kb_i2c = None
            self.cardkb = None
        else:
            self.use_i2c_kb = False
            self.setup_keyboard()
            self.kb_cols = None
            self.kb_pins = None
            self.kb_rows = None

    def get_keyboard_input(self):

        all_possible = self.__build_all_possible()
        meaning = [
            ['a', 'w', 'right shift', '1']
            ,
            ['s', 'd', 'enter', 'backspace'],
        ]

        c = 0
        if self.test_led is not None:
            self.test_led.value = True
        for cpin in self.kb_cols:
            r = 0
            cpin.value = True
            for rpin in self.kb_rows:
                if rpin.value:
                    all_possible[meaning[c][r]] = True
                r += 1
            c += 1
            cpin.value = False
        if self.test_led is not None:
            self.test_led.value = False

        if self.__last_keyboard != all_possible:
            self.__last_keyboard = all_possible
            return all_possible
        else:
            return None

    def setup_keyboard(self):
        self.kb_pins = {
            "out": [board.GP7, board.GP9],
            "in": [board.GP6, board.GP8, board.GP10, board.GP11]
        }
        self.kb_rows = []
        self.kb_cols = []
        for type_of_input, pins in self.kb_pins.items():
            for pin in pins:
                temp = None
                if type_of_input == "in":
                    temp = DigitalInOut(pin)
                    temp.direction = Direction.INPUT
                    temp.pull = Pull.DOWN
                    self.kb_rows.append(temp)
                if type_of_input == "out":
                    temp = DigitalInOut(pin)
                    temp.direction = Direction.OUTPUT
                    temp.value = False
                    self.kb_cols.append(temp)
                del temp
        all_possible = self.__build_all_possible()
        self.__last_keyboard = all_possible

    def __build_all_possible(self):
        return {
            "a": False,
            "b": False,
            "c": False,
            "d": False,
            "e": False,
            "f": False,
            "g": False,
            "h": False,
            "i": False,
            "j": False,
            "k": False,
            "l": False,
            "m": False,
            "n": False,
            "o": False,
            "p": False,
            "q": False,
            "r": False,
            "s": False,
            "t": False,
            "u": False,
            "v": False,
            "w": False,
            "x": False,
            "y": False,
            "z": False,
            "0": False,
            "1": False,
            "2": False,
            "3": False,
            "4": False,
            "5": False,
            "6": False,
            "7": False,
            "8": False,
            "9": False,
            "right shift": False,
            "enter": False,
            "backspace": False,
        }

    def get_i2c_keyboard_input(self):
        all_possible = self.__build_all_possible()
        ESC = chr(27)
        CR = "enter"
        LF = "\n"
        c = ''
        b = bytearray(1)
        self.kb_i2c.readfrom_into(self.cardkb, b)
        c = b.decode()

        if c == "?":
            c = "right shift"

        if b == b'\r':
            c = "enter"

        if b == b'\x00':
            c = None

        if self.__last_keyboard != all_possible:
            if c is not None:
                all_possible[c] = True
                return all_possible
        else:
            return None

    def setup_i2c_keyboard(self, scl, sda):
        self.kb_i2c = busio.I2C(scl=scl, sda=sda)
        while not self.kb_i2c.try_lock():
            pass
        self.cardkb = self.kb_i2c.scan()[0]

    def toggle_lcd_event_flag(self):
        self.lcd_event_change_detected = not self.lcd_event_change_detected

    def print_screen(self):
        lcd_redrawn = False
        self.__lcd.set_cursor_mode(CursorMode.HIDE)
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
                y = i / self.lcd_width
                x = i % self.lcd_width
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
                    y = i / self.lcd_width
                    x = i % self.lcd_width
            self.cursor_row = self.next_cursor_row
            self.cursor_col = self.next_cursor_col
        self.__lcd.set_cursor_pos(self.cursor_row, self.cursor_col)
        if self.function_toggle:
            self.__lcd.draw_cursor("blink")
        else:
            self.__lcd.draw_cursor("line")
        self.toggle_lcd_event_flag()

    def get_message(self):
        data_in = self.lora.read_from_device()
        if data_in is not None:
            self.messages.add(data_in)


if __name__ == "__main__":
    pass
