from threading import Lock


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zerolock = Lock()
        self.evenlock = Lock()
        self.oddlock = Lock()

        self.evenlock.acquire()
        self.oddlock.acquire()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.zerolock.acquire()
            printNumber(0)

            if i % 2 == 0:
                self.evenlock.release()
            else:
                self.oddlock.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for k in range(1, self.n + 1, 2):
            self.oddlock.acquire()
            printNumber(k)

            self.zerolock.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for j in range(2, self.n + 1, 2):
            self.evenlock.acquire()
            printNumber(j)

            self.zerolock.release()




