class MyCircularQueue:

    def __init__(self, k: int):
        self.list = [None] * k
        self.max = k
        self.fp = 0
        self.rp = 0

    def enQueue(self, value: int) -> bool:
        if self.list[self.rp] is None:
            self.list[self.rp] = value
            self.rp = (self.rp + 1) % self.max
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.list[self.fp] is not None:
            self.list[self.fp] = None
            self.fp = (self.fp + 1) % self.max
            return True
        else:
            return False

    def Front(self) -> int:
        if self.list[self.fp] is not None:
            return self.list[self.fp]
        else:
            return -1

    def Rear(self) -> int:
        # 값을 추가하고 rear를 하나 옮기기 때문에
        # rear 실제 값을 확인하기 위해서는 -1 인덱스를 해줘야함
        if self.list[self.rp - 1] is not None:
            return self.list[self.rp - 1]
        else:
            return -1

    def isEmpty(self) -> bool:
        for c in self.list:
            if c is not None:
                return False
        return True

    def isFull(self) -> bool:
        for c in self.list:
            if c is None:
                return False
        return True

o = MyCircularQueue(4)
o.enQueue(1)
o.enQueue(2)
o.enQueue(3)
o.enQueue(4)
print(o.Rear())