from queue import PriorityQueue

def uniformcostsearch(graph,start,goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0,start,[]))
    while not queue.empty():
        (cost,node,path) = queue.get()
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == goal:
                return path,cost
            for neighbour in graph[node]:
                if neighbour not in visited:
                    totalcost = cost + graph[node][neighbour]
                    queue.put((totalcost,neighbour,path))
    return None
graph = {'a':{'b':6,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':9},'e':{'d':7}}
start = 'a'
goal = 'e'
path,cost = uniformcostsearch(graph,start,goal)

if path is not None:
    print(f"Lowest cost path from node {start} to node {goal}: {path}")
    print(f"Total Cost: {cost}")
else:
    print(f"No path from node {start} to node {goal}")
