from repos.project_repo import projectrepo


class ProjectService:
    """Service runnig app logic."""

    def __init__(self) -> None:
        self._default_repo = projectrepo
        self._default_repo._initialize()

    def print_data(self) -> None:
        self._default_repo.print_projects()

    def add_project(self, name: str) -> None:
        """Create new project to project repo."""

        self._default_repo.add_project(name.lower())

project_service = ProjectService()
