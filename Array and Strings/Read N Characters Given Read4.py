# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        cnt = n // 4
        n = n % 4
        total_cnt = 0
        for i in range(cnt): 
            cur = [""] * 4
            total_cnt += read4(cur)
            buf[i*4:i*4+4] = cur
        cur = [""] * 4
        read4(cur)
        total_cnt += n # NOTE: n rather than cnt
        buf[cnt*4:cnt*4+4] = cur[:n]
        print(total_cnt, buf)
        return total_cnt