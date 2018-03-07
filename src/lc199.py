import collections as c

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def rightSideView(self, root):
        if not root:
            return []
        q = c.deque()
        q.append((1,root))
        ans, tmp = [], []
        
        while q:
            level, node = q.popleft()
            
            if node.left:
                q.append((level+1,node.left))
            if node.right:
                q.append((level+1,node.right))
            
            if len(ans)<level:
                ans.insert(0,[])
            
            ans[-level].append(node.val)
 
        for n in ans[::-1]:
            tmp.append(n[-1])
        return tmp

class Solution2:
    def rightSideView(self, root):
        if not root:
            return []
        
        self.result = []
        self.dfs(root, 0)
        return self.result
        
    def dfs(self, root, depth):
        if not root:
            return
        
        if depth==len(self.result):
            self.result.append(root.val)
            
        self.dfs(root.right, depth+1)
        self.dfs(root.left, depth+1)

class Solution3:
    def rightSideView(self, root):
        if not root:
            return []
        
        q = c.deque()
        q.append(root)
        result = []
        
        while q:
            l = len(q)
            for i in range(l):
                cur = q.popleft()
                if i==0:
                    result.append(cur.val)
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)
        
        return result