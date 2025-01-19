from collections import deque

# 994. Rotting Oranges
# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# BFS (Breadth-First Search)


def oranges_rotting(grid: list[list[int]]) -> int:
    n, m = len(grid), len(grid[0])
    
    visited = [[False]*m for _ in range(n)]
    
    def valid(i, j):
        return (0 <= i < n) and (0 <= j < m) and (grid[i][j] == 1)
    
    # let's initialize a queue
    queue = deque()
    fresh_cnt = 0
    
    for i in range(n):
        for j in range(m):
            if (grid[i][j] == 2):
                queue.append((i, j, 0))
                visited[i][j] = True
            
            if (grid[i][j] == 1):
                fresh_cnt += 1
    
    minutes = 0
    cnt = 0
    
    # define directions for the traversal
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    
    while queue:
        row, col, t = queue.popleft()
        minutes = max(minutes, t)
        
        for d in directions:
            nrow = row + d[0]
            ncol = col + d[1]
            
            if valid(nrow, ncol) and not visited[nrow][ncol]:
                queue.append((nrow, ncol, t+1))
                visited[nrow][ncol] = True
                cnt += 1
    
    if (fresh_cnt != cnt):
        return -1
    
    return minutes            


grid = [[2,1,1],[1,1,0],[0,1,1]]
grid1 = [[2,1,1],[0,1,1],[1,0,1]]
res = oranges_rotting(grid=grid1)
print(res)

