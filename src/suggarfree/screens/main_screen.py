from textual.app import ComposeResult
from textual.screen import Screen

from widgets import Sidebar, Header, Footer


class MainScreen(Screen):

    def compose(self) -> ComposeResult:
        yield Sidebar(id="main-sidebar")
        yield Header(id="main-header")
        yield Footer(id="main-footer")
