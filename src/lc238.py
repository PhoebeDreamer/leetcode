class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod = [1]
        for i in range(1,len(nums)):
            prod.append(prod[-1]*nums[i-1])
        
        prev = 1
        i = len(nums)-1
        while i>=0:
            prod[i] *= prev
            prev*=nums[i]
            i-=1
        
        return prod