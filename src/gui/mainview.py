import tkinter as tk
from tkinter import CENTER, E, W, ttk,constants,Grid

from services.project_service import project_service


class MainView:
    """Class for main window."""

    def __init__(self, root) -> None:
        self._root = root
        self._frame = None
        self._widgets = []  # storing text widgets for update function
        self._treeview = None
        self._start()

    def pack(self) -> None:
        """Pack self._frame."""

        self._frame.pack(fill = constants.BOTH)

    def update(self, width) -> None:

        size = int(width*0.01)
        # style = ttk.Style()
        # style.theme_use('default')
        # style.map('TreeView')
        # style.configure('Treeview.Heading', font = ('Arial', size))
        # style.configure('Label', font = ('Arial', size))
        for widget in self._widgets:
            widget.config(font = ('Arial', size))

    def _start(self) -> None:
        """Initialize view layout."""

        self._frame = tk.Frame(
            master = self._root,
            background = 'black'
        )
        Grid.rowconfigure(self._root, 0, weight = 1)
        Grid.columnconfigure(self._root, 1, weight = 2, minsize = 200)
        Grid.columnconfigure(self._root, 0, weight = 5)

        left_frame = tk.Frame(self._root, bg='white')
        right_frame = tk.Frame(self._root, bg='white')
        left_frame.grid(row=0, column=0, sticky='nsew')
        right_frame.grid(row=0, column=1, sticky='nsew')

        projects = ttk.Treeview(left_frame)
        self._treeview = projects

        # Define columns for treeview
        projects['columns'] = ('Nimi', 'Ajastin', 'Napit')
        # Format columns
        projects.column('#0', width = 0)
        projects.column('Nimi', anchor = W, width = 1, minwidth = 1)
        projects.column('Napit', anchor = CENTER, width = 1, minwidth = 1)
        projects.column('Ajastin', anchor = E, width = 1, minwidth = 1)
        # Headings for columns
        projects.heading('Nimi', text = 'Nimi', anchor = W)
        projects.heading('Napit', text = 'Start/Stop/Pause', anchor = CENTER)
        projects.heading('Ajastin', text = 'Ajastin', anchor = E)

        projects.insert(
            parent = '',
            index = 'end',
            iid = 0,
            text = '',
            values = ('Ohte', '00:00:00', 'Tähän napit')
        )

        Grid.columnconfigure(left_frame, 0, weight = 1)
        Grid.rowconfigure(left_frame, 0, weight = 1)
        projects.grid(row = 0, column = 0, pady=20, padx=20, sticky = 'nsew')

        # New project creation area
        new_project_label = ttk.Label(right_frame, text = 'Luo uusi projekti', font = ('Arial', 18))
        new_project_label.grid(row = 0, column = 0, pady=20, padx=20, sticky='n')

        project_name_label = ttk.Label(right_frame, text = 'Projektin nimi:', font = ('Arial', 12))
        project_name = ttk.Entry(right_frame)
        project_name_label.grid(row = 1, column = 0, pady=10, padx=10, sticky='new')
        project_name.grid(row = 2, column = 0, pady=10, padx=10, sticky='new')

        create_project = ttk.Button(
            right_frame,
            command = lambda:[project_service.add_project(project_name.get()),
            project_name.delete(0, 'end'),
            project_service.print_data()],
            text = 'Lisää projekti'
        )
        create_project.grid(row = 3, column = 0, pady=10, padx=10, sticky='new')

        Grid.columnconfigure(right_frame, 0, weight = 1)
        Grid.rowconfigure(right_frame, 0, weight = 1)
        Grid.rowconfigure(right_frame, 1, weight = 1)
        Grid.rowconfigure(right_frame, 2, weight = 1)
        Grid.rowconfigure(right_frame, 3, weight = 1)
