def add_vertex(v):
  global graph
  if v in graph:
    print("Vertex ", v, " already exists.")
  else:
    graph[v] = []

def add_edge(v1, v2):
    temp = v2
    graph[v1].append(temp)

graph = {}
add_vertex(0),add_vertex(1),add_vertex(2),add_vertex(3),add_vertex(4),add_vertex(5)
add_edge(5,0)
add_edge(5,2)
add_edge(4,0)
add_edge(4,1)
add_edge(2,3)
add_edge(3,1)
def DFS(G,v,visited):
    if v not in visited:
        visited.append(v)
        for k in graph[v]:
            DFS(graph,k,visited)
    return visited
visited = DFS(graph,5,[])
visited = DFS(graph,4,visited) 
print(visited)
