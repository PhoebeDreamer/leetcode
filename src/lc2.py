# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_head = dummy = ListNode(None)
        sum = 0
        while l1 or l2:
            sum //= 10
            if l1:
                sum+=l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            dummy.next = ListNode(sum%10)
            dummy = dummy.next
            
        if sum//10:
            dummy.next = ListNode(1)
        
        return new_head.next

class Solution2(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag = 0
        tmp = l1
        
        while l1.next and l2.next:
            l1.val = l1.val+l2.val+flag      
            if l1.val >= 10:
                l1.val -= 10
                flag = 1
            else:
                flag = 0           
            l1, l2 = l1.next, l2.next 
        
        l1.val = l1.val+l2.val+flag      
        if l1.val >= 10:
            l1.val -= 10
            flag = 1
        else:
            flag = 0 
        
        if l1.next:
            while l1.next:
                l1.next.val += flag
                if l1.next.val >= 10:
                    l1.next.val -= 10
                    flag = 1
                else:
                    flag = 0
                l1 = l1.next
        elif l2.next:
            while l2.next:
                l2.next.val += flag
                if l2.next.val >= 10:
                    l2.next.val -= 10
                    flag = 1
                else:
                    flag = 0
                
                l1.next = l2.next
                l2 = l2.next
                l1 = l1.next
                
        if flag == 1:
            l1.next = ListNode(1)
        
        return tmp
            
class Solution3(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pass
    
    flag = 0
    ret_head = l1

    while l1 and l2:
        l1.val = l1.val+l2.val+flag      
        flag = l1.val//10
        l1.val %= 10     
        prev, l1, l2 = l1, l1.next, l2.next 
    
    if not l1:
        l1 = l2
        prev.next = l1

    while flag and l1.next:
        l1.val += flag 
        flag = l1.val//10
        l1.val %= 10 
        l1 = l1.next 
    
    if flag == 1:
        l1.next = ListNode(1)

    return ret_head