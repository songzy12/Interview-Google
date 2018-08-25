class Solution:

    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """

        time = time[:2] + time[3:]
        digits = list(set([x for x in time]))

        def get_times(digits, cur, index):
            if index == 4:
                return cur
            ans = []
            for digit in digits:
                ans += get_times(digits, [x + digit for x in cur], index + 1)
            return ans

        def valid(time):
            h, m = map(int, [time[:2], time[2:]])
            return h < 24 and m < 60

        def get_delta(time1, time2):
            h1, m1 = map(int, [time1[:2], time1[2:]])
            h2, m2 = map(int, [time2[:2], time2[2:]])
            temp = h2 * 60 + m2 - h1 * 60 - m1
            if temp <= 0:
                temp += 24 * 60
            return temp

        ans = None
        delta = 24 * 60
        for next_time in filter(valid, get_times(digits, [""], 0)):
            temp = get_delta(time, next_time)
            if temp <= delta:
                ans = next_time
                delta = temp
        return ":".join([ans[:2], ans[2:]])

time = "00:00"
print(Solution().nextClosestTime(time))

# temp <= 0 for next same time
#  return ":".join([ans[:2], ans[2:]]) remember to convert to suitable format