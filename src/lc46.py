class Solution1:
    def permute(self, nums):
        self.ans = []
        if nums:
            nums.sort()
            self.count(nums, [])
        
        return self.ans
               
    def count(self, nums, partial):
        if len(partial) == len(nums):
            self.ans.append(list(partial))
            return
        
        for n in nums:
            if n not in partial:
                partial.append(n)
                self.count(nums, partial)
                partial.pop()
***************************************************
class Solution2:
    def permute(self, nums):
        if not nums:
            return [] 
        return list(itertools.permutations(sorted(nums), len(nums)))