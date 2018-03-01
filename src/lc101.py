# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return self.isMirror(root.left, root.right)
        
    def isMirror(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        return p.val == q.val and self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)