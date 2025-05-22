from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import ModalScreen
from textual.widgets import Label, Input, Button


class AddAddrWallet(ModalScreen[str]):

    # CSS específico para este modal - Textual permite CSS inline
    CSS = """
        AddItemScreen {
            align: center middle;  /* Centraliza o modal na tela */
        }

        #add-item-container {
            width: 50;
            height: 10;
            border: solid $primary;  /* $primary é uma variável CSS do tema do Textual */
            background: $surface;
            padding: 1;
        }

        #item-input {
            margin: 1 0;
        }

        #buttons-container {
            height: 3;
            margin-top: 1;
        }

        Button {
            margin: 0 1;
        }
        """

    def compose(self) -> ComposeResult:

        with Vertical(id="modal-add-wallet-addr-container"):
            yield Input(placeholder="Enter wallet hash...", id="input-add-wallet-addr")
            # TODO: add command: enter -> add item
            # TODO: add command: esc -> cancel


    def on_mount(self) -> None:
        self.query_one("#input-add-wallet-addr", Input).focus()

    def on_button_pressed(self, event: Button.Pressed) -> None:

        ...

    def on_input_submitted(self, event: Input.Submitted) -> None:

       ...
