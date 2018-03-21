class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here 
        nums = [-n for n in nums]
        
        min_sum = 0
        max_sum = float('-inf')
        tmp_sum = 0
        for n in nums:
            tmp_sum+=n
            max_sum = max(max_sum, tmp_sum-min_sum)
            min_sum = min(min_sum, tmp_sum)
        
        return -max_sum