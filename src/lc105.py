# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return 
        
        root = TreeNode(preorder[0])
        pivot = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:pivot+1],inorder[:pivot])
        root.right = self.buildTree(preorder[pivot+1:], inorder[pivot+1:])

        return root