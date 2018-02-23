# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        cur, count = root, 0
        while cur:
            cur = cur.next
            count += 1
        base_len = count // k
        ext_num = count % k
        ret = []
        cur = root
        dummy = ListNode(None)
        for i in range(k):
            act_len = base_len + 1 if ext_num > 0 else base_len
            ext_num -= 1
            dummy.next = cur
            while act_len - 1 > 0 and cur:
                cur = cur.next
                act_len -= 1
            if cur:
                temp = cur.next
                cur.next = None
                cur = temp
            ret.append(dummy.next)
        return ret
