from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Static


class Sidebar(Vertical):

    def compose(self) -> ComposeResult:
        yield Static("Wallets", id="sidebar-title")
