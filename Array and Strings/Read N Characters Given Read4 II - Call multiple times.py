# https://leetcode.com/explore/interview/card/google/59/array-and-strings/436/

class Solution:

    def __init__(self):
        self.last = []

    def read(self, buf, n):
        if len(self.last) >= n:
            buf[:]  = self.last[:n]
            self.last = self.last[n:]
            return n
        cur_cnt = 0
        if self.last:
            buf[:len(self.last)] = self.last
            cur_cnt += len(self.last)
            self.last = []
            n -= cur_cnt # NOTE: remember to minus this
        while n:
            cur = [''] * 4
            cnt = read4(cur)
            if not cnt:
                break

            if cnt > n:
                self.last = cur[n:] # NOTE: n rather than cnt-n
            buf[cur_cnt: cur_cnt + cnt] = cur

            cur_cnt += min(cnt, n)
            n -= min(cnt, n)

        return cur_cnt
