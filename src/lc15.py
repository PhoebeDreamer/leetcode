class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            start, end = i+1, len(nums)-1
            target = -nums[i]
            while start < end: 
                if nums[start]+nums[end] < target:
                    start+=1
                elif nums[start]+nums[end] > target:
                    end-=1
                else:
                    ans.append([nums[i], nums[start], nums[end]])
                    start+=1
                    end-=1
                    while start<end and nums[start] == nums[start-1]: 
                        start+=1
                    while start<end and nums[end] == nums[end+1]:
                        end-=1
                
        return ans
        