# https://leetcode.com/explore/interview/card/google/66/others-4/460/
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def _map(word):
            res = 0
            for c in word:
                res |= 1<<(ord(c) - ord('a'))
            return res
        bits = list(map(_map, words))
        res = 0
        for i in range(len(words)):
            for j in range(i, len(words)):
                if not (bits[i] & bits[j]):
                    res = max(res, len(words[i]) * len(words[j]))
        return res

# repeat chars do not matter
# order does not matter

# It turns out O(n^2) is enough to pass the test
# TODO: can we do better?