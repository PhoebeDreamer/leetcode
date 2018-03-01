# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        partial = []
        ans = []
        self.helper(root, sum_, partial, ans)
        return ans
        
    def helper(self, root, sum_, partial, ans):        
        if root and not root.left and not root.right:
            partial = partial + [root.val]
            if sum(partial) == sum_:
                ans.append(partial)
        elif root:
            self.helper(root.left, sum_, partial+[root.val], ans)
            self.helper(root.right, sum_, partial+[root.val], ans)