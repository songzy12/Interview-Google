# https://leetcode.com/explore/interview/card/google/61/trees-and-graphs/463/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.distance = None
        self.ans = None

    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return
        # NOTE: remember: if self.distance == None
        if self.distance == None or abs(root.val - target) < self.distance:
            self.distance = abs(root.val - target)
            self.ans = root.val
        if root.val > target:
            self.closestValue(root.left, target)
        else:
            self.closestValue(root.right, target)
        return self.ans
