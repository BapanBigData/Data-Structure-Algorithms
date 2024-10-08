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

##############################################################################################

# graph traversals
# Breadth first search (bfs) of an undirected graph

def bfs_utils(adj, visited, source):
    # initializing a queue
    queue = deque()
    
    queue.append(source)
    visited[source] = True
    
    while queue:
        curr = queue.popleft()
        print(curr, end=' ')
        
        for u in adj[curr]:
            if not visited[u]:
                queue.append(u)
                visited[u] = True
    return


def bfs_connected(adj, source):
    visited = [False]*len(adj)
    bfs_utils(adj, visited, source)


# bfs of disconnected graph (generalized)
def bfs(adj):
    vertices = len(adj)
    visited = [False]*vertices
    
    for u in range(vertices):
        if not visited[u]:
            bfs_utils(adj=adj, visited=visited, source=u)

##################################################################################################################

# number of connected components in a graph (undirected graph)

def number_of_connected_components_undirected_graph(graph: Graph) -> int:
    adj_lst = graph.adj
    
    vertices = len(adj_lst)
    visited = [False] * vertices
    
    def traverse(source):
        # initializing a queue
        queue = deque()
        
        queue.append(source)
        visited[source] = True
        
        while queue:
            curr = queue.popleft()
            
            for u in adj_lst[curr]:
                if not visited[u]:
                    queue.append(u)
                    visited[u] = True
    
    cnt = 0
    
    for u in range(vertices):
        if not visited[u]:
            traverse(u)
            cnt += 1
            
    return cnt

###########################################################################################################

# Depth first search (dfs)

def dfs_utils(adj, visited, source):
    visited[source] = True
    print(source, end=' ')
    
    for u in adj[source]:
        if not visited[u]:
            dfs_utils(adj, visited, u)
    return


def dfs_connected(graph: Graph, source: int):
    adj_lst = graph.adj
    vertices = len(adj_lst)
    visited = [False]*vertices
    
    dfs_utils(adj=adj_lst, visited=visited, source=source)


# dfs generalized

def dfs(graph: Graph):
    adj_lst = graph.adj
    vertices = len(adj_lst)
    visited = [False]*vertices
    
    for vertex in range(vertices):
        if not visited[vertex]:
            dfs_utils(adj=adj_lst, visited=visited, source=vertex)


# number of connected components in an undirected graph

def connected_components(graph: Graph):
    adj_lst = graph.adj
    vertices = len(adj_lst)
    visited = [False]*vertices
    
    def traverse(source):
        visited[source] = True
        
        for u in adj_lst[source]:
            if not visited[u]:
                traverse(u)
        return
    
    cnt = 0
    
    for vertex in range(vertices):
        if not visited[vertex]:
            traverse(vertex)
            cnt += 1
    
    return cnt



# driver code (undirected graph)
# graph = Graph(6)
# graph.add_edge(0, 1)
# graph.add_edge(0, 2)
# graph.add_edge(0, 5)
# graph.add_edge(1, 3)
# graph.add_edge(2, 4)
# graph.add_edge(3, 5)
# graph.add_edge(4, 5)

# # graph.display()


# # let's take a dis-connected graph
graph = Graph(7)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(4, 5)
graph.add_edge(4, 6)
graph.add_edge(5, 6)

# graph.display()

# print(number_of_connected_components(graph))

# traversal 
# bfs(adj)


# let's define a directed graph

# graph = Graph(8)
# graph.add_edge(0, 1, undirected=False)
# graph.add_edge(2, 1, undirected=False)
# graph.add_edge(3, 4, undirected=False)
# graph.add_edge(3, 0, undirected=False)
# graph.add_edge(4, 3, undirected=False)
# graph.add_edge(5, 7, undirected=False)
# graph.add_edge(6, 5, undirected=False)
# graph.add_edge(6, 7, undirected=False)

# graph.display()
# print(number_of_connected_components_undirected_graph(graph))

# let's initialize a connected and undirected graph
# graph = Graph(7)
# graph.add_edge(0, 1)
# graph.add_edge(0, 4)
# graph.add_edge(1, 2)
# graph.add_edge(2, 3)
# graph.add_edge(4, 5)
# graph.add_edge(4, 6)


# # let initialize a connected directed graph
# graph = Graph(4)
# graph.add_edge(0, 1, undirected=False)
# graph.add_edge(0, 2, undirected=False)
# graph.add_edge(1, 2, undirected=False)
# graph.add_edge(2, 1, undirected=False)
# graph.add_edge(2, 3, undirected=False)
# graph.add_edge(3, 1, undirected=False)

# print(connected_components(graph))


graph = Graph(6)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(3, 5)
graph.add_edge(4, 5)

print(graph.adj)

dfs(graph)

print()

bfs(graph.adj)









