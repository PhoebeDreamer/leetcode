class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t = s[::-1]
        if s == t:
            return True
        i = 0
        while i<len(s) and t[i]==s[i]:
            i+=1   
        return s[:i]+s[i+1:] == (s[:i]+s[i+1:])[::-1] or t[:i]+t[i+1:] == (t[:i]+t[i+1:])[::-1]
        
        
            