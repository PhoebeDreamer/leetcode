class Solution:
    def combinationSum3(self, k, n):
        self.ans = []
        if k > int(math.sqrt(2*n)) or not k or n > 45:
            return self.ans
        
        nums = [i for i in range(1, 10)][::-1]
        self.helper(nums, k, n, [], 0)
        return self.ans
    
    def helper(self, nums, k, target, partial, cur):
        if target == 0 and len(partial) == k:
            self.ans.append(list(partial))
            return
        elif target > 0 and len(partial) < k:
            for i in range(cur, len(nums)):
                if nums[i] <= target:
                    partial.append(nums[i])
                    self.helper(nums, k, target-nums[i], partial, i+1)
                    partial.pop()