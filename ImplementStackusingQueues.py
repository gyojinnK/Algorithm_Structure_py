import collections


class MyStack:
    def __init__(self):
        self.list = collections.deque()

    def push(self, x:int) -> None:
        self.list.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        else:
            poped = self.list.pop()
            return poped

    def top(self) -> int:
        if self.empty():
            return None
        else:
            return self.list[-1]

    def empty(self) -> bool:
        if not self.list:
            return True
        else:
            return False


obj = MyStack()
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(1)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.empty())