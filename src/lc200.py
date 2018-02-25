class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        self.h, self.w = len(grid), len(grid[0])
        count = 0
        
        for i in range(self.h):
            for j in range(self.w):
                if grid[i][j] == "1":
                    self.helper(grid, i, j)
                    count+=1
        
        return count
    
    def helper(self, grid, i, j):
        if i<0 or i>=self.h or j<0 or j>=self.w or grid[i][j]=="0":
            return
        grid[i][j] = "0"
        self.helper(grid, i+1, j)
        self.helper(grid, i-1, j)
        self.helper(grid, i, j+1)
        self.helper(grid, i, j-1)