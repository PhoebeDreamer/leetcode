class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.ans = []
        if not candidates:
            return []
        
        candidates = sorted(candidates, reverse=True)
        self.helper(candidates, target, [], 0)
        return self.ans
    
    def helper(self, candidates, target, partial, cur):
        if target == 0:
            self.ans.append(list(partial))
            return
        
        if target < 0:
            return 

        for i in range(cur, len(candidates)):
            if candidates[i] <= target:
                partial.append(candidates[i])
                self.helper(candidates, target-candidates[i], partial, i)
                partial.pop()
