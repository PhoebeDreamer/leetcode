class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board:
            self.r, self.c = len(board), len(board[0])

            for i in range(self.r):
                if board[i][0] == 'O':
                    self.visit(board, i, 0)
                if board[i][self.c-1] == 'O':
                    self.visit(board, i, self.c-1)

            for i in range(self.c):
                if board[0][i] == 'O':
                    self.visit(board, 0, i)
                if board[self.r-1][i] == 'O':
                    self.visit(board, self.r-1, i)
            
            print board
            for i in range(self.r):
                for j in range(self.c):
                    if board[i][j] == '*':
                        board[i][j] = 'O'
                    elif board[i][j] == 'O':
                        board[i][j] = 'X'
    
    
    def visit(self, board, i, j):
        if i<0 or j<0 or i>=self.r or j>=self.c:
            return
        
        if board[i][j]=='O':
            board[i][j] = '*'
        if i < self.r-2 and board[i+1][j]=='O':
            self.visit(board, i+1, j)
        if i > 1 and board[i-1][j]=='O':
            self.visit(board, i-1, j)
        if j < self.c-2 and board[i][j+1]=='O':
            self.visit(board, i, j+1)
        if j > 1 and board[i][j-1]=='O':
            self.visit(board, i, j-1)