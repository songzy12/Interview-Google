class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2: # NOTE: index out of range
            return []
        heap = []
        from heapq import heappush, heappop
        for i in range(len(nums1)):            
            heappush(heap, (nums1[i] + nums2[0], i, 0))
        res = []
        cnt = 0
        while cnt < k and heap: # NOTE: index out of range
            cnt += 1
            _, i, j = heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res
