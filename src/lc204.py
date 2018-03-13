class Solution(object):
    def countPrimes(self, n):
        if not n:
            return 0
        
        dic = n*[True]
        dic[0], dic[1] = False, False
        
        for i in range(2,int(n**0.5)+1):
            dic[i*i:n:i] = [False]*len(dic[i*i:n:i])
            
        return sum(dic)
            
        
        