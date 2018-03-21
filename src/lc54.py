class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        left, right = 0, len(matrix[0])-1
        up, down = 0, len(matrix)-1
        ans = []
        while up<=down and left<=right:
            for i in range(left, right+1):
                ans.append(matrix[up][i])
            up+=1
            
            for i in range(up, down+1):
                ans.append(matrix[i][right])
            right-=1
            
            if up<=down:
                for i in range(right, left-1, -1):
                    ans.append(matrix[down][i])
            down-=1
            
            if left<=right:
                for i in range(down, up-1, -1):
                    ans.append(matrix[i][left])
            left+=1
            
        return ans
    
        