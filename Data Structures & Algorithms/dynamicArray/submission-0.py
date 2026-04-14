class DynamicArray:
    capacity = 0
    length = 0
    def __init__(self, capacity: int):
        self._array = [None] * capacity
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self._array[i]

    def set(self, i: int, n: int) -> None:
        self._array[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.length:
            self.resize()
        self._array[self.length] = n
        self.length +=1

    def popback(self) -> int:

        self.length -=1
        val = self._array[self.length]
        return val
 

    def resize(self) -> None:
        self._array += [None] * self.capacity
        self.capacity = self.capacity * 2


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
