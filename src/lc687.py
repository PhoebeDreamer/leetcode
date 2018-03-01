# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxval = 0
        self.helper(root)
        return self.max
        
    def helper(self, root):
        if not root:
            return 0
        
        length_l = self.helper(root.left)
        length_r = self.helper(root.right)
        left = length_l + 1 if root.left and root.left.val==root.val else 0
        right = length_r + 1 if root.right and root.right.val==root.val else 0
        
        self.max = max(self.max, left+right)
        return max(left, right)
        