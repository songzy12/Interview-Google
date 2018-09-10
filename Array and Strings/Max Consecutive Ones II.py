# https://leetcode.com/explore/interview/card/google/59/array-and-strings/455/
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        if nums.count(1) == 0 and len(nums):
            return 1 # if all is zero
        res = 0

        def compute_ones(nums, i):
            head = i
            while i < len(nums) and nums[i] == 1:
                i += 1
            return i - head, i
        def compute_zeros(nums, i):			
            head = i
            while i < len(nums) and nums[i] == 0:
                i += 1
            return i - head, i
        
        index = 0
        cnt0, index = compute_zeros(nums, index)        

        flag = False
        last_cnt1 = 0
        while index < len(nums):
            cnt1, index = compute_ones(nums, index)
            if flag:
                res = max(res, cnt1 + last_cnt1 + 1) #NOTE: here do not forget to +1
            else:
                if cnt0 or index < len(nums): # NOTE: convert 1 before or after
                    res = max(res, cnt1 + 1) # NOTE: and here do not forget to +1
                else:
                    res = max(res, cnt1)
            last_cnt1 = cnt1
            cnt0, index = compute_zeros(nums, index)
            flag = True if cnt0 == 1 else False
        return res	
    
        
