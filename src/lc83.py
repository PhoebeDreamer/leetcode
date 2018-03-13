# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = prev = ListNode(None)
        prev.next = head
        while head:
            if head.val == prev.val:
                head = head.next
                prev.next = head
            else:
                prev = prev.next
                head = head.next
            
        return dummy.next