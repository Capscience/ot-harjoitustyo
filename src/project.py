from timer import Timer

class Project:
    """This class represents a cource or project you can time."""

    def __init__(self, name: str, timer: Timer) -> None:
        self.name = name
        self.timer = Timer()
        print(self.timer)