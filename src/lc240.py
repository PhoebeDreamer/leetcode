class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not len(matrix) or not len(matrix[0]):
            return False
        
        i, j = 0, len(matrix[0])-1
        while i<len(matrix) and j>=0:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                i+=1
            else:
                j-=1
        
        return False
        

        
        

            