class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)
        
        while start<end:
            mid = (start+end)//2
            
            # nums[mid] and target on the same side
            if (nums[mid]<nums[0]) == (target<nums[0]):
                num = nums[mid]
            else:
                num = float("-inf") if target<nums[0] else float("inf")
                
            if num<target:
                start = mid + 1
            elif num > target:
                end = mid
            else:
                return mid
        
        return -1
