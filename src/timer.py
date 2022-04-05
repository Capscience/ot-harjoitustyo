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
    
    def start(self) -> None:
        """Start new or paused timer."""

        if self.__running:
            return
        self.__start = time.time()
        self.__running = True

    def current(self) -> float:
        """Print duration so far."""

        total = sum(self.__times) + time.time() - self.__start
        return round(total * 2) / 2 # total/3600 later to get hours

    def pause(self) -> float:
        """Pause timer, use start() to continue.
        
        Return worktime so far.
        """

        if not self.__running:
            return
        stop = time.time()
        self.__times.append(stop - self.__start)
        self.__running = False

        total = sum(self.__times)
        return round(total * 2) / 2 # total/3600 later to get hours

    def stop(self) -> float:
        """Stop timer and return worktime.
        
        Worktime is rounded to the nearest half or whole second.
        """
        
        time = self.pause()
        self.__times = 0
        return time