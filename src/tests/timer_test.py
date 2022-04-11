import unittest
from time import sleep
from entities.timer import Timer

class TestTimer(unittest.TestCase):
    """Test class Timer.
    
    Test class methods, check that times are correct,
    and especially that rounding is correct.
    """
    def setUp(self):
        self.timer = Timer()
    
    def test_start_current_stop(self):
        self.timer.start()
        sleep(2)
        ret = str(self.timer)
        self.assertEqual(ret, '00:00:02')
        sleep(2)
        ret = self.timer.stop()
        self.assertEqual(ret, 4.0)
    
    def test_pause(self):
        self.timer.start()
        sleep(1)
        self.timer.pause()
        sleep(1)
        self.timer.start()
        sleep(1)
        ret = self.timer.stop()
        self.assertEqual(ret, 2.0)
    
    def test_halfrounding(self):
        self.timer.start()
        sleep(0.1)
        ret = str(self.timer)
        self.assertEqual(ret, '00:00:00')
        sleep(0.4)
        ret = str(self.timer)
        self.assertEqual(ret, '00:00:00')
        sleep(1)
        ret = self.timer.stop()
        self.assertEqual(ret, 1.5)
    
    def test_pause_while_paused(self):
        self.timer.pause()
        self.timer.start()
        sleep(0.5)
        ret = self.timer.stop()
        self.assertEqual(ret, 0.5)
    
    def test_start_while_running(self):
        self.timer.start()
        self.timer.start()
        sleep(0.5)
        ret = self.timer.stop()
        self.assertEqual(ret, 0.5)