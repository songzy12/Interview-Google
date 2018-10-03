class Solution(object):

    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m_cross = {(1, 3): 2, (1, 9): 5, (1, 7): 4, (2, 8): 5,
                   (3, 7): 5, (3, 9): 6, (4, 6): 5, (7, 9): 8}

        deck = set(range(1, 10))
        self.res = 0

        def check(head, num):
            if (head, num) in m_cross:
                if m_cross[head, num] in deck:
                    return False
            if (num, head) in m_cross:
                if m_cross[num, head] in deck:
                    return False
            return True

        def dfs(m, n, head, step):
            if m <= step <= n:
                self.res += 1
            deck.remove(head)
            for num in deck:
                if check(head, num):
                    dfs(m, n, num, step + 1)
            deck.add(head)

        dfs(m, n, 1, 1)
        temp = 4 * self.res
        self.res = 0
        dfs(m, n, 2, 1)
        temp += 4 * self.res
        self.res = 0
        dfs(m, n, 5, 1)
        temp += self.res

        return temp


m = 4
n = 5
print(Solution().numberOfPatterns(m, n))

# TLE: we need to record some mid results?
# No, use the symmetric property