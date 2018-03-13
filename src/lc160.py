# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tmp1 = headA
        tmp2 = headB
        n1, n2 = 0, 0
        
        while tmp1:
            tmp1 = tmp1.next
            n1 += 1
        
        while tmp2:
            tmp2 = tmp2.next
            n2 += 1
       
        m = abs(n1-n2)
        if n1 < n2:
            headA, headB = headB, headA
        while m != 0:
            headA = headA.next
            m -= 1
        
        while headA:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        
        return None