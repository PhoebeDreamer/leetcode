class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not image:
            return image
        
        self.r, self.c = len(image), len(image[0])
        
        if sr not in range(self.r) or sc not in range(self.c):
            return image
        
        color = image[sr][sc]
        
        if color != newColor:
            self.helper(image, color, sr, sc, newColor)
        return image
    
    def helper(self, image, color, i, j, newColor):
        if i<0 or j<0 or i>=self.r or j>=self.c or image[i][j]!=color:
            return None
        
        image[i][j] = newColor
        self.helper(image, color, i+1, j, newColor)
        self.helper(image, color, i-1, j, newColor)
        self.helper(image, color, i, j+1, newColor)
        self.helper(image, color, i, j-1, newColor)
            
        
        
        
        
        
        