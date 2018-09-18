# https://leetcode.com/explore/interview/card/google/65/design-4/479/
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.queue = [v1, v2]
        self.queue_id = -1
        self.index = 0
        self.max_len = max(len(v1), len(v2))

    def next(self):
        """
        :rtype: int
        """
        return self.queue[self.queue_id][self.index]

    def hasNext(self):
        """
        :rtype: bool
        """
        while True:
            self.queue_id += 1
            if self.queue_id == len(self.queue):
                self.queue_id = 0
                self.index += 1
            if self.index == self.max_len:
                return False
            if self.index < len(self.queue[self.queue_id]):
                break
        return True


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
