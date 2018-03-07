# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    "漂亮的pathSum+pathSumFrom抽象"
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.pathSumFrom(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def pathSumFrom(self, root, sum):
        if not root:
            return 0
        else:
            res = self.pathSumFrom(root.left, sum - root.val) + self.pathSumFrom(root.right, sum - root.val)
            if root.val == sum:
                res += 1
            return res
