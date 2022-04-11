from timer import Timer

class Project:
    """This class represents a cource or project you can time."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.timer = Timer()

if __name__ == '__main__':
    p = Project('Ohte')
    print(p.timer)
