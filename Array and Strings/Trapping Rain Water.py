class Solution:

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0

        left = []
        max_left = 0
        for i in range(len(height)):
            cur = height[i]
            left.append(max_left)
            if cur > max_left:
                max_left = cur

        right = []
        max_right = 0
        for i in range(len(height) - 1, -1, -1):
            cur = height[i]
            right = [max_right] + right
            if cur > max_right:
                max_right = cur

        for i in range(len(height)):
            temp = max(0, min(left[i], right[i]) - height[i])
            ans += temp
        return ans

# 左边最高的 和 右边最高的 中的 最低的那个

# right = [max_right] + right，嗨呀好蠢
