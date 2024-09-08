from collections import deque

# **200. Number of Islands**
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.


def num_islands(grid: list[list[int]]) -> int:
    n, m = len(grid), len(grid[0])
    
    # initializing a visited matrix
    visited = [[False]*m for _ in range(n)]
    
    # let's define all the directions that can be traverse from the current node
    # # all 8 directions: 
    # for gfg (test cases)
    # directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    
    # 4 directions: left, Up, Right, Down
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)] 
    
    def valid(i, j):
        return (0 <= i < n) and (0 <= j < m) and (grid[i][j] == '1')
    
    def bfs_traversal(row, col):
        visited[row][col] = True
        
        # initialize a queue
        queue = deque()
        queue.append((row, col))
        
        while queue:
            u, v = queue.popleft()
            
            # traversing all neighbour of (u, v) 
            for d in directions:
                nrow = u + d[0]
                ncol = v + d[1]
                
                if valid(nrow, ncol) and not visited[nrow][ncol]:
                    queue.append((nrow, ncol))
                    visited[nrow][ncol] = True
        return
    
    def dfs_traversal(row, col):
        visited[row][col] = True
        
        for d in directions:
            nrow = row + d[0]
            ncol = col + d[1]
            
            if valid(nrow, ncol) and not visited[nrow][ncol]:
                dfs_traversal(nrow, ncol)
        
        return
    
    
    cnt_islands = 0
    for row in range(n):
        for col in range(m):
            if (grid[row][col] == '1') and not visited[row][col]:
                dfs_traversal(row, col)
                cnt_islands += 1
    
    return cnt_islands


grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

res = num_islands(grid)
print(res)
