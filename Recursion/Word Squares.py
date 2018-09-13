# https://leetcode.com/explore/interview/card/google/62/recursion-4/370/
class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        result = []

        from collections import defaultdict
        m = defaultdict(list)
        for word in words:
            for i in range(1, len(word)+1):
                m[word[:i]].append(word)

        def generate(current):
            if len(current) == len(words[0]):
                result.append(current)
                return
            prefix = ''.join(x[len(current)] for x in current)
            for word in m[prefix]:
                generate(current + [word])

        for word in words:
            generate([word])
        return result
