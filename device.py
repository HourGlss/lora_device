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
        return {"a": True}

    def get_message(self):
        data_in = self.lora.read_from_device()
        if data_in is not None:
            self.messages.add(data_in)


if __name__ == "__main__":
    data = {
        1: "a",
        2: "b"
    }
    data2 = {
        1: "c",
        2: "d"
    }
    data3 = {
        1: "c",
        2: "z"
    }
    data4 = {
        1: "z",
        2: "d"
    }
    data5 = {
        1: "f",
        2: "d"
    }
    data6 = {
        1: "c",
        2: "f"
    }
    data7 = {
        1: "g",
        2: "d"
    }
    data8 = {
        1: "c",
        2: "g"
    }
    data9 = {
        1: "c",
        2: "h"
    }
    data10 = {
        1: "i",
        2: "h"
    }
    data11 = {
        1: "o",
        2: "d"
    }
    m = Messages()
