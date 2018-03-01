# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections as c

class Solution1(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        node = root
        # stack = []
        ans = c.Counter()
        def dfs(node):
            if node:
                ans[node.val]+=1
                dfs(node.left)
                dfs(node.right)
      
        dfs(root)
        maxval = max(ans.itervalues())
        return [i for i in ans if ans[i] == maxval]



class Solution2(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        node = root
        stack = []
        ans = c.Counter()
        while stack or node:
            count = 0
            while node:
                stack.append(node)
                ans[node.val] += 1
                node = node.left
 
            node = stack.pop()
            node = node.right
        
        maxval = max(ans.itervalues())
        return [i for i in ans if ans[i] == maxval]