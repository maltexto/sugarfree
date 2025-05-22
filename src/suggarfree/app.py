from textual.app import App

from screens import MainScreen


class Sugarfree(App):

    CSS_PATH = "suggarfree.tcss"
    ENABLE_COMMAND_PALETTE = False
    BINDINGS = [
        ("ctrl+q", "quit", "Quit"),
        ("ctrl+d", "toggle_dark", "Toggle dark mode"),
    ]
    SCREENS = {"main_screen": MainScreen}

    def on_mount(self) -> None:
        self.push_screen("main_screen")


if __name__ == "__main__":
    app = Sugarfree()
    app.run()
