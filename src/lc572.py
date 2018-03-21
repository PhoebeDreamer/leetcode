# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if self.isequal(s,t):
            return True
        
        if not s:
            return False
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)        
        
        
    def isequal(self, s, t):
        if not (s or t):
            return s is t
        
        if s and t:
            return s.val==t.val and self.isequal(s.left, t.left) and self.isequal(s.right, t.right)