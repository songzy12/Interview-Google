# https://leetcode.com/explore/interview/card/google/67/sql-2/470/


class Solution:

    def kEmptySlots(self, flowers, k):
        # we think reversed order
        n = len(flowers)

        left = [i - 1 for i in range(n + 1)]
        right = [i + 1 for i in range(n + 1)]

        ans = -1
        for i in range(n - 1, -1, -1):
            index = flowers[i]
            # print(i, index, left[index], right[index])
            if left[index] != 0 and index - left[index] - 1 == k or \
                    right[index] != n + 1 and right[index] - index - 1 == k:
                ans = i + 1
            if left[index] != 0:
                right[left[index]] = right[index]
            if right[index] != n + 1:
                left[right[index]] = left[index]
        return ans

flowers = [3, 9, 2, 8, 1, 6, 10, 5, 4, 7]
k = 1
print(Solution().kEmptySlots(flowers, k))

# 复杂度高的方法：
# 维护一个 list，使用 binary search 每次找到插入下标，并检查左右

# 反过来的话
# 每次它要被消掉的时候看一下左边和右边是不是恰好有 k 个
# left 和 right 分别记录还没有凋谢的花
# 就是 index - left - 1 和 right - index - 1
# 然后更新 left 的 right （本来是当前位置，改成 right）和
# right 的 left （本来是当前位置，改成 left）

# left[index] != 0
# right[index] != n + 1