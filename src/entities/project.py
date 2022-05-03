from datetime import datetime

from sqlalchemy.orm import Session

from database.database import ProjectData, ENGINE
from entities.timer import Timer


class Project:
    """This class represents a cource or project you can time.

    Args:
        name: Name of the project.
        id_: Unique identifier, same as database entry id.
    """

    def __init__(self, name: str, id_: int) -> None:
        """Class constructor.

        Creates own timer for project.
        """

        self.name = name
        self.timer = Timer()
        self.id_ = id_

    def __repr__(self) -> str:
        """String representation of the class.

        Returns:
            str: String representation with name and timer.
        """
        return f'<Project name: {self.name}, timer: {self.timer}>'

    def save(self) -> None:
        """Save projects timer to database."""

        time = self.timer.stop()
        with Session(ENGINE) as session:
            session.add_all(
                [ProjectData(project_id = self.id_, time = time, date = datetime.today())]
            )
            session.commit()
