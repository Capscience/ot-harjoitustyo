import time


class Timer:
    """Timer class for workhour counter."""

    def __init__(self) -> None:
        """Class constructor.

        Create Timer object, starts at 0.
        """

        self.__times = []   # Save times when paused
        self.__start = 0    # Start time for calculating time difference
        self.__stop = 0     # Stop time
        self.__running = False  # Tells methods if timer is running

    def __repr__(self) -> str:
        """String form of timer.

        Returns:
            str: Time in hh:mm:ss format.
        """

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

    def pause(self) -> str:
        """Pause timer, can be restarted.

        Returns:
            self.__repr__(): String representation of the class.
        """

        if not self.__running:
            return None
        self.__stop = time.time()
        self.__times.append(self.__stop - self.__start)
        self.__running = False

        return self.__repr__()

    def stop(self) -> int:
        """Stop timer and return worktime.

        Returns:
            total: Total worktime in seconds.
        """

        if self.__running:
            total = int(sum(self.__times) + time.time() - self.__start)
        else:
            total = int(sum(self.__times))
        self.__running = False
        self.__times = []
        self.__start = 0
        self.__stop = 0
        return total
