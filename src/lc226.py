# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        if root:
            root.left, root.right = root.right, root.left
          
        return root
            
        
        
        
        
        
        
        
        