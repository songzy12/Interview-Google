class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = {}
        def get_dp(i, j):
            if (i, j) in dp:
                return dp[i, j]
            if i == len(word1):
                dp[i, j] = len(word2) - j
            elif j == len(word2):
                dp[i, j] = len(word1) - i
            else:
                if word1[i] == word2[j]: # NOTE: remeber to check this
                    dp[i, j] = get_dp(i + 1, j + 1)
                else:
                    dp[i, j] = 1 + min([get_dp(i, j+1), get_dp(i+1,j), get_dp(i+1,j+1)])
            return dp[i, j]
        return get_dp(0, 0)

word1 = 'horse'
word2 = 'ros'
print(Solution().minDistance(word1, word2))