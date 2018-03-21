class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        count = len(nums1)+len(nums2)
        if not count:
            return count/2
        
        if count%2:
            return self.findKthnumber(nums1, 0, nums2, 0, count//2+1)/1.0
        else:
            return (self.findKthnumber(nums1, 0, nums2, 0, count//2) + self.findKthnumber(nums1, 0, nums2, 0, count//2+1))/2.0
    
    def findKthnumber(self, A, Astart, B, Bstart, k):
        if Astart>=len(A):
            return B[Bstart+k-1]
        if Bstart>=len(B):
            return A[Astart+k-1]
        
        if k==1:
            return min(A[Astart], B[Bstart])
        
        midA = float('inf') if Astart+k//2-1>=len(A) else A[Astart+k//2-1]
        midB = float('inf') if Bstart+k//2-1>=len(B) else B[Bstart+k//2-1]
        
        if midA>midB:
            return self.findKthnumber(A, Astart, B, Bstart+k//2, k-k//2)
        else:
            return self.findKthnumber(A, Astart+k//2, B, Bstart, k-k//2)

        