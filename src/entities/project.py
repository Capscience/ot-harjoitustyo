from entities.timer import Timer


class Project:
    """This class represents a cource or project you can time."""

    def __init__(self, name: str, id_: int) -> None:
        self.name = name
        self.timer = Timer()
        self.id_ = id_

    def __repr__(self) -> str:
        return f'<Project name: {self.name}, timer: {self.timer}>'

