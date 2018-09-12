# https://leetcode.com/explore/interview/card/google/61/trees-and-graphs/344/
class Solution:
    def inorderSuccessor(self, root, p):
        # left most son of right subtree 
        # or father of which it is the left son
        if p.right:
            cur = p.right
            while cur.left:
                cur = cur.left
            return cur
        # NOTE: the first father to turn right

        m = {}
        def find(node):
            if not node:
                m[node] = False
                return m[node]
            if node == p:
                m[node] = True
                return m[node]
            if find(node.left) or find(node.right):
                m[node] = True
                return m[node]
            m[node] = False
            return False

        find(root)
        
        res = None
        cur = root
        while cur != p:
            if m[cur.left]:
                res = cur
                cur = cur.left
            else:
                cur = cur.right
        return res