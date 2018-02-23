# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        if fast:
            slow = slow.next
            
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        while prev:
            if prev != head:
                return False
            else:
                prev = prev.next
                head = head.next
        
        return True

def main():
    Solution().isPalindrome()
    head = ListNode(0)
    head.next = ListNode(0)

if __name__ == '__main__':
    main()