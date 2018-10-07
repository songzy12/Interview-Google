# https://leetcode.com/explore/interview/card/google/63/sorting-and-searching-4/440/
from bisect import bisect_left, bisect_right


class RangeModule(object):

    def __init__(self):
        self.X = []
        self.in_ = []

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        il = bisect_left(self.X, left)
        ir = bisect_right(self.X, right)
        # if i % 2 == 0, means last is False
        # if i % 2 == 1, means last is True
        self.X[il:ir] = [left] * (il % 2 == 0) + [right] * (ir % 2 == 0)
        self.in_[il:ir] = [True] * (il % 2 == 0) + [False] * (ir % 2 == 0)

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        il = bisect_right(self.X, left)
        ir = bisect_left(self.X, right)
        # print(self.X)
        # print(self.in_)
        # print(il, ir)
        return il == ir and il > 0 and self.in_[il - 1] == True

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        il = bisect_left(self.X, left)
        ir = bisect_right(self.X, right)
        self.X[il:ir] = [left] * (il % 2 == 1) + [right] * (ir % 2 == 1)
        self.in_[il:ir] = [False] * (il % 2 == 1) + [True] * (ir % 2 == 1)

# ["RangeModule","addRange","removeRange","queryRange","queryRange","queryRange"]
# [[],[10,20],[14,16],[10,14],[13,15],[16,17]]

# Your RangeModule object will be instantiated and called as such:
obj = RangeModule()
obj.addRange(10, 20)
obj.removeRange(14, 16)
print(obj.queryRange(10, 14))
print(obj.queryRange(13, 15))
print(obj.queryRange(16, 17))

# thought: interval tree
# or, you can use some simple way
# 哎呀不要总是想着屠龙之术

# Segment tree stores intervals, and optimized for "which of these intervals contains a given point" queries.
# Interval tree stores intervals as well, but optimized for "which of these intervals overlap with a given interval" queries. It can also be used for point queries - similar to segment tree.
# Range tree stores points, and optimized for "which points fall within a given interval" queries.
# Binary indexed tree stores items-count per index, and optimized for "how
# many items are there between index m and n" queries.


# https://www.geeksforgeeks.org/interval-tree/
# https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/
# https://www.geeksforgeeks.org/segment-tree-set-1-range-minimum-query/
