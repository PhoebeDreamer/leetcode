import collections as c

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        q = c.deque()
        q.append(root)
        count, next_count = 1, 0
        tmp, ans = [], []
        while q:
            node = q.popleft()
            tmp.append(node.val)
            count-=1
                
            if node.left:
                q.append(node.left)
                next_count+=1
            if node.right:
                q.append(node.right)
                next_count+=1

            if count == 0:
                ans.append(tmp)
                count = next_count
                next_count = 0
                tmp = []
        
        return ans[::-1]
            
            