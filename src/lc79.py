class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not word:
            return False
        self.r, self.c = len(board), len(board[0])
        self.char = [[0 for i in range(self.c)] for j in range(self.r)]
        # !!!!!!!
        
        for i in range(self.r):
            for j in range(self.c):
                if board[i][j]==word[0] and self.visit(board, i, j, word, 0):
                    return True
        
        return False
                
    def visit(self, board, sr, sc, s, cur):
        if cur == len(s):
            return True
        
        if sr<0 or sc<0 or sr>=self.r or sc>=self.c or board[sr][sc]!=s[cur] or self.char[sr][sc]:
            return False
        # print(self.char) 
        self.char[sr][sc]=1
        # print(board[sr][sc], s[cur])
        if (self.visit(board, sr+1, sc, s, cur+1)
            or self.visit(board, sr-1, sc, s, cur+1) 
            or self.visit(board, sr, sc+1, s, cur+1)
            or self.visit(board, sr, sc-1, s, cur+1)):
            return True
    
        self.char[sr][sc]=0
        return False
