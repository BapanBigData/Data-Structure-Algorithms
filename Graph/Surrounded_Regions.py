
# 130. Surrounded Regions
# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
# A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.


def surrounded_region_solver(board: list[list[str]]) -> None:
    n, m = len(board), len(board[0])
    
    # let's initializing a visited matrix
    visited = [[False]*m for _ in range(n)]
    
    # let's define the directions of the traversal
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    
    def valid(i, j):
        return (0 <= i < n) and (0 <= j < m) and (board[i][j] == 'O')
    
    def boundary_traversal(row, col):
        visited[row][col] = True
        
        for d in directions:
            drow = row + d[0]
            dcol = col + d[1]
            
            if valid(drow, dcol) and not visited[drow][dcol]:
                boundary_traversal(drow, dcol)
        
        return
    
    # traversing through the boundaries
    # 0th row and (n-1)th row
    for j in range(m):
        if not visited[0][j] and (board[0][j] == 'O'):
            boundary_traversal(0, j)
        
        if not visited[n-1][j] and (board[n-1][j] == 'O'):
            boundary_traversal(n-1, j)
    
    # 0th col and (m-1)th col
    for i in range(n):
        if not visited[i][0] and (board[i][0] == 'O'):
            boundary_traversal(i, 0)
        
        if not visited[i][m-1] and (board[i][m-1] == 'O'):
            boundary_traversal(i, m-1)
    
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and (board[i][j] == 'O'):
                board[i][j] = 'X'
    
    return


board = [
    
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
]

surrounded_region_solver(board)
print(board)
