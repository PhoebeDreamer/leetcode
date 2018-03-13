# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        sdummy = s_node = ListNode(None)
        ldummy = l_node = ListNode(None)
        while head:
            if head.val >= x:
                l_node.next = head
                l_node = l_node.next
            else:
                s_node.next = head
                s_node = s_node.next
            head = head.next
        l_node.next = None
        s_node.next = ldummy.next
        return sdummy.next