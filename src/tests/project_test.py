import unittest
from time import sleep
from entities.project import Project

class TestProject(unittest.TestCase):
    """Test class Project."""

    def setUp(self):
        self.p1 = Project('one', 1)
        self.p2 = Project('two', 2)
    
    def test_repr(self):
        out = str(self.p1)
        self.assertEqual(out, '<Project name: one, timer: 00:00:00>')

    def test_different_times(self):
        """Obvious test, but had problems previously..."""

        self.p1.timer.start()
        sleep(1)
        out1 = str(self.p1)
        out2 = str(self.p2)
        self.assertEqual(out1, '<Project name: one, timer: 00:00:01>')
        self.assertEqual(out2, '<Project name: two, timer: 00:00:00>')
