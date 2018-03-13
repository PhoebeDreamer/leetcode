# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        
        return prev

class Solution2:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse(head, None)
    
    def reverse(self, head, prev):
        if not head:
            return prev
        
        next_node = head.next
        head.next = prev
        return self.reverse(next_node, head)