# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        ans, length, cur = [], 0, root
        while cur:
            cur = cur.next
            length += 1  
        
        base_len, ext_len = length//k, length%k
        dummy, cur = ListNode(None), root
        while k:
            move = base_len+1 if ext_len>0 else base_len
            ext_len-=1
            # dummy指向子段的开头
            dummy.next = cur
            # 解决length<k的问题,空集问题
            # cur如果走完move，就无法切断了，所以走move-1步
            while move-1>0:
                move-=1
                cur = cur.next
            # 当前next指向空
            if cur:
                tmp = cur.next
                cur.next = None
                cur = tmp
            ans.append(dummy.next)
            k-=1
        
        return ans