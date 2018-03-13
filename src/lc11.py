class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        area = 0
        while left < right:
            area = max(area, (right-left)*min(height[right],height[left]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return area
            
                