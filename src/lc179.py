# sort cmp
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = list(map(str, nums))
        comp = lambda a, b: 1 if a+b>b+a else -1 if b+a>a+b else 0
        nums.sort(cmp=comp, reverse=True)
        return ''.join(nums).lstrip('0') or '0'

# quicksort
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = list(map(str, nums))
        self.sort(nums, 0, len(nums)-1)
        # print nums
        return ''.join(nums[::-1]).lstrip('0') or '0'
    
    def sort(self, nums, start, end):
        if start>=end:
            return
        
        target = nums[start]
        pivot = start
        for i in range(start+1, end+1):
            if self.comp(target, nums[i]):
                pivot+=1
                nums[pivot], nums[i] = nums[i], nums[pivot]
        nums[pivot], nums[start] = nums[start], nums[pivot]
        
        self.sort(nums, start, pivot-1)
        self.sort(nums, pivot+1, end)
    
    def comp(self, n1, n2):
        if n1+n2>n2+n1:
            return True
        return False