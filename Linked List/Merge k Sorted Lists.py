# https://leetcode.com/explore/interview/card/google/60/linked-list-5/342/
class Solution:
    def mergeKLists(self, lists):
        from heapq import heappush, heappop
        heap = [] 
        for i in range(len(lists)):
            if not lists[i]:
                continue
            heappush(heap, (lists[i].val, lists[i]))
            lists[i] = lists[i].next
        head = ListNode(-1)
        cur = head
        while heap:
            element, node = heappop(heap)
            if node.next: # node rather than element
                heappush(heap, (node.next.val, node.next))
            cur.next = node
            cur = cur.next
        return head.next