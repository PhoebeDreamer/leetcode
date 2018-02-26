# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = float('-inf')
        self.Pathsum(root)
        return self.maxSum
        
    
    def Pathsum(self, root):
        if not root:
            return 0
        
        left = max(self.Pathsum(root.left), 0) 
        right = max(self.Pathsum(root.right), 0)
        self.maxSum = max(self.maxSum, left+right+root.val)
        
        return max(left, right) + root.val
        