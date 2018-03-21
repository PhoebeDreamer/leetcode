# Description:
# Given an array of integers, find two non-overlapping subarrays which have the largest sum.
# The number in each subarray should be contiguous.
# Return the largest sum.

# Given an array of integers, find two non-overlapping subarrays which have the largest sum.
# The number in each subarray should be contiguous.
# Return the largest sum.

class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here
        left = []
        right = []
        tmp_sum, max_sum, min_sum = 0, float("-inf"), 0
        for i, n in enumerate(nums):
            tmp_sum += n
            max_sum = max(max_sum, tmp_sum-min_sum)
            min_sum = min(min_sum, tmp_sum)
            left.append(max_sum)
        
        tmp_sum, max_sum, min_sum = 0, float("-inf"), 0
        for i, n in enumerate(nums[::-1]):
            tmp_sum += n
            max_sum = max(max_sum, tmp_sum-min_sum)
            min_sum = min(min_sum, tmp_sum)
            right.append(max_sum)
        
        right = right[::-1]
        
        max_sum = float("-inf")
        for i in range(len(nums)-1):
            max_sum = max(max_sum, left[i]+right[i+1])
        
        return max_sum
            