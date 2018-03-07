# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.subtree(root)
        return self.ans
        
        
    def subtree(self, root):
        if not root:
            return 0
        
        left = self.subtree(root.left)
        right = self.subtree(root.right)
        
        self.ans += abs(left-right)
        return left+right+root.val
        
        
        
    
    
    
    