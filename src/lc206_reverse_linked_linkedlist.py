# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
# #         # Method 1
# #         prev = None
# #         # where we build the new reversed list
# #         while head:
# #             cur = head
# #             # a reference to a node where we are moving from a list to the other
# #             head = head.next
# #             # pop the node off the front of the list
# #             cur.next = prev
# #             prev = cur
# #             # make the cur the new head of the reversed list
# #         return prev
        
#         # Method 2
#         # Failed!!!!! because the _init_ doesn't work
#         # change the _init_(self,x,next)
#         # prev = None
#         # while head:
#         #     prev = ListNode(head.val,prev)
#         #     head = head.next
#         # return prev
        
#         # Method 3
#         return self.reverse(head,None)
#         # why self?????
        


# Definition for singly-linked list.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        prev = None
        while cur:
            next_node = cur.next
            cur.next = prev 
            prev = cur
            cur = next_node

        return prev

    def reverseList2(self, head):
        cur = head
        if not cur or not cur.next:
            return cur
        else:
            tail = cur.next
            new_head = self.reverseList2(tail)
            tail.next = cur
            cur.next = None
            return new_head

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    Solution().reverseList2(head)

if __name__ == '__main__':
    main()