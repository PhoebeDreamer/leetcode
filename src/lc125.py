class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([i.lower() for i in s if i.isalnum()])
        return s == s[::-1]