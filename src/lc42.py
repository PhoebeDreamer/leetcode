class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        length = len(height)
        if length == 1:
            return 0
        k = 0
        while k < length:
            j = 1
            rest = 0
            rest_n = 0
            if height[k]:
                while k+j < length and height[k+j] < height[k]:
                    if height[k+j] >= rest:
                        rest_n = j
                        rest = height[k+j]
                    j += 1 
                # find a higher one   
                # or find the highest one among the rest 
                
                if j > 1 and j+k < length:
                    area += min(height[k+j], height[k]) * (j-1)
                    tmp = j
                    while tmp-1:
                        area -= height[k+tmp-1]
                        tmp -= 1
                    k += j
                elif j>1 and j+k == length:
                    area += rest*(rest_n-1)
                    tmp = rest_n
                    while tmp-1:
                        area -= height[k+tmp-1]
                        tmp -= 1
                    k += rest_n
                else:
                    k+=1       
            else:
                k+=1
        
        return area
            
                    
                    
                
                    
                
            
            