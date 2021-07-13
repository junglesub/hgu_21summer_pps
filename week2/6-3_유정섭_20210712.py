from collections import deque


class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__st1 = deque()
        self.__st2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.__st1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.__st2:
            for x in range(len(self.__st1)):
                self.__st2.append(self.__st1.pop())
        return self.__st2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.__st2:
            return self.__st1[0]
        return self.__st2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.__st1 and not self.__st2

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
# obj.push(1)
# obj.push(2)
param_2 = obj.pop()
# param_3 = obj.peek()
param_4 = obj.empty()
print(param_2)
print(param_4)
