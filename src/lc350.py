class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        
        a = collections.Counter(nums1)
        b = collections.Counter(nums2)
        c = a-(a-b)
        return list(c.elements())
                
                
                
                
                