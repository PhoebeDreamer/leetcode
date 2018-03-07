# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
                
        self.flatten(root.left)
        self.flatten(root.right)
        
        if root.left:
            if root.right:
                dummy = root.left
                while dummy.right:
                    dummy = dummy.right
                dummy.right = root.right
            root.right = root.left
            root.left = None

        