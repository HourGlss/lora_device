from state.state import AbstractState


class ComposeMenu(AbstractState):

    def __init__(self, d):
        super().__init__(d)

    def get_next_state(self):
        pass

    def use_keyboard_input(self, kb):
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
