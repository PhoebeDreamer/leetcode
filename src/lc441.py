class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        end = int(math.sqrt(2*n))
        
        if sum(range(end+1)) > n:
            return end-1
        else:
            return end
                