class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        single_len, comp_len = self.helper(root,0)
        return comp_len
        
        
    def helper(self, root, comp_len):
        if not root:
            return 0, 0
        
        left, comp_l = self.helper(root.left, comp_len)
        right, comp_r= self.helper(root.right, comp_len)
        
        return max(left,right)+1, max(comp_l, comp_r, left+right)