# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = prev = ListNode(None)
        dummy.next = cur = head
        while cur and cur.next:
            tmp = cur.next.next
            
            next_node = cur.next
            prev.next = next_node
            cur.next = next_node.next
            next_node.next = cur
            # swap sequence
            prev = cur
            cur = tmp
        
        return dummy.next