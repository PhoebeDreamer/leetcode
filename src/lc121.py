class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        
        profits = []
        for i in range(1, len(prices)):
            profits.append(prices[i]-prices[i-1])
        
        tmp_sum = 0
        max_profits = float('-inf')
        for n in profits:
            if tmp_sum<0:
                tmp_sum=0
            tmp_sum+=n
            max_profits = max(max_profits, tmp_sum)
        
        return max(max_profits, 0)