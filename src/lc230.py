# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        pre = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                k-=1
                if k == 0:
                    return root.val
                root = root.right
                
                
                
                
                
                
                