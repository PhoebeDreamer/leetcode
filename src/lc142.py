# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Floyd’s cycle detection algorith
        # Tortoise and Hare Algorithm
        
        fast = slow = start = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast is slow:
                while start is not slow:
                    start = start.next
                    slow = slow.next
                return start
        
        return None
            
            