class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        m = {}
        stack = []
        for num in nums:
            while stack and stack[-1] < num:
                m[stack[-1]] = num
                stack.pop()
            stack.append(num)
        res =  []
        for num in findNums:
            res.append(m.get(num, -1))
        return res
