# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections as c
class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = c.deque()
        q.append(root)
        ans = 0
        
        while q:
            node = q.popleft()
            
            if node.left:
                if not node.left.left and not node.left.right:
                    ans += node.left.val
                else:
                    q.append(node.left)
            
            if node.right:
                q.append(node.right)
        
        return ans
                    
                    
                    
                    