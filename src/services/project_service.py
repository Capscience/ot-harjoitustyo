from repos.project_repo import projectrepo


class ProjectService:
    """Service runnig app logic."""

    def __init__(self) -> None:
        self._default_repo = projectrepo
        self._default_repo._initialize()

project_service = ProjectService()
