from state.state import AbstractState


class MainMenu(AbstractState):

    def __init__(self, d):
        super().__init__(d)

    def get_next_state(self):
        pass

    def use_keyboard_input(self, kb):
        print(kb)

    def print_input_buffer(self):
        pass

    def update_screen(self):

        self.print_menu(("* Send", "* Messages", "* Settings"))
        # if there is an error it will display it on the bottom line
        if self.device.error_message is not None:
            # prints the error message
            self.print_error(self.device.error_message)

    def on_enter(self):
        pass

    def write_char(self, c):
        pass

    def delete(self):
        pass
