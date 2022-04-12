from tkinter import Tk
from gui.gui import GUI


def main() -> None:
    """Start project timer app."""

    root = Tk()
    root.title('Project Timer')
    root.geometry('1280x720')

    window = GUI(root)
    window.start()

    root.bind('<Configure>', window.resize)

    root.mainloop()


if __name__ == '__main__':
    main()
