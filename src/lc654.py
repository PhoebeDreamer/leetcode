# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        return self.dfs(nums, 0, len(nums)-1)
    
    def dfs(self, nums, start, end):
        if start>end:
            return None
        
        idmax = start
        for i in range(start, end+1):
            if nums[i]>nums[idmax]:
                idmax = i
        
        root = TreeNode(nums[idmax])
        root.left = self.dfs(nums, start, idmax-1)
        root.right = self.dfs(nums, idmax+1, end)
        
        return root