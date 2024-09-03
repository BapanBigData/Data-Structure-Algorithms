
# graph representations: adjacency list

def add_edge(adj, u, v, directed=True):
    adj[u].append(v)
    
    if directed:
        adj[v].append(u)
        

def print_graph(adj):
    for e in adj:
        print(e)


# driver code (undirected graph)
V = 4
adj = [[] for _ in range(V)]
add_edge(adj, 0, 1)
add_edge(adj, 0, 2)
add_edge(adj, 1, 2)
add_edge(adj, 1, 3)

#print_graph(adj)

# let's define a directed graph
V = 5
adj = [[] for _ in range(V)]
add_edge(adj, 0, 1, False)
add_edge(adj, 0, 2, False)
add_edge(adj, 1, 2, False)
add_edge(adj, 2, 1, False)
add_edge(adj, 2, 3, False)
add_edge(adj, 3, 1, False)
add_edge(adj, 3, 4, False)
print_graph(adj)

