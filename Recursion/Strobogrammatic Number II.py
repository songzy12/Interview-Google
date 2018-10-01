# https://leetcode.com/explore/interview/card/google/62/recursion-4/399/

class Solution(object):
    def _findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return ['']
        if n == 1:
            return ['0', '1', '8']
        
        res = []
        a = ['0', '1', '8']
        b = ['6', '9']
        c = ['9', '6']
    
        for t in self._findStrobogrammatic(n - 2):        
            for i in range(3):
                res.append(a[i] + t + a[i])
            for i in range(2):
                res.append(b[i] + t + c[i])
        return res

    
    def findStrobogrammatic(self, n):
        temp = self._findStrobogrammatic(n)
        def check(s):
            if len(s) <= 1:
                return True
            return s[0] != '0'
        return [x for x in temp if check(x)]

print(Solution().findStrobogrammatic(3))        
        