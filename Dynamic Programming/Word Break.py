class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = {}
        wordDict = set(wordDict)
        def get_dp(index):
            if index in dp:
                return dp[index]
            if index == len(s):
                return True
            for i in range(index + 1, len(s) + 1):
                if s[index:i] in wordDict:
                    if get_dp(i):
                        return True
            dp[index] = False
            return False            
        return get_dp(0)