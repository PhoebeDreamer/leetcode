# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections as c
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        q = c.deque()
        q.append((root,1))
        ans = c.defaultdict(list)
        ans[1] = [root.val]
        
        while q:
            node, level = q.popleft()
            if node.left:
                q.append((node.left, level+1))
                ans[level+1].append(node.left.val)    
                
            if node.right:
                q.append((node.right, level+1))
                ans[level+1].append(node.right.val)

        zigzag = []
        for i in range(1, level+1):
            if i%2:
                zigzag.append(ans[i])
            else:
                zigzag.append(ans[i][::-1])
        
        return zigzag
            
            
            
            
            
            
            
            
            