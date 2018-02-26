class Solution(object):
    def sumNumbers(self, root):
        if not root:
            return 0
        
        self.ans = 0
        self.helper(root, 0)
        return self.ans
    
    def helper(self, root, partial):
        if not root:
            return
        
        if not root.left and not root.right:
            self.ans += partial*10 + root.val
            return
            
        if root.left:
            self.helper(root.left, partial*10+root.val)
        if root.right:
            self.helper(root.right, partial*10+root.val)