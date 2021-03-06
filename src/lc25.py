# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = prev = ListNode(None)
        dummy.next = cur = head
        while cur:
            g_head, enough, cur = self.return_group(cur,k)
            if not enough:
                return dummy.next
            prev.next = self.reverse(g_head)
            prev = g_head
            g_head.next = cur
        
        return dummy.next
    
    def return_group(self,ghead,k):
        cur = ghead
        while k-1 and cur:
            cur = cur.next
            k-=1
        if not cur:
            return ghead, False, cur
        
        tmp = cur.next
        cur.next = None
        cur = tmp
        # cur.next = cur.nextC, None
        return ghead, True, cur 
        
    
    def reverse(self,g_head):
        cur = g_head
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp        
            # cur.next, prev, cur = prev, cur, cur.next
        return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        count = 0
        while cur:
            cur = cur.next
            count+=1
        
        times = count//k
        count = times
        dummy = tail = ListNode(None)
        prev, dummy.next = None, head 
        while count:
            old_head = head
            tmp = k
            while tmp:
                cur = head
                head = head.next
                cur.next = prev
                prev = cur
                tmp-=1

            # if count == times:
            #     dummy.next = prev
            # 连接已经反转的当前段的头和上一段的尾巴
            tail.next = prev
            tail = old_head
            # 连接已经反转的上一段的头和下一段的头
            old_head.next = head
            prev = old_head
            count-=1
        
        return dummy.next
            

def test1():
    lst = to_llist([1,2,3,4,5])
    k = 3
    ret = Solution().reverseKGroup(lst, k)
    print_lst(ret)

def print_lst(lst):
    arr = []
    while lst:
        arr.append(lst.val)
        lst = lst.next
    print(arr)
        

def to_llist(lst):
    cur = dummy = ListNode(None)
    for i in lst:
        cur.next = ListNode(i)
        cur = cur.next
    return dummy.next

if __name__ == '__main__':
    test1()            
        
        