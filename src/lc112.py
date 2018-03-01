# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        if not root.left and not root.right and root.val == sum_:
            return True
        
        sum_ -= root.val
        
        return self.hasPathSum(root.left, sum_) or self.hasPathSum(root.right, sum_)