class Solution:

    def __init__(self):
        self.cnt = {}
        self.size = 0

    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not k:
            return 0

        def check(c):
            return self.size + (1 if c not in self.cnt else 0) <= k

        def add(c):
            if c not in self.cnt:
                self.cnt[c] = 1
                self.size += 1
            else:
                self.cnt[c] += 1

        def remove(c):
            self.cnt[c] -= 1
            if self.cnt[c] == 0:
                self.cnt.pop(c)
                self.size -= 1

        tail = 0
        ans = 0
        for head in range(len(s)):
            while tail < len(s) and check(s[tail]):
                add(s[tail])
                tail += 1
            cur = tail - head
            if cur > ans:
                ans = cur
            remove(s[head])
        return ans

# 注意这两句的顺序
# add(s[tail])
# tail += 1

# 注意边界条件：
# if not k: return 0