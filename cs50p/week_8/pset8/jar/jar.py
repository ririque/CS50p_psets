class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid number of cookies")
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        return self.size * "🍪"


    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Too many cookies are in the jar. Cannot deposit")
        if self.size + n > self.capacity:
            raise ValueError("Too many cookies are in the jar. Cannot deposit")
        self.size += n


    def withdraw(self, n):
        if self.size < n:
            raise ValueError("There aren't many cookies in the jar. Cannot withdraw")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
