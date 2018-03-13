class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        low = 0
        high = len(letters)-1
        mid = (low+high)//2
        
        while low < high:
            if letters[mid] > target:
                high = mid
            else:
                low = mid
            
            mid = (low+high)//2
            
            if high-low <= 1:
                if letters[low] > target:
                    return letters[low]
                elif letters[high] <= target and high == len(letters)-1:
                    return letters[0]
                else:
                    return letters[high]
                
            