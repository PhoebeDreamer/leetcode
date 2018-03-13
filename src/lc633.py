class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        def isSqrt(num):
            if int(num**0.5)**2 == num:
                return True
            return False
        
        return any(isSqrt(c-n*n) for n in range(int(c**0.5)+1))