# https://leetcode.com/explore/interview/card/google/65/design-4/336/

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.sum = 0
        self.size = size
        self.cnt = 0
        self.window = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.cnt < self.size:
            self.sum += val
            self.cnt += 1
            self.window.append(val)
            return self.sum * 1. / self.cnt
        else:
            self.sum -= self.window.pop(0)
            self.sum += val
            self.window.append(val)
            return self.sum * 1. / self.cnt

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)