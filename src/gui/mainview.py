import tkinter as tk
from tkinter import ttk, Grid
from datetime import datetime

from repos.project_repo import projectrepo


class MainView:
    """Class for main window.

    Args:
        root: Root window where view is placed.
    """

    def __init__(self, root) -> None:
        """Class constructor.

        Saves root window, and frames that divide the view to sections.
        ProjectControllers are saved to a list for easy handling.
        """
        self._root = root
        self._frame = None
        self._controllers = []
        self._left_frame = None
        self._right_frame = None
        self._stats_label = None
        self._start()

    def _start(self) -> None:
        """Initialize view layout."""

        # Create main frame
        self._frame = tk.Frame(
            master = self._root,
            background = 'black'
        )
        Grid.rowconfigure(self._root, 0, weight = 1)    # Fills root height
        # Divide window to 2 frames in 5:2 width ratio
        Grid.columnconfigure(self._root, 1, weight = 2, minsize = 200)
        Grid.columnconfigure(self._root, 0, weight = 5)

        # Create and grid dividing frames
        self._left_frame = tk.Frame(self._root, bg='white')
        self._right_frame = tk.Frame(self._root, bg='white')
        self._left_frame.grid(row = 0, column = 0, sticky = 'nsew')
        self._right_frame.grid(row = 0, column = 1, sticky = 'nsew')

        # Create ProjectControllers for each project
        self._create_project_controllers(self._left_frame)
        # New project creation area
        self._create_new_project_area(self._right_frame)
        # Project deletion area
        self._create_delete_project_area(self._right_frame)
        # Statistics area
        self._create_statistics_area(self._right_frame)

    def _create_project_controllers(self, root) -> None:
        """Get projects from repo and create ProjectControllers for them.

        Args:
            root: Root frame where controllers are placed."""

        Grid.columnconfigure(root, 0, weight = 1)   # Fills root width
        header = tk.Label(root, text = 'Projektisi tällä hetkellä', font = ('Arial', 18))
        header.grid(row = 0, column = 0, pady = 20, padx = 20, sticky = 'n')

        # Destroy existing controllers so no duplicates are created
        if len(self._controllers) != 0:
            for controller in self._controllers:
                controller.destroy()

        # Create new controllers
        for i, project in enumerate(projectrepo.get_projects()):
            controller = ProjectController(root, project)
            controller.grid(i+1)    # Stack controllers on top of each other
            controller.update()     # Restart GUI timer update cycle for runnig timers
            self._controllers.append(controller)

    def _create_new_project_area(self, root) -> None:
        """Create section where new projects can be added.

        Section is placed in first 4 rows of given root.

        Args:
            root: Root frame where area is placed.
        """

        Grid.columnconfigure(root, 0, weight = 1)   # Column 0 fills width of root
        new_project_label = ttk.Label(root, text = 'Luo uusi projekti', font = ('Arial', 18))
        new_project_label.grid(row = 0, column = 0, pady = 20, padx = 20, sticky = 'n')

        project_name_label = ttk.Label(root, text = 'Projektin nimi:', font = ('Arial', 12))
        project_name = ttk.Entry(root)
        project_name_label.grid(row = 1, column = 0, pady = 10, padx = 10, sticky = 'nsew')
        project_name.grid(row = 2, column = 0, pady = 10, padx = 10, sticky = 'nsew')

        create_project = ttk.Button(
            root,
            command = lambda:[self._create_project(project_name.get()),
            project_name.delete(0, 'end'),
            self._create_project_controllers(self._left_frame)],
            text = 'Lisää projekti'
        )
        create_project.grid(row = 3, column = 0, pady = 10, padx = 10, sticky =' new')

    def _create_project(self, name) -> None:
        """Create project function for button.

        Args:
            name: Name of the project that is going to be saved and displayed.
        """

        # Try adding the project and print message accordingly
        if projectrepo.add_project(name):
            message = 'Lisäys onnistui!'
        else:
            message = 'Virheellinen syöte.\n Anna projektin nimeksi yksi sana, joka\n' + \
            ' voi sisältää isoja ja pieniä kirjaimia sekä numeroita'
        display_message = ttk.Label(
            self._right_frame,
            text = message,
            font = ('Arial', 12)
        )
        display_message.grid(row = 4, column = 0, pady = 10, padx = 10, sticky = 'nsew')
        display_message.after(5000, display_message.destroy)    # Displays message for 5s

    def _create_delete_project_area(self, root) -> None:
        """Create area where projects can be deleted.

        Args:
            root: Root frame where area is placed.
        """

        Grid.columnconfigure(root, 0, weight = 1)
        delete_label = ttk.Label(root, text = 'Poista projekti', font = ('Arial', 18))
        # Leave one empty row for error messages, so row numbering starts from 5
        delete_label.grid(row = 5, column = 0, pady = 20, padx = 20, sticky = 'n')

        project_name_label = ttk.Label(
            root,
            text = 'Poistettavan projektin nimi:',
            font = ('Arial', 12)
        )
        project_name = ttk.Entry(root)
        project_name_label.grid(row = 6, column = 0, pady = 10, padx = 10, sticky = 'nsew')
        project_name.grid(row = 7, column = 0, pady = 10, padx = 10, sticky = 'nsew')

        delete_project = ttk.Button(
            root,
            command = lambda:[self._delete_project(project_name.get()),
            project_name.delete(0, 'end'),
            self._create_project_controllers(self._left_frame)],
            text = 'Poista projekti'
        )
        delete_project.grid(row = 8, column = 0, pady = 10, padx = 10, sticky =' new')

    def _delete_project(self, name: str) -> None:
        """Delete project with given name and all data connected to it.

        Args:
            name: Name of the project that will be deleted.
        """

        if projectrepo.delete_project(name):
            message = 'Projekti poistettu.'
        else:
            message = 'Projektia ei löytynyt.'
        display_message = ttk.Label(
            self._right_frame,
            text = message,
            font = ('Arial', 12)
        )
        display_message.grid(row = 9, column = 0, pady = 10, padx = 10, sticky = 'nsew')
        display_message.after(5000, display_message.destroy)

    def _create_statistics_area(self, root) -> None:
        """Create area where statistics are shown.

        Args:
            root: Root frame where the area is placed.
        """

        Grid.columnconfigure(root, 0, weight = 1)
        statistics_label = ttk.Label(root, text = 'Statistiikat', font = ('Arial', 18))
        # Leave one empty row for error messages, so row numbering starts from 10
        statistics_label.grid(row = 10, column = 0, pady = 20, padx = 20, sticky = 'n')

        project_name_label = ttk.Label(
            root,
            text = 'Anna aikamääre (yyyy-mm tai yyyy-mm-dd, tyhjä antaa koko historian.)',
            font = ('Arial', 12)
        )
        timeframe = ttk.Entry(root)
        project_name_label.grid(row = 11, column = 0, pady = 10, padx = 10, sticky = 'nsew')
        timeframe.grid(row = 12, column = 0, pady = 10, padx = 10, sticky = 'nsew')

        search_stats = ttk.Button(
            root,
            command = lambda:[self._get_statistics(root, timeframe.get()),
            timeframe.delete(0, 'end')],
            text = 'Hae tiedot'
        )
        search_stats.grid(row = 13, column = 0, pady = 10, padx = 10, sticky =' new')
        self._get_statistics(root, datetime.today().strftime('%Y-%m'))  # Get default stats

    def _get_statistics(self, root, timestr: str) -> None:
        """Creates and gets the statistics of given timeframe.

        Args:
            root: Root frame where stats will be displayed.
            timestr: Datetime-like string. Used to get stats for certain month or day.
                Use empty string to get all data.
        """

        if self._stats_label is not None:
            self._stats_label.destroy()
        text = projectrepo.get_stats(timestr)
        self._stats_label = ttk.Label(root, text = text, font = ('Courier', 14))
        self._stats_label.grid(row = 14, column = 0, pady = 10, padx = 10, sticky =' new')

    def destroy(self) -> None:
        """Destroy the main frame."""

        self._frame.destroy()


class ProjectController:
    """GUI class to control project timers.

    Args:
        root: Root frame where controllers are placed.
        project: Project object for the controller to control.
    """

    def __init__(self, root, project) -> None:
        """Class constructor.

        self._text is needed to update time easily while timer is running.
        """
        self._project = project
        self._text = tk.StringVar()
        self._text.set(str(self._project.timer))
        self._frame = tk.Frame(
            master = root,
            background = 'grey'
        )
        self.name = tk.Label(
            self._frame,
            text = f' {self._project.name:<12}',
            font = ('Courier', 14)
        )
        self.time = tk.Label(
            self._frame,
            textvariable = self._text,
            font = ('Courier', 14)
        )
        self.play = tk.Button(
            self._frame,
            text = 'Play',
            command = lambda:[self._play(), self.update()]
        )
        self.pause = tk.Button(
            self._frame,
            text = 'Pause',
            command = lambda:[self._pause(), self.update()]
        )
        self.stop = tk.Button(
            self._frame,
            text = 'Stop',
            command = lambda:[self._stop(), self.update()]
        )

    def grid(self, row: int) -> None:
        """Place ProjectController on screen.

        Args:
            row: Tells which row controller is placed on. """

        self.name.grid(row = 0, column = 0, padx = 10, pady = 2, sticky = 'w')
        self.time.grid(row = 0, column = 1, padx = 10, pady = 2, sticky = 'e')
        self.play.grid(row = 0, column = 2, padx = 10, pady = 2, sticky = 'e')
        self.pause.grid(row = 0, column = 3, padx = 10, pady = 2, sticky = 'e')
        self.stop.grid(row = 0, column = 4, padx = 10, pady = 2, sticky = 'e')
        self._frame.grid(row = row, pady = 5, padx = 5, sticky = 'nsew')
        Grid.columnconfigure(self._frame, 0, weight = 3)
        Grid.columnconfigure(self._frame, 1, weight = 3)
        Grid.columnconfigure(self._frame, 2, weight = 1)
        Grid.columnconfigure(self._frame, 3, weight = 1)
        Grid.columnconfigure(self._frame, 4, weight = 1)

    def _play(self) -> None:
        """Start or restart project's timer."""

        self._project.timer.start()

    def _pause(self) -> None:
        """Pause project's timer."""

        self._project.timer.pause()

    def _stop(self) -> None:
        """Stop project's timer."""

        self._project.save()

    def destroy(self) -> None:
        """Destroy main frame of controller."""

        self._frame.destroy()

    def update(self) -> None:
        """Update timer of self._project every 1000 ms."""

        self._text.set(str(self._project.timer))
        self.time.after(1000, self.update)
