# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        x, y = 0, 0
        while l1:
            x = x*10 + l1.val
            l1 = l1.next
        while l2:
            y = y*10 + l2.val
            l2 = l2.next
        x+=y
        new_head = dummy = ListNode(0)
        if not x:
            return dummy
        x = str(x)
        for i in range(len(x)):
            dummy.next = ListNode(x[i])
            dummy = dummy.next
        
        return new_head.next