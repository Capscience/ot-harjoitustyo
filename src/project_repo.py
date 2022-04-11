from src.database import ProjectData
from entities.project import Project


class ProjectRepository:
    """Class that handles creating and saving new projects."""

    def __init__(self, database: ProjectData) -> None:
        self._projects = []
        self._database = database

    def _initialize(self) -> None:
        """Read projects from ProjectData."""

        pass
