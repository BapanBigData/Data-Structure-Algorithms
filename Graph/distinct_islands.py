from collections import deque

# Given a boolean 2D matrix grid of size n * m. 
# You have to find the number of distinct islands where a group of connected 1s (horizontally or vertically) forms an island. 
# Two islands are considered to be distinct if and only if one island is not equal to another (not rotated or reflected).


def cnt_distinct_islands(grid: list[list[int]]) -> int:
    n, m = len(grid), len(grid[0])
    
    # let's initialize a visited grid
    visited = [[False]*m for _ in range(n)]
    
    # let's define all possible direction of the traversal
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    
    def valid(i, j):
        return (0 <= i < n) and (0 <= j < m) and (grid[i][j] == 1)
    
    def dfs(row, col, row0, col0, coords):
        visited[row][col] = True
        coords.append((row-row0, col-col0))
        
        for d in directions:
            drow = row + d[0]
            dcol = col + d[1]
            
            if valid(drow, dcol) and not visited[drow][dcol]:
                dfs(drow, dcol, row0, col0, coords)
        
        return
    
    
    def bfs(row, col, row0, col0, coords):
        # let's initializing a queue
        queue = deque()
        queue.append((row, col))
        
        visited[row][col] = True
        
        while queue:
            r, c = queue.popleft()
            coords.append((r-row0, c-col0))
            
            for d in directions:
                drow = r + d[0]
                dcol = c + d[1]
                
                if valid(drow, dcol) and not visited[drow][dcol]:
                    queue.append((drow, dcol))
                    visited[drow][dcol] = True
        return
    
    res_set = set()
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and (grid[i][j] == 1):
                vec = []
                bfs(i, j, i, j, vec)
                res_set.add(tuple(vec))
                
    return len(res_set)


grid = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 0, 1, 0]
]

cnt = cnt_distinct_islands(grid=grid)
print(cnt)
