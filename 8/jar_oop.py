"""
class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self.size -= n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
        
jar = Jar()
jar.deposit(5)
jar.withdraw(3)
print(jar)




"""



class Jar:
    
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self._size * "🍪"
        

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError
        self.size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError
        self.size += n
        

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

jar = Jar()
jar.deposit(5)
jar.withdraw(3)
print(jar)

