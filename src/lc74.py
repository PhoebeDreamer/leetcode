# 太慢了。。。。，二分法，对二维数组来说不好
class Solution1(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not len(matrix) or not len(matrix[0]):
            return False
        
        self.path = set()
        return self.search(matrix, target, 0, len(matrix), 0, len(matrix[0]))
        
    def search(self, matrix, target, start_h, end_h, start_w, end_w):
        mid_h, mid_w = (start_h+end_h)//2, (start_w+end_w)//2            
        if (mid_h, mid_w) in self.path:
            print "type 1"
            return False
        
        if matrix[mid_h][mid_w]==target:
            return True
        
        self.path.add((mid_h, mid_w))
        if matrix[mid_h][mid_w]>target:                
            if mid_w:
                end_w = mid_w
            elif not mid_w and end_h:
                end_h = mid_h
                start_w = 0
                end_w = len(matrix[0])
            else:
                print "type 2"
                return False
        else:
            if mid_w<len(matrix[0])-1:
                start_w = mid_w
            elif mid_w==len(matrix[0])-1 and start_h<len(matrix):
                start_h = mid_h
                start_w = 0
                end_w = len(matrix[0])
            else:
                print "type 3"
                return False    
        
        return self.search(matrix, target, start_h, end_h, start_w, end_w)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not len(matrix) or not len(matrix[0]):
            return False
        
        r = 0
        c = len(matrix[0])
        
        path = set()
        while r<len(matrix):
            if target>matrix[r][c-1]:
                r+=1
            else:
                for i in range(c):
                    if target==matrix[r][i]:
                        return True
                return False     
            
        return False
                

        
        

                    
        

            