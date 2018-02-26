class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0
        
        visited = [False for i in range(len(M))]
        count = 0
        for i in range(len(M)):
            if not visited[i]:
                self.dfs(M, visited, i)
                count+=1
                
        return count
        
    def dfs(self, M, visited, person):        
        for other in range(len(M)):
            if M[person][other] and not visited[other]:
                visited[other] = True
                self.dfs(M, visited, other)