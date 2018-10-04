class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:  # NOTE: this
            return nums[0]
        # two conditions: 2...n, no condition or 1...n-1, no condition
        dp = [0 for i in range(len(nums)+2)]
        for i in range(len(nums)-2, -1, -1):
            dp[i] = max(dp[i+1], nums[i]+dp[i+2])
        res = dp[0]

        dp = [0 for i in range(len(nums)+2)]
        for i in range(len(nums)-1, 0, -1):
            dp[i] = max(dp[i+1], nums[i]+dp[i+2])
        res = max(res, dp[1])  # NOTE: this is dp[1] rather than dp[0]
        return res
