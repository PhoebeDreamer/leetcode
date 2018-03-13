# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = deque()
        q.append((1, root))
        flag_l = False
        flag_r = False
        
        while(q):
            level, node = q.popleft()
            
            if node.left:
                q.append((level+1, node.left))
            else:
                flag_l = True
            if node.right:
                q.append((level+1, node.right))
            else:
                flag_r = True


            if flag_l and flag_r: 
                return level
            else:
                flag_l = False
                flag_r = False
        
        return level+1
