from database.tables import Projects
from entities.project import Project
from database.database import Session,Base,engine


class ProjectRepository:
    """Class that handles creating and saving new projects."""

    def __init__(self, session: Session) -> None:
        self._projects = []
        self._session = session

    def check(self, name: str) -> bool:
        """Check for project with given name.
        
        Return True if found, else False.
        """

        for project in self._projects:
            if project.name == name:
                return True
        return False

    def add_project(self, name: str) -> bool:
        """Add new project."""

        if self.check(name):
            return False
        self._projects.append(Project(name.lower()))

    def print_projects(self) -> None:
        for project in self._projects:
            print(project.name, project.timer)

    def _update(self) -> None:
        """Read projects from ProjectData."""

        return

    def _initialize(self) -> None:
        """Initialize database and get data if there is any."""

        Base.metadata.create_all(engine)

projectrepo = ProjectRepository(Session)
