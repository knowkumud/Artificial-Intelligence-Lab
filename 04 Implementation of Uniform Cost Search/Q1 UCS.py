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
graph = {'S':{1:2,3:5},1:{'G':1},3:{'G':6,4:2},'G':{4:7},4:{5:3,2:4},5:{2:6,'G':3},2:{1:4}}
start = 'S'
goal = 'G'
path,cost = uniformcostsearch(graph,start,goal)
 
if path is not None:
    print(f"Lowest cost path from node {start} to node {goal}: {path}")
    print(f"Total Cost: {cost}")
else:
    print(f"No path from node {start} to node {goal}")
