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
        if not head:
            return None
        dummy = prev = ListNode(None)
        prev.next = head
        flag = None
        while head:
            if head.next and head.val == head.next.val:
                flag = head.val
                while head and head.val == flag:
                    head = head.next
                if not head:
                    prev.next = head
            else:
                prev.next = head
                prev = head
                head = head.next
        
        return dummy.next
            
            