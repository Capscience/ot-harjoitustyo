from tkinter import Tk
from gui.gui import GUI


def main() -> None:
    """Start project timer app."""

    root = Tk()
    root.title('Project Timer')

    window = GUI(root)
    window.start()

    root.mainloop()


if __name__ == '__main__':
    main()
