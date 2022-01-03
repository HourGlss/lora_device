import keyboard

class Messages(object):

    def __init__(self):
        self.max_messages = 10
        print("------")
        self.messages = []
        print(self.messages)

    def add(self, d: dict):
        self.messages.append(d)
        if len(self.messages) > self.max_messages:
            self.messages.pop(0)


class Device(object):
    def __init__(self, lcd_to_use, lora_to_use):
        self.lcd = lcd_to_use
        self.lora = lora_to_use
        self.messages = Messages()
        self.error_message = None
        self.text_row = 0
        self.row = 0
        self.text_col = 0
        self.col = 0

        self.input_buffer = ""

    def get_keyboard_input(self):
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
            "enter":False,
            "right shift":False, # THIS WILL BE FUNCTION
            "space":False,
            "backspace":False
        }
        pressing = keyboard.read_key()
        if pressing in all_possible.keys():
            all_possible[pressing] = True
        return all_possible

    def get_message(self):
        data_in = self.lora.read_from_device()
        if data_in is not None:
            self.messages.add(data_in)

    def setup_keyboard(self):
        pass




if __name__ == "__main__":
    pass
