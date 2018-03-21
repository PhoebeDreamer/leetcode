class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if sum(L)<k:
            return 0
            
        max_len = max(L)
        start = 1
        end = max_len
        ans = set()
        while start+1<end:
            mid = (start+end)//2
            tmp_sum = sum(l//mid for l in L)
            if tmp_sum<k:
                end = mid
            else:
                start=mid
        
        tmp_sum = sum(l//end for l in L)        
        if tmp_sum>=k:
            return end
        else:
            return start