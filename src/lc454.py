class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        n = len(A)
        res = 0
        AB = {}
        for i in range(n):
            for j in range(n):
                if A[i]+B[j] not in AB:
                    AB[A[i]+B[j]]=0
                AB[A[i]+B[j]]+=1
        
        for i in range(n):
            for j in range(n):
                if -(C[i]+D[j]) in AB:
                    res+=AB[-(C[i]+D[j])]
        
        return res
                    