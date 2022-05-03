import tkinter as tk
from tkinter import ttk, constants, Grid

from repos.project_repo import projectrepo


class MainView:
    """Class for main window."""

    def __init__(self, root) -> None:
        self._root = root
        self._frame = None
        self._widgets = []  # storing text widgets for update function
        self._controllers = []
        self._left_frame = None
        self._right_frame = None
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

        self._left_frame = tk.Frame(self._root, bg='white')
        self._right_frame = tk.Frame(self._root, bg='white')
        self._left_frame.grid(row = 0, column = 0, sticky = 'nsew')
        self._right_frame.grid(row = 0, column = 1, sticky = 'nsew')

        # make custom class instead of Treeview
        self._create_project_controllers(self._left_frame)
        # self.__dev_create_controllers(left_frame)
        # New project creation area
        self._create_new_project_area(self._right_frame)

    def _create_new_project_area(self, root) -> None:

        Grid.columnconfigure(root, 0, weight = 1)
        new_project_label = ttk.Label(root, text = 'Luo uusi projekti', font = ('Arial', 18))
        new_project_label.grid(row = 0, column = 0, pady = 20, padx = 20, sticky = 'n')

        project_name_label = ttk.Label(root, text = 'Projektin nimi:', font = ('Arial', 12))
        project_name = ttk.Entry(root)
        project_name_label.grid(row = 1, column = 0, pady = 10, padx = 10, sticky = 'nsew')
        project_name.grid(row = 2, column = 0, pady = 10, padx = 10, sticky = 'nsew')

        create_project = ttk.Button(
            root,
            command = lambda:[projectrepo.add_project(project_name.get()),
            project_name.delete(0, 'end'),
            projectrepo.print_projects(),
            self._create_project_controllers(self._left_frame)],
            text = 'Lisää projekti'
        )
        create_project.grid(row = 3, column = 0, pady = 10, padx = 10, sticky =' new')

    def _create_project_controllers(self, root) -> None:
        """Get projects from repo and create ProjectControllers for them."""

        Grid.columnconfigure(root, 0, weight = 1)
        header = tk.Label(root, text = 'Projektisi tällä hetkellä', font = ('Arial', 18))
        header.grid(row = 0, column = 0, pady = 20, padx = 20, sticky = 'n')
        if len(self._controllers) != 0:
            for controller in self._controllers:
                controller.destroy()

        for i, project in enumerate(projectrepo.get_projects()):
            controller = ProjectController(root, project)
            controller.grid(i+1)
            self._controllers.append(controller)

    def destroy(self) -> None:
        self._frame.destroy()


class ProjectController:
    """GUI class to control project timers."""

    def __init__(self, root, project) -> None:
        self._project = project
        self._text = tk.StringVar()
        self._text.set(str(self._project.timer))
        self._frame = tk.Frame(
            master = root,
            background = 'grey'
        )
        self.name = tk.Label(self._frame, text = self._project.name, font = ('Arial', 12))
        self.time = tk.Label(self._frame, textvariable = self._text, font = ('Arial', 12))
        self.play = tk.Button(
            self._frame,
            text = 'Play',
            command = lambda:[self._play(), print('play'), self.update()]
        )
        self.pause = tk.Button(
            self._frame,
            text = 'Pause',
            command = lambda:[self._pause(), print('pause'), self.update()]
        )
        self.stop = tk.Button(
            self._frame,
            text = 'Stop',
            command = lambda:[self._stop(),print('stop'), self.update()]
        )

    def grid(self, row) -> None:
        """Place ProjectController on screen."""

        self.name.grid(row = 0, column = 0, padx = 10, pady = 2, sticky = 'w')
        self.time.grid(row = 0, column = 1, padx = 10, pady = 2, sticky = 'e')
        self.play.grid(row = 0, column = 2, padx = 10, pady = 2, sticky = 'e')
        self.pause.grid(row = 0, column = 3, padx = 10, pady = 2, sticky = 'e')
        self.stop.grid(row = 0, column = 4, padx = 10, pady = 2, sticky = 'e')
        self._frame.grid(row = row, pady = 5, padx = 5, sticky = 'nsew')
        Grid.columnconfigure(self._frame, 0, weight = 2)
        Grid.columnconfigure(self._frame, 1, weight = 1)
        Grid.columnconfigure(self._frame, 2, weight = 1)
        Grid.columnconfigure(self._frame, 3, weight = 1)
        Grid.columnconfigure(self._frame, 4, weight = 1)

    def _play(self) -> None:
        self._project.timer.start()

    def _pause(self) -> None:
        self._project.timer.pause()

    def _stop(self) -> None:
        self._project.save()

    def destroy(self) -> None:
        self._frame.destroy()

    def update(self) -> None:
        self._text.set(str(self._project.timer))
        self.time.after(1000, self.update)
