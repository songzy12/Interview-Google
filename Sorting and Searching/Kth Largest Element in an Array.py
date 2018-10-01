class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from heapq import heappop, heappush
        q = []
        for t in nums:            
            heappush(q, t)
            if len(q) > k:
                heappop(q)
        return heappop(q)