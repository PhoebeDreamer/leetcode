class Solution1:
    def rotate(self, nums, k):
        k %= len(nums)
        
        if k:
            end = k
            n = len(nums)
            while end:
                nums.append(nums[n-end])
                end-=1
                
            end = n-k
            while end:
                nums[end+k-1] = nums[end-1]
                end-=1
                
            while k:
                k-=1
                nums[k] = nums.pop()
                

class Solution2:
    def rotate(self, nums, k):
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]    

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        
        if k:
            nums[:] = nums[:-k][::-1] + nums[-k:][::-1] 
            nums[:] = nums[::-1]
                
          