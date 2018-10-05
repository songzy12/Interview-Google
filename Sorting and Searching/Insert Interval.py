# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        head = 0
        while head < len(intervals) and intervals[head].end < newInterval.start:
            head += 1
        if head == len(intervals):
            intervals.append(newInterval)
            return intervals
        # else we need some merge

        newInterval.start = min(newInterval.start, intervals[head].start)

        tail = head
        while tail < len(intervals) and intervals[tail].start <= newInterval.end:
            tail += 1
        if tail - 1 >= 0: # NOTE: remember to check  this
            newInterval.end = max(newInterval.end, intervals[tail - 1].end)
        return intervals[:head] + [newInterval] + intervals[tail:]
