class Solution1:
    def findUnsortedSubarray(self, nums):
        if not nums:
            return 0
        
        tmp = sorted(nums)
        length = len(nums)        
        left = 0
        right = length-1
        
        while left<length and nums[left] == tmp[left]:
            left+=1
        
        while right > left and nums[right] == tmp[right]:
            right-=1
        
        return right-left + 1

class Solution2(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        beg = -1
        end = -2
        maxN = nums[0] 
        minN = nums[n-1]
        
        for i in range(n):
            maxN = max(maxN, nums[i])
            minN = min(minN, nums[n-i-1])
            if nums[i] < maxN:
                end = i
            if nums[n-1-i] > minN:
                beg = n-1-i
                
        return end-beg+1
                
            