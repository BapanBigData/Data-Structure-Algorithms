from collections import deque

# 547. Number of Provinces
# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, 
# and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.


def find_num_provinces(is_connected: list[list[int]]) -> int:
    vertices = len(is_connected)
    visited = [False] * vertices
    
    def dfs_traversal(u):
        visited[u] = True
        
        for v in range(vertices):
            if not visited[v] and (is_connected[u][v] == 1):
                dfs_traversal(v)
        
        return
    
    
    def bfs_traversal(vertex):
        visited[vertex] = True
        
        queue = deque()
        queue.append(vertex)
        
        while queue:
            u = queue.popleft()
            
            for v in range(vertices):
                if not visited[v] and (is_connected[u][v] == 1):
                    queue.append(v)
                    visited[v] = True
        return
    
    cnt_provinces = 0
    
    for vertex in range(vertices):
        if not visited[vertex]:
            bfs_traversal(vertex)
            cnt_provinces += 1
    
    return cnt_provinces


graph = [[1,1,0],[1,1,0],[0,0,1]]
isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
res = find_num_provinces(isConnected)
print(res)
