class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        ans = [[1] for i in range(numRows)]
        if numRows <2:
            return ans
        
        ans[1].append(1)  
        
        for i in range(2,numRows):
            # print(ans[i])
            # print(ans[i-1])
            j = 0
            while j+1 < i:
                ans[i].append(ans[i-1][j]+ans[i-1][j+1])
                j+=1          
            ans[i].append(1)
        
        return ans