from collections import deque


# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.


def update_matrix(mat: list[list[int]]) -> list[list[int]]:
    n, m = len(mat), len(mat[0])
    
    # initializing the res and visited matrix
    res = mat[:]
    visited = [[False]*m for _ in range(n)]
    
    def valid(i, j):
        return (0 <= i < n) and (0 <= j < m) and (mat[i][j] == 1)
    
    
    # initializing a queue
    queue = deque()
    
    for i in range(n):
        for j in range(m):
            if (mat[i][j] == 0):
                queue.append((i, j, 0))
                visited[i][j] = True
    
    # let's define all the possible direction of the traversal
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    
    while queue:
        row, col, dist = queue.popleft()
        res[row][col] = dist
        
        for d in directions:
            nrow = row + d[0]
            ncol = col + d[1]
            
            if valid(nrow, ncol) and not visited[nrow][ncol]:
                queue.append((nrow, ncol, dist+1))
                visited[nrow][ncol] = True
                
    return res



###############################################################################################

# GFG
# Given a binary grid of n*m. Find the distance of the nearest 1 in the grid for each cell.
# The distance is calculated as |i1  - i2| + |j1 - j2|, where i1, j1 are the row number and column number of the current cell, 
# and i2, j2 are the row number and column number of the nearest cell having value 1. There should be atleast one 1 in the grid.

def nearest(grid: list[list[int]]) -> list[list[int]]:
    n, m = len(grid), len(grid[0])
    
    # initializing the res and visited matrix
    res = grid[:]
    visited = [[False]*m for _ in range(n)]
    
    def valid(i, j):
        return (0 <= i < n) and (0 <= j < m) and (grid[i][j] == 0)
    
    
    # initializing a queue
    queue = deque()
    
    for i in range(n):
        for j in range(m):
            if (grid[i][j] == 1):
                queue.append((i, j, 0))
                visited[i][j] = True
    
    # let's define all the possible direction of the traversal
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    
    while queue:
        row, col, dist = queue.popleft()
        res[row][col] = dist
        
        for d in directions:
            nrow = row + d[0]
            ncol = col + d[1]
            
            if valid(nrow, ncol) and not visited[nrow][ncol]:
                queue.append((nrow, ncol, dist+1))
                visited[nrow][ncol] = True
                
    return res


grid = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 1]
]

print(nearest(grid))
