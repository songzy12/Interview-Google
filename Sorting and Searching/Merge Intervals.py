# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # NOTE: to define the compare metric
        intervals.sort(key=lambda x: (x.start, x.end))
        res = []
        head = 0
        while head < len(intervals):
            cur_right = intervals[head].end
            tail = head + 1
            while tail < len(intervals) and intervals[tail].start <= cur_right:
                cur_right = max(cur_right, intervals[tail].end)
                tail += 1
            intervals[head].end = cur_right
            res.append(intervals[head])
            head = tail
        return res
