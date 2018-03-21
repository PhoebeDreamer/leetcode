class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        
        # find the last ascending index
        for i, n in enumerate(nums):
            if i > 0 and n > prev:
                index = i
            prev = n
        
        if index!=0:    
            # swap(nums[index-1], the smallest nums bigger than nums[index-1]
            i = index
            last = index
            while i<len(nums):
                if nums[index-1]<nums[i]:
                    last = i
                i+=1
            nums[last], nums[index-1] = nums[index-1], nums[last]
            
        # sort nums[index:] in ascending order
        i = index
        j = len(nums)-1
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1
        
                