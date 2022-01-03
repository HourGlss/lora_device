from state.state import AbstractState


class ReceivedMenu(AbstractState):

    def __init__(self, d):
        super().__init__(d)

    def get_next_state(self):
        pass

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
        pass

    def print_input_buffer(self):
        pass

    def update_screen(self):
        pass

    def on_enter(self):
        pass

    def write_char(self, c):
        pass

    def delete(self):
        pass
