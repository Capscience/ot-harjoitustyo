from database.tables import Projects
from entities.project import Project
from database.database import Session, Base, engine


class ProjectRepository:
    """Class that handles creating and saving new projects."""

    def __init__(self, session: Session) -> None:
        self._projects = []
        self._session = session

    def _update(self) -> None:
        """Read projects from ProjectData."""

        self._session.
    
    def _initialize(self) -> None:
        """Initialize database and get data if there is any."""

        Base.metadata.create_all(engine)

projectrepo = ProjectRepository()
