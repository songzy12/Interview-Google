# https://leetcode.com/explore/interview/card/google/59/array-and-strings/461/
class Solution:
    def moveZeroes(self, nums):
        head = 0
        cur = 0
        while cur < len(nums):
            if nums[cur] != 0:
                nums[head] = nums[cur]
                head += 1
            cur += 1
        while head < len(nums):
            nums[head] = 0
            head += 1 # NOTE: remember to move cursor
