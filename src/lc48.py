'''
 clockwise rotate
 first reverse up to down, then swap the symmetry 
 1 2 3     7 8 9     7 4 1
 4 5 6  => 4 5 6  => 8 5 2
 7 8 9     1 2 3     9 6 3
'''

# 1   2  3  4       13 14 15 16     13 9  5  1
# 5   6  7  8       9  10 11 12     14 10 6  2
# 9  10 11 12  ==>  5  6  7  8  ==> 15 11 7  3
# 13 14 15 16       1  2  3  4      16 12 8  4

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # first reverse up to down, then swap the symmetry 
        n = len(matrix)
        for i in range(n//2):
            tmp = matrix[i]
            matrix[i] = matrix[n-1-i]
            matrix[n-1-i] = tmp
        
        for i in range(n):
            for j in range(i):
                # 转一半
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        
            
        