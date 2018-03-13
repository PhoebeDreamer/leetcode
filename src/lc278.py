# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        high = n
        low = 1
        mid = (high+low)//2
        while low+1 < high:
            if isBadVersion(mid):
                high = mid
            else:
                low = mid

            mid = (high+low)//2
            
        if isBadVersion(low):
            return low
        else:
            return high
        