from collections import deque

# **733. Flood Fill**


def flood_fill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    ans = image[:]
    n, m = len(image), len(image[0])
    
    visited = [[False]*m for _ in range(n)]
    initial_color = image[sr][sc]
    
    # directions for the traversal
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    
    def valid(i, j):
        return (0 <= i < n) and (0 <= j < m) and (image[i][j] == initial_color)
    
    
    def dfs_traversal(row, col):
        ans[row][col] = color
        visited[row][col] = True
        
        for d in directions:
            nrow = row + d[0]
            ncol = col + d[1]
            
            if valid(nrow, ncol) and not visited[nrow][ncol]:
                dfs_traversal(nrow, ncol)
        
        return
    
    
    def bfs_traversal(row, col):
        # initializing a queue
        queue = deque()
        queue.append((row, col))
        
        visited[row][col] = True
        
        while queue:
            u, v = queue.popleft()
            ans[u][v] = color
            
            for d in directions:
                nrow = u + d[0]
                ncol = v + d[1]
                
                if valid(nrow, ncol) and not visited[nrow][ncol]:
                    queue.append((nrow, ncol))
                    visited[nrow][ncol] = True
        
        return
    
    bfs_traversal(sr, sc)
    
    return ans




image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1 
color = 2

res = flood_fill(image=image, sr=sr, sc=sc, color=color)
print(res)
