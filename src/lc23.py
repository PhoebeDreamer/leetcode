from heapq import heapify, heappop, heapreplace, heappush

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = new_head = ListNode(None)
        h = [(node.val, node) for node in lists if node]
        heapify(h)
        while h:
            val, node = h[0]
            if not node.next:
                heappop(h)
            else:
                heapreplace(h, (node.next.val, node.next))
            
            dummy.next = node
            dummy = dummy.next
        
        return new_head.next
            