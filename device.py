import keyboard
import logging
import inspect


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
        func = inspect.currentframe().f_back.f_code
        logging.debug("created")
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

        self.lcd_event_change_detected = False

        self.input_buffer = ""

    def get_keyboard_input(self):
        func = inspect.currentframe().f_back.f_code
        # @TODO THIS NEEDS TO CHANGE FOR lora controller implementation
        all_possible = {
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
            "enter": False,
            "right shift": False,  # THIS WILL BE FUNCTION
            "space": False,
            "backspace": False
        }
        for k in all_possible.keys():
            all_possible[k] = keyboard.is_pressed(k)
        if all_possible != self.__last_keyboard:
            self.__last_keyboard = all_possible
            return all_possible
        else:
            return None

    def toggle_lcd_event_flag(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug("Something toggled this flag")
        self.lcd_event_change_detected = not self.lcd_event_change_detected

    def print_screen(self):
        func = inspect.currentframe().f_back.f_code
        logging.debug("print_sceen was called")
        lcd_redrawn = False
        if len(self.next_screen) == 80:
            self.next_screen = self.next_screen[:79]
        if self.next_screen != self.current_screen:
            logging.debug("something actually on the screen changed")
            x = 0
            y = 0
            i = 0
            for c in self.next_screen:
                logging.debug("Printed {}".format(c))
                self.__lcd.set_cursor_pos(y, x)
                self.__lcd.print(str(c))
                i += 1
                y = i / self.__lcd.width
                x = i % self.__lcd.width
            self.current_screen = self.next_screen
            lcd_redrawn = True
            logging.debug("Got past printing")
        if self.next_cursor_row != self.cursor_row or self.next_cursor_col != self.cursor_col:
            logging.debug("the cursor changed")
            self.__lcd.clear()
            if not lcd_redrawn:
                logging.debug("we had to redraw")
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
            logging.debug("changed cursor position and redrew the screen")
        logging.debug("drawing the cursor character")
        self.__lcd.set_cursor_pos(self.cursor_row, self.cursor_col)
        self.__lcd.draw_cursor()
        logging.debug("finished drawing the cursor")
        self.toggle_lcd_event_flag()

    def get_message(self):
        data_in = self.lora.read_from_device()
        if data_in is not None:
            self.messages.add(data_in)


if __name__ == "__main__":
    pass
