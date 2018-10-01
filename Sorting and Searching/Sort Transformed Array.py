class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        if a == 0: # NOTE: this
            if b > 0:
                return [b * x + c for x in nums] # NOTE: this
            else:
                return [b * x + c for x in nums[::-1]]

        t = - b / (2.0 * a)
        
        tail = 0
        while tail < len(nums) and nums[tail] <= t:
            tail += 1
        head = len(nums) - 1
        while head >= 0 and nums[head] > t:
            head -= 1

        # print(t, head, tail)

        res = []
        while head >= 0 and tail < len(nums):
            if abs(nums[head] - t) < abs(nums[tail] - t):
                res.append(a * nums[head] ** 2 + b * nums[head] + c)
                head -= 1
            else:                
                res.append(a * nums[tail] ** 2 + b * nums[tail] + c)
                tail += 1
        while head >= 0:
            res.append(a * nums[head] ** 2 + b * nums[head] + c)
            head -= 1
        while tail < len(nums):
            res.append(a * nums[tail] ** 2 + b * nums[tail] + c)
            tail += 1
        return res if a > 0 else res[::-1] # NOTE: this