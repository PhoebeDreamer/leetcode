class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ans = max_prod = min_prod = nums[0]

        for i, n in enumerate(nums):  
            if i==0:
                continue
                
            # swap min_prod, max_prod
            if n<0:
                min_prod, max_prod = max_prod, min_prod
            
            max_prod = max(n, n*max_prod)
            min_prod = min(n, n*min_prod)
            
            ans = max(ans, max_prod)
            
        return ans
            
        