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
print(graph)
  
set1 = graph.keys()
set2 = []
for k in graph:
    for i in graph.get(k):
        if i not in set2:
            set2.append(i)
set3 = []
for i in set1:
    if i not in set2:
        set3.append(i)

queue = []
        
def BFS(G,v,visited):
    if v not in visited:
        queue.append(v)
        visited[v] = True
    for i in set3:
        if i not in visited:
            queue.append(i)
            visited[i] = True
    while queue:
        pop = queue.pop(0)
        print(pop , end = " ")
        for i in G.get(pop):
            if i not in visited:
                queue.append(i)
                visited[i] = True
    return visited
    
    print(BFS(graph,5,{}))
