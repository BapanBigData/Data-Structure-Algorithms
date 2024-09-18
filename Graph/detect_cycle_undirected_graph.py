from collections import deque

# adjacency list representations of the graphs

class Graph:
    
    def __init__(self, V) -> None:
        self.adj = [[] for _ in range(V)]
    
    def add_edge(self, u, v, undirected=True):
        self.adj[u].append(v)
    
        if undirected:
            self.adj[v].append(u)
    
    def display(self):
        for e in self.adj:
            print(e)

#################################################################################

# given an undirected graph detect cycle, if it's contains cycle

def detect_cycle(V: int, adj: list[list[int]]) -> bool:
    # let's initialize a visited array
    visited = [False]*V
    
    def bfs_traversal(vertex):
        # initializing a queue
        queue = deque()
        queue.append((vertex, -1))
        
        visited[vertex] = True
        
        while queue:
            node, parent = queue.popleft()
            
            for u in adj[node]:
                if not visited[u]:
                    queue.append((u, node))
                    visited[u] = True
                    
                elif (parent != u):
                    return True
                
        return False

    
    def dfs_traversal(node, parent):
        visited[node] = True
        
        for u in adj[node]:
            if not visited[u]:
                if dfs_traversal(u, node):
                    return True
                
            elif (parent != u):
                return True
                
        return False
    
    for vertex in range(V):
        if not visited[vertex]:
            if dfs_traversal(vertex, -1):
                return True
            
    return False




graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 1)

graph = Graph(3)
graph.add_edge(0, 1)
graph.add_edge(1, 2)

# print(graph.adj)

res = detect_cycle(3, graph.adj)
print(res)