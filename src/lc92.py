# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        count = 1
        dummy = tail = ListNode(None)
        tail.next = head
        while count<m:
            tail.next = head
            tail = tail.next
            head = head.next     
            count+=1

        prev = None
        old_head = head
        while count<=n:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
            count+=1
        tail.next = prev
        old_head.next = head
        
        return dummy.next
            