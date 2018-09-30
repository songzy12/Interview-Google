# https://leetcode.com/explore/interview/card/google/59/array-and-strings/465/


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def compute_lps(pat):
            l = 0
            lps = [0 for i in range(len(pat))]
            i = 1
            while i < len(pat):
                if pat[i] == pat[l]:
                    l += 1
                    lps[i] = l
                    i += 1
                else:
                    if l != 0:
                        l = lps[l - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps        
        temp = s + '#' + s[::-1]
        lps = compute_lps(temp)
        if len(s) - lps[-1] > 0:
            return s[-len(s)+lps[-1]:][::-1] + s
        return s


# lps[i] = the longest proper prefix of pat[0..i]
# which is also a suffix of pat[0..i].
