# two pass
class Solution1(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # two-pass algorithm
        red = 0
        white = 0
        blue = 0
        for n in nums:
            if n==0:
                red+=1
            elif n==1:
                white+=1
            elif n==2:
                blue+=1
        
        i = 0
        while i<len(nums):
            if red:
                nums[i]=0
                red-=1
            elif white:
                nums[i]=1
                white-=1
            elif blue:
                nums[i]=2
                blue-=1
            i+=1

# two pointers
class Solution2(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # two-pass algorithm
        white_start = 0
        white_end = 0
        blue = len(nums)
        i, j = 0, len(nums)-1
        while white_end<blue:
            if nums[white_end]==0:
                nums[white_start], nums[white_end] = nums[white_end], nums[white_start]
                white_start+=1
                white_end+=1
            elif nums[white_end]==2:
                blue-=1
                nums[white_end], nums[blue]=nums[blue], nums[white_end]
            else:
                white_end+=1

# bucket sort
class Solution3(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # two-pass algorithm
        red = -1
        white = -1
        blue = -1
        
        for i in range(len(nums)):
            if nums[i]==0:
                blue+=1
                white+=1
                red+=1
                nums[blue] = 2
                nums[white] = 1
                nums[red] = 0
            elif nums[i]==1:
                blue+=1
                white+=1
                nums[blue] = 2
                nums[white] = 1
            else:
                blue+=1
                nums[blue] = 2

            
            
            
            