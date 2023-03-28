  print("Vertex ", v, " already exists.")
  else:
    graph[v] = []

def add_edge(v1, v2, e):
    temp = [v2, e]
    graph[v1].append(temp)

def print_graph():
  global graph
  for vertex in graph:
    for edges in graph[vertex]:
      print("(", vertex, "->", edges[0],",",edges[1], ")",end = " ")
    print()

graph = {}
add_vertex(0)
add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)
add_vertex(5)
add_edge(0, 1, 6)
add_edge(1, 2, 7)
add_edge(2, 0, 5)
add_edge(2, 1, 4)
add_edge(3, 2, 10)
add_edge(4, 5, 3)
add_edge(5, 4, 1)
print_graph()
