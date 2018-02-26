class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.helper(nums, k)
        
        
    def helper(self, nums, target):
        mid = len(nums)//2
        left, right, equal = [], [], []
        
        for n in nums:
            if n > nums[mid]:
                left.append(n)
            elif n < nums[mid]:
                right.append(n)
            else:
                equal.append(n)
        
        if len(left) + len(equal) < target:
             return self.helper(right, target-len(left)-len(equal))  
        elif len(left) >= target:
            return self.helper(left, target)
        elif len(left) == target - 1 or len(left)+len(equal) >= target:
            return nums[mid]