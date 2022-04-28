from sqlalchemy import select
from sqlalchemy.orm import Session

from entities.project import Project
from database.database import Base, ENGINE, Projects


class ProjectRepository:
    """Class that handles creating and saving new projects."""

    def __init__(self) -> None:
        self._projects = []

        Base.metadata.create_all(ENGINE)

        with Session(ENGINE) as session:
            selection = select(Projects)
            for project in session.scalars(selection):
                self._projects.append(Project(project.name, project.id))
            session.commit()

    def valid_name(self, name: str) -> bool:
        """Check for project with given name.

        Return True if found, else False.
        """

        if name == '':
            return False
        for project in self._projects:
            if project.name == name:
                return False
        return True

    def get_projects(self) -> list:
        """Method to aquire self._projects from outside the class."""

        return self._projects

    def add_project(self, name: str) -> bool:
        """Add new project."""

        name = name.lower()
        if not self.valid_name(name):
            return False
        with Session(ENGINE) as session:
            session.add_all([Projects(name = name)])
            session.commit()
            selection = select(Projects).where(Projects.name.in_([name]))
            for project in session.scalars(selection):
                self._projects.append(Project(project.name, project.id))
                print(project.name, project.id)
            session.commit()
        return True

    def print_projects(self) -> None:
        for project in self._projects:
            print(project.name, project.timer)

    def _update(self) -> None:
        """Read projects from ProjectData."""

        return


projectrepo = ProjectRepository()
