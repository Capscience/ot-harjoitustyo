import time


class Timer:
    """Timer class for workhour counter."""

    def __init__(self) -> None:
        """Class init method.

        Create Timer object, starts at 0.
        """
        self.__times = []
        self.__start = 0
        self.__stop = 0
        self.__running = False

    def __repr__(self) -> str:
        """String form of timer."""

        if self.__start == 0:
            return '00:00:00'
        if self.__running:
            total = int(sum(self.__times) + time.time() - self.__start)
        else:
            total = int(sum(self.__times))
        hours = total // 3600
        minutes = total%3600 // 60
        seconds = total%60
        return f'{hours:02d}:{minutes:02d}:{seconds:02d}'

    def start(self) -> None:
        """Start new or paused timer."""
        if self.__running:
            return
        self.__start = time.time()
        self.__running = True

    def pause(self) -> float:
        """Pause timer, use start() to continue.

        Return worktime so far.
        """

        if not self.__running:
            return None
        self.__stop = time.time()
        self.__times.append(self.__stop - self.__start)
        self.__running = False

        return self.__repr__()

    def stop(self) -> float:
        """Stop timer and return worktime.

        Worktime is rounded to the nearest half or whole second.
        """

        worktime = self.pause()
        self.__times = []
        return worktime
