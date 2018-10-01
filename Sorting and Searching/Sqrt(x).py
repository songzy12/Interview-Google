class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        def check(t, x):
            if t * t <= x and (t+1) * (t+1) > x:
                return True
            return False
        
        def binary(left, right, x):
            mid  = (left + right) // 2
            if check(mid, x):
                return mid
            if mid * mid <= x:
                return binary(mid + 1, right, x)
            return binary(left, mid - 1, x)
        return binary(0, x, x)

print(Solution().mySqrt(0))