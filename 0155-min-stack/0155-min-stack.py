from collections import deque
class MinStack(object):
    def __init__(self):
        self.stack=deque()
        self.minimum=deque()

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        if not self.minimum or self.minimum[-1]>=value:
            self.minimum.append(value)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack.pop()==self.minimum[-1]:
            self.minimum.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return -1
        else:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.minimum:
            return -1
        else:
            return self.minimum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()