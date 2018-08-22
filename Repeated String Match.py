class Solution:

    def repeatedStringMatch(self, A, B):
        min_cnt = len(B) // len(A)
        if min_cnt * len(A) < len(B):
            min_cnt += 1
        if B in A * min_cnt:
            return min_cnt
        if B in A * (min_cnt + 1):
            return min_cnt + 1
        return -1

# 使用 // 而不是 /
# len(B) // len(A) 而不是 len(A) // len(B)
