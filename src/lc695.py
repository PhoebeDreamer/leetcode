class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    area = max(area, self.getArea(grid, i, j))
        
        return area
    
    def getArea(self, grid, r, c):
        if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or not grid[r][c]:
            return 0
        
        grid[r][c]=0
        return 1+self.getArea(grid, r+1, c)+ \
                self.getArea(grid, r-1, c)+ \
                self.getArea(grid, r, c+1)+ \
                self.getArea(grid, r, c-1)