class Jar:
    def __init__(self, _capacity=12):
        if _capacity < 0:
            raise ValueError
        self._cookie = 0
        self._capacity = _capacity

    def __str__(self):
        return "🍪" * self._cookie

    def deposit(self, n):
        if self._cookie + n > self.capacity:
            raise ValueError("Cookies have reach theire capacity")
        self._cookie += n

    def withdraw(self, n):
        if n > self._cookie:
            raise ValueError("N was greater than cookie amount")
        self._cookie -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookie
