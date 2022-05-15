import unittest
from time import sleep
from repos.project_repo import ProjectRepository
from sqlalchemy import delete
from sqlalchemy.orm import Session
from database.database import ENGINE, Projects

class TestRepo(unittest.TestCase):
    """Test ProjectRepo class."""

    def setUp(self) -> None:
        self.repo = ProjectRepository()
        projects = self.repo.get_projects()
        self.length = len(projects)

    def test_add_project(self):
        add_empty = self.repo.add_project('')
        self.assertEqual(add_empty, 0)
        add_testi = self.repo.add_project('testi')
        self.assertEqual(add_testi, 2)
        self.assertEqual(len(self.repo.get_projects()), self.length + 1)

    def test_add_same_name(self):
        add_same = self.repo.add_project('testi')
        self.assertEqual(add_same, 0)

    def test_delete_project(self):
        delete_fail = self.repo.delete_project('testi1')
        self.assertEqual(delete_fail, False)
        delete_testi = self.repo.delete_project('testi')
        self.assertEqual(delete_testi, True)
        print(len(self.repo.get_projects()))
        self.assertEqual(self.length - 1, len(self.repo.get_projects()))
    
    def test_delete_tests(self):
        """Delete testi from database completely."""
        with Session(ENGINE) as session:
            deletion = delete(Projects).where(Projects.name == 'testi')
            session.execute(deletion)
            session.commit()