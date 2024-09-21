from collections import deque

# 1020. Number of Enclaves
# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.


def num_enclaves(grid: list[list[int]]) -> int:
    n, m = len(grid), len(grid[0])
    
    # let's initializing the visited matrix
    visited = [[False]*m for _ in range(n)]
    
    # let's define all the possible directions of the traversal
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    
    def valid(i, j):
        return (0 <= i < n) and (0 <= j < m) and (grid[i][j] == 1)
    
    def dfs(row, col):
        visited[row][col] = True
        grid[row][col] = 0
        
        for d in directions:
            drow = row + d[0]
            dcol = col + d[1]
            
            if valid(drow, dcol) and not visited[drow][dcol]:
                dfs(drow, dcol)
        
        return
    
    
    def bfs(row, col):
        
        # let's initializing a queue
        queue = deque()
        queue.append((row, col))
        
        visited[row][col] = True
        
        while queue:
            r, c = queue.popleft()
            grid[r][c] = 0
            
            for d in directions:
                drow = r + d[0]
                dcol = c + d[1]
                
                if valid(drow, dcol) and not visited[drow][dcol]:
                    queue.append((drow, dcol))
                    visited[drow][dcol] = True
        return
    
    # let's do the boundary traversal
    for j in range(m):
        if not visited[0][j] and (grid[0][j] == 1):
            bfs(0, j)
        
        if not visited[n-1][j] and (grid[n-1][j] == 1):
            bfs(n-1, j)
    
    for i in range(n):
        if not visited[i][0] and (grid[i][0] == 1):
            bfs(i, 0)
        
        if not visited[i][m-1] and (grid[i][m-1] == 1):
            bfs(i, m-1)
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and (grid[i][j] == 1):
                cnt += 1
    
    return cnt


grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]

grid1 = [
    
    [0,0,0,1,1,1,0,1,0,0],
    [1,1,0,0,0,1,0,1,1,1],
    [0,0,0,1,1,1,0,1,0,0],
    [0,1,1,0,0,0,1,0,1,0],
    [0,1,1,1,1,1,0,0,1,0],
    [0,0,1,0,1,1,1,1,0,1],
    [0,1,1,0,0,0,1,1,1,1],
    [0,0,1,0,0,1,0,1,0,1],
    [1,0,1,0,1,1,0,0,0,0],
    [0,0,0,0,1,1,0,0,0,1]
]

res = num_enclaves(grid=grid1)
print(res)
