class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.ans = 0
        visited ={i:0 for i in range(1, N+1)}
        nums = [i for i in range(1, N+1)][::-1]
        self.helper(visited, N, N, nums)
        return self.ans
    
    def helper(self, visited, cur, target, nums):
        if cur == 0:
            self.ans += 1
            return
        
        for i in nums:
            if not visited[i] and (not i%cur or not cur%i):
                visited[i] = 1
                self.helper(visited, cur-1, target, nums)
                visited[i] = 0
    
    # def swap(self, nums, i, )
                