class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.Queue = []
        

    def enQueue(self, value: int) -> bool:
        if len(self.Queue) < self.k:
            self.Queue.insert(0,value)
            return True
        return False

    def deQueue(self) -> bool:
        if self.Queue:
            self.Queue.pop()
            return True
        return False


    def Front(self) -> int:
        if self.Queue:
            return self.Queue[-1]
            return True
        return -1

    def Rear(self) -> int:
        if self.Queue:
            return self.Queue[0]
            return True
        return -1
        

    def isEmpty(self) -> bool:
        return len(self.Queue) == 0
        

    def isFull(self) -> bool:
        return len(self.Queue) == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()