from typing import List

class Solution:

    def isSafe(self, board, i, j, n, num) -> bool:
        ## checking in row wise and column wise
        for k in range(n):
            if board[k][j] == num or board[i][k] == num:
                return False
        
        ## check in sub-grids
        sx = (i // 3) * 3
        sy = (j // 3) * 3

        for x in range(sx, sx+3):
            for y in range(sy, sy+3):
                if board[x][y] == num:
                    return False
        
        return True

    def isSolvable(self, board, i, j, n) -> bool:
        ## base case
        if i == n:
            return True
        
        if j == n:
            return self.isSolvable(board, i+1, 0, n)
        
        ## skip the pre-fill cell
        if board[i][i] != ".":
            return self.isSolvable(board, i, j+1, n)
        
        ## cell to be filled
        ## try with all possible numbers
        for num in range(1, n+1):
            if self.isSafe(board, i, j, n, str(num)):
                board[i][j] = str(num)

                isSubProblemSolvable = self.isSolvable(board, i, j+1, n)
                if isSubProblemSolvable:
                    return True
        
        ## now backtrack
        board[i][j] = "."

        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = len(board)
        return self.isSolvable(board, 0, 0, n)
    


sol = Solution() 

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

# board1 = [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

res = sol.isValidSudoku(board)
print(res)