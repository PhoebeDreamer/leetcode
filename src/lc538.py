# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        
        self.sum = 0
        self.dfs(root)
        return root
           
    def dfs(self, root):
        if not root:
            return 0
        
        self.dfs(root.right)
        root.val+=self.sum
        self.sum=root.val
        self.dfs(root.left)


        
        
            
            
            
            
            
            
            
            
            
            
            
            
            