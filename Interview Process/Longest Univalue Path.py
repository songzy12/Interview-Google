# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    def __init__(self):
        self.ans = 1

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        dp = {}

        def longest_all(node):

            if not node:
                return 0
            
            temp = 1
            if node.left and node.left.val == node.val:
                temp += longest_single(node.left)
            if node.right and node.right.val == node.val:
                temp += longest_single(node.right)
            if temp > self.ans:
                self.ans = temp
            longest_all(node.left)
            longest_all(node.right)
            return temp


        def longest_single(node):
            if not node:
                return 0
            if node in dp:
                return dp[node]
            res = 1
            if node.left and node.left.val == node.val:
                res = 1 + longest_single(node.left)
            if node.right and node.right.val == node.val:
                res = max(res, 1 + longest_single(node.right))
            dp[node] = res
            return res

        longest_all(root)
        return self.ans - 1

# 不要手抖把 left 误写成 right
# 注意题目对于路径长度的定义是边的数目还是点的数目