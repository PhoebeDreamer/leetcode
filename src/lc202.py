class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic = set()
        while n not in dic:
            dic.add(n)
            n = sum(int(i)**2 for i in str(n))
        
        return n==1