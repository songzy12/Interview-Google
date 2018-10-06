# https://leetcode.com/explore/interview/card/google/66/others-4/458/


class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        def count1before0(num):
            cnt = 0
            t = 1 << 7
            while num & t:
                cnt += 1
                t >>= 1
            return cnt

        index = 0
        while index != len(data):
            cnt = count1before0(data[index]) # NOTE: index 
            print(cnt)
            if cnt > 4:
                return False
            if cnt == 0:
                index += 1
                continue
            if cnt == 1:  # NOTE: check this
                return False
            if len(data) - index < cnt:  # NOTE: check this
                return False
            for t in data[index + 1:index + cnt]:
                if count1before0(t) != 1:
                    return False
            index += cnt
        return True


data = [197, 130, 1]
print(Solution().validUtf8(data))
