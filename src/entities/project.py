from datetime import datetime

from database.database import Session, ProjectData

from entities.timer import Timer


class Project:
    """This class represents a cource or project you can time."""

    def __init__(self, name: str, id_: int) -> None:
        self.name = name
        self.timer = Timer()
        self.id_ = id_

    def __repr__(self) -> str:
        return f'<Project name: {self.name}, timer: {self.timer}>'

    def save(self) -> None:
        """Save projects timer to database."""

        time = self.timer.stop()
        Session.add_all([ProjectData(project_id = self.id_, time = time)])
