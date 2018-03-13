class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)<3:
            return None
        
        nums.sort()
        ans = sum(nums[0:3]) - target
        
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left<right:
                prev = nums[left]+nums[right]+nums[i]-target
                if abs(prev)<abs(ans):
                    ans = prev
                    
                if nums[left]+nums[right]+nums[i]<target:
                    left+=1
                elif nums[left]+nums[right]+nums[i]>target:
                    right-=1
                else:
                    return target
                
        return ans+target
            
                

            
        