# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.ans = []
        self.helper(root)
        return self.ans
        
    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        self.ans.append(root.val)
        self.helper(root.right)

******************************************************
class Solution2:
    def inorderTraversal(self, root):
        if not root:
            return []
        
        stack = []
        node = root
        ans = []
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            ans.append(node.val)
            node = node.right
        
        return ans
