class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x and not x%10 or x<0:
            return False
        
        r = 0
        tmp = x
        while tmp:
            r = r*10 + tmp%10
            tmp//=10
        
        return r==x
        