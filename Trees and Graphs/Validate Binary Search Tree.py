# https://leetcode.com/explore/interview/card/google/61/trees-and-graphs/437/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(root, left, right):
            if not root:
                return True
            # NOTE: != None is different from != 0
            if left != None and root.val <= left or \
                    right != None and root.val >= right:
                return False
            return valid(root.left, left, root.val) and \
                valid(root.right, root.val, right)
        return valid(root, None, None)
