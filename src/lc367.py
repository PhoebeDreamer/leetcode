class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start = 0
        end = num
        
        while start+1<end:
            mid = (start+end)//2
            if mid*mid<num:
                start=mid
            elif mid*mid==num:
                end=mid
                return True
            else:
                end=mid
        
        if start*start == num or end*end == num:
            return True
        else:
            return False