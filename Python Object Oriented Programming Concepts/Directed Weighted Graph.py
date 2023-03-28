def add_vertex(v):
  global graph
  if v in graph:
    print("Vertex ", v, " already exists.")
  else:
    graph[v] = []

def add_edge(v1, v2):
    temp = v2
    graph[v1].append(temp)

def print_graph():
  global graph
  for vertex in graph:
    for edges in graph[vertex]:
      print("(",vertex, " -> ", edges,")" , end = " ")
    print()

graph = {}
add_vertex(0),add_vertex(1),add_vertex(2),add_vertex(3),add_vertex(4),add_vertex(5)
add_edge(0, 1)
add_edge(1, 2)
add_edge(2, 0)
add_edge(2, 1)
add_edge(3, 2)
add_edge(4, 5)
add_edge(5, 4)
print_graph()
