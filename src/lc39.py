class Solution:
    def combinationSum(self, candidates, target):
        self.ans = []
        if not candidates:
            return []
        
        candidates = sorted(candidates)[::-1]
        self.helper(candidates, target, [], 0)
        return self.ans
    
    def helper(self, candidates, target, partial, cur):
        if target == 0:
            self.ans.append(list(partial))
            return
        
        if target > 0:
            for i in range(cur, len(candidates)):
                if candidates[i] <= target:
                    partial.append(candidates[i])
                    self.helper(candidates, target-candidates[i], partial, i)
                    partial.pop()