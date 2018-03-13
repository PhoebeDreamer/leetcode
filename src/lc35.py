class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        
        while start+1<end:
            mid = (start+end)//2
            if nums[mid] == target:
                end = mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid
        
        if nums[start] >= target:
            return start
        elif nums[end] < target:
            return end+1
        else:
            return end
        