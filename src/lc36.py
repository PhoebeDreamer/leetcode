class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        visit = []
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!='.':
                    n = board[i][j]
                    visit += [(i,n), (n,j), (i//3,j//3, n)]
        
        return len(visit) == len(set(visit))
                    