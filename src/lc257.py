# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.stack = []
        self.helper(root, "")
        return self.stack
    
    def helper(self, root, string):
        if not root:
            return 

        if not root.left and not root.right:
            self.stack.append(string+str(root.val))
            return 

        if root.left:
            self.helper(root.left, string+str(root.val)+"->")

        if root.right:
            self.helper(root.right, string+str(root.val)+"->")