class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        cnt = 0
        res = ''
        for c in S[::-1]:
            if c == '-':
                continue
            if cnt == K:                
                res += '-'
                cnt = 0
            cnt += 1
            res += c.upper()
        return res[::-1]

S = 'aa-1'
K = 2
print(Solution().licenseKeyFormatting(S, K))