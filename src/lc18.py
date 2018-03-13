class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def findNsum(nums, target, N, partial, result):
            # early termination
            if N<2 or len(nums)<N or target < nums[0]*N or target > nums[-1]*N:
                return
            
            if N==2:
                start, end = 0, len(nums)-1
                while start<end:
                    if nums[start] + nums[end] < target:
                        start+=1
                    elif nums[start] + nums[end] > target:
                        end-=1
                    else:
                        result.append(partial+[nums[start], nums[end]])
                        start+=1
                        end-=1
                        while start<end and nums[start]==nums[start-1]: start+=1
                        while start<end and nums[end]==nums[end+1]: end-=1
            else:
                for i in range(len(nums)-N+1):
                    # skip duplicates
                    if i==0 or (i>0 and nums[i]!=nums[i-1]):
                        findNsum(nums[i+1:], target-nums[i], N-1, partial+[nums[i]], result)
                        # similar to combination sum
        
        nums.sort()
        result = []
        findNsum(nums, target, 4, [], result)
        return result
        