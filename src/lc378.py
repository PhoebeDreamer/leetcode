class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return 0
        
        h = len(matrix)
        w = len(matrix[0])
        
        pq = []
        
        for i in range(h):
            for j in range(w):
                heapq.heappush(pq, matrix[i][j])
        
        for i in range(k-1):
            heapq.heappop(pq)
        
        return heapq.heappop(pq)