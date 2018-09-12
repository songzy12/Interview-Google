# https://leetcode.com/explore/interview/card/google/63/sorting-and-searching-4/345/

class Solution:
    def minWindow(self, s, t):
        from collections import defaultdict
        target = defaultdict(int)
        for c in t:
            target[c] += 1

        cur = defaultdict(int)
        def check():
            for k, v in target.items():
                if cur[k] < v:
                    return False
            return True

        tail = 0
        res = ""
        for head in range(len(s)):
            while not check() and tail < len(s):
                cur[s[tail]] += 1
                tail += 1
            if check() and (not res or tail - head < len(res)):
                # NOTE: when to update the answer
                res = s[head:tail]

            cur[s[head]] -= 1
            head += 1
        return res