# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odummy = ohead = ListNode(None)
        edummy = ehead = ListNode(None)
        count = 0
        while head:
            count+=1
            if count%2:
                odummy.next = head
                odummy = odummy.next
            else:
                edummy.next = head
                edummy = edummy.next
            head = head.next
        
        edummy.next = None
        odummy.next = ehead.next
        return ohead.next