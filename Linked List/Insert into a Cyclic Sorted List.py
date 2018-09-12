# https://leetcode.com/explore/interview/card/google/60/linked-list-5/1342/

class Solution:
    def insert(self, head, insertVal):
        dump = head
        if not head:
            head = Node(insertVal, None)
            head.next = head
            return head
        cur = head
        flag = False
        while not cur.val <= insertVal <= cur.next.val:
            cur = cur.next
            if cur == dump:
                flag = True
                break
        if not flag:
            node = Node(insertVal, cur.next)
            cur.next = node
            return dump

        while not cur.val > cur.next.val:
            cur = cur.next
            if cur == dump:
                break		
        node = Node(insertVal, cur.next)
        cur.next = node
        return dump
