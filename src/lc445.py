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
        list1 = []
        list2 = []
        list3 = []
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        
        while l2:
            list2.append(l2.val)
            l2 = l2.next
        
        flag = 0
        while list1 and list2:
            n = list1.pop() + list2.pop() + flag
            flag = n // 10
            n = n % 10
            list3.append(n)
        
        if not list1:
            list1 = list2

       while list1:
            n = list1.pop() + flag
            if n >= 10:
                n -= 10
                flag = 1
            else:
                flag = 0
            list3.append(n)

        if flag == 1:
            list3.append(flag)
        
        tmp = new_list = ListNode(None)
        for i in list3[::-1]:
            tmp.next = ListNode(i)
            tmp = tmp.next
        
        return new_list.next
            
             