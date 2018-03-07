# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True    
        
        return self.dfs(root.left, float("-inf"), root.val) and self.dfs(root.right, root.val, float("inf"))
    
    def dfs(self, root, floor, ceiling):
        if not root:
            return True
        
        if root.val >= ceiling or root.val <= floor:
            return False
        
        return self.dfs(root.left, floor, min(ceiling, root.val)) and self.dfs(root.right, max(floor, root.val), ceiling)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        pre = None
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            if pre and root.val <= pre.val:
                return False
            pre = root
            root = root.right
            
        return True
            
        
        
        
        
        