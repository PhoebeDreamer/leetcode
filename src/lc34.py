class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums)
        low = -1
        high = -1
        
        while start<end:
            mid = (start+end)//2 
            if nums[mid]==target:
                low = mid-1
                high = mid+1
                while low>=0 and nums[low]==target:
                    low-=1
                while high<=len(nums)-1 and nums[high]==target:
                    high+=1
                
                return [low+1, high-1]
            elif nums[mid]<target:
                start = mid+1
            else:
                end = mid
        
        return [low, high]
                
                                