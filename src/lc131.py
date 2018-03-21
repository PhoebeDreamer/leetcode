class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []
        
        def helper(cur, res):
            if cur == len(s):
                ans.append(res)
                    
            for i in range(cur,len(s)):
                if self.palindrome(s[cur:i+1]):
                    helper(i+1, res+[s[cur:i+1]])     
                
        helper(0, [])
        return ans
    
    
    def palindrome(self, s):
        if s==s[::-1]:
            return True
        return False