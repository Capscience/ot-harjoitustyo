from gui.mainview import MainView


class GUI:
    """Class that handles all GUI interactions."""

    def __init__(self, root) -> None:
        self._root = root
        self._open = None

    def start(self) -> None:
        """Start GUI."""

        self._show_mainview()

    def _kill_current_view(self) -> None:
        """Destroy currently open view if exists."""

        if self._open:
            self._open.destroy()
        self._open = None

    def _show_mainview(self) -> None:
        """Start MainView class to show main view."""

        self._kill_current_view()

        self._open = MainView(
            self._root
        )
