import time


class Timer:
    """Timer class for workhour counter."""

    def __init__(self) -> None:
        """Class init method.

        Create Timer object, starts at 0.
        """

        self.__times = []
        self.__start = 0
        self.__running = False

    def __str__(self) -> str:
        """String form of timer."""

        total = int(sum(self.__times) + time.time() - self.__start)
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
        stop = time.time()
        self.__times.append(stop - self.__start)
        self.__running = False

        total = sum(self.__times)
        return round(total * 2) / 2 # total/3600 later to get hours

    def stop(self) -> float:
        """Stop timer and return worktime.

        Worktime is rounded to the nearest half or whole second.
        """

        worktime = self.pause()
        self.__times = 0
        return worktime
