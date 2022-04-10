from hashlib import new
import tkinter as tk
from tkinter import ttk, constants


class MainView:
    """Class for main window."""

    def __init__(self, root) -> None:
        self._root = root
        self.frame = None
        style = ttk.Style()
        style.configure('BW.TLabel', foreground="black", background="white")

        self._start()
    
    def pack(self) -> None:
        """Pack self._frame."""

        self._frame.pack(fill = constants.BOTH)

    def _start(self) -> None:
        """Initialize view layout."""

        self._frame = tk.Frame(
            master = self._root,
            background = 'black'
        )
        panel1 = ttk.PanedWindow(orient = constants.HORIZONTAL)
        panel1.pack(
            fill = constants.BOTH,
            expand = 1
        )
        panel2 = ttk.PanedWindow(
            master = panel1,
            orient = constants.VERTICAL,
            width = 150
        )
        panel3 = ttk.PanedWindow(
            master=panel1,
            orient = constants.VERTICAL,
            width = 150
        )
        panel1.add(panel2)
        panel1.add(panel3)


        project_area = ttk.LabelFrame(panel2, text = 'This shows current projects', style = 'BW.TLabel')
        panel2.add(project_area)

        new_project_area = ttk.LabelFrame(panel3, text = 'Here we can create new projects', style = 'BW.TLabel')
        menu = ttk.LabelFrame(panel3, text = 'Here we will put menu buttons', style = 'BW.TLabel')
        panel3.add(new_project_area)
        panel3.add(menu)
