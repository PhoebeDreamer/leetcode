class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        
        stack = []
        area = 0
        for i in range(len(heights)+1):
            cur = -1 if i==len(heights) else heights[i] # the last one is -1, less than any num in the list
                
            while stack and cur<=heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i-1-stack[-1]
                #here, nodes can be not continuous, like 2,1,3,6,4,7,5,stack[1,3,4,5]
                # we know stack[0] is the smallest num in the list, so we have to count from i->0
                area = max(area, h*w)
            
            stack.append(i)
        
        return area