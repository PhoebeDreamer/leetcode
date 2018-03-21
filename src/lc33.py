class Solution1(object):
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

class Solution2(object):
    def search(self, nums, target):
        if not nums:
            return -1
        
        start = 0
        end = len(nums)-1
        
        while start<end:
            mid = (start+end)//2
            if nums[mid]==target:
                return mid
            
            if nums[mid]>nums[end]:
                start = mid + 1
            elif nums[mid]<nums[end]:
                end = mid
        tmp =  start
        
        start = 0 if target>nums[-1] else tmp
        end = tmp if target>nums[-1] else len(nums)
        while start<end:
            mid = (start+end)//2
                
            if nums[mid]<target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid
            else:
                return mid
        
        return -1
