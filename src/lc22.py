class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        self.ans = []
        self.helper(n, "", 0, 0)
        return self.ans
    
    def helper(self, n, partial, left, right):
        if len(partial) == 2*n:
            self.ans.append(partial)
            return
        
        if left<n:
            self.helper(n, partial+'(', left+1, right)
        if right<left:
            self.helper(n, partial+')', left, right+1)
        
        