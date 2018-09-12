class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = {}

        def get_dp(index):
            if index in dp:
                return dp[index]
            if index == len(s):
                return 1
            if s[index] == '0': # NOTE: add this
                return 0
            # NOTE: from index
            if len(s) - index > 1 and 1 <= int(s[index:index+2]) <= 26:
                dp[index] = get_dp(index + 1) + get_dp(index + 2)
                return dp[index]
            dp[index] = get_dp(index + 1)
            return dp[index]
        return get_dp(0)


s = "12"
print(Solution().numDecodings(s))
