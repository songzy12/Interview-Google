# https://leetcode.com/explore/interview/card/google/63/sorting-and-searching-4/439/
class Solution(object):

    def smallestDistancePair(self, nums, k):
        nums.sort()

        left = 0
        right = max(nums) - min(nums)

        import bisect

        def check(mid):
            # we find the number of distances that less or equal to mid
            res = 0
            for i in range(len(nums)):
                next_index = bisect.bisect_right(nums, nums[i] + mid)
                res += next_index - i - 1
            return res

        while left < right:
            # [left, right]
            mid = (left + right) // 2
            temp = check(mid)
            # we find the first distance that greater or equal to k
            print(left, right, mid, temp)
            if temp >= k:
                right = mid
            else:
                left = mid + 1
        return left

nums = [1, 3, 1]
k = 1
print(Solution().smallestDistancePair(nums, k))

# TLE: to use binary search


# class Solution(object):
# def smallestDistancePair(self, nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: int
#     """
#     nums.sort()
#     heap = []
#     from heapq import heappush, heappop
#     for i in range(len(nums) - 1):
#         heappush(heap, (abs(nums[i] - nums[i+1]), i, i + 1))
#     cnt = 0
#     while cnt < k - 1 and heap:
#         cnt += 1
#         _, i, j = heappop(heap)
#         if j + 1 < len(nums):
#             heappush(heap, (abs(nums[i] - nums[j + 1]), i, j + 1))
#     x, _, _ = heappop(heap)
#     return x

# https://leetcode.com/problems/k-th-smallest-prime-fraction/discuss/115819/Summary-of-solutions-for-problems-%22reducible%22-to-LeetCode-378
# https://leetcode.com/explore/interview/card/google/63/sorting-and-searching-4/439/discuss/109082/Approach-the-problem-using-the-%22trial-and-error%22-algorithm
