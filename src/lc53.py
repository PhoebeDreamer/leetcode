class Solution1:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = float('-inf')
        min_sum = 0
        tmp_sum = 0
        for n in nums:
            tmp_sum += n 
            max_sum = max(max_sum, tmp_sum-min_sum)
            min_sum = min(min_sum, tmp_sum)
        
        return max_sum

class Solution2:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = float('-inf')
        min_sum = 0
        tmp_sum = 0
        for n in nums:
            if tmp_sum<0:
                tmp_sum=0
    
            tmp_sum += n 
            max_sum = max(max_sum, tmp_sum)
        
        return max_sum
            