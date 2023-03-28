from queue import PriorityQueue

def ucs(graph,start,goal):
    frontier=PriorityQueue()
    frontier.put((0,start,[]))# initial state cost,current node,path taken
    visited=set()

    while not frontier.empty():
        cost,current,path=frontier.get()
        if current ==goal:
            return path+[current]
        if current in visited:
            continue
        visited.add(current)
        for neighbour,weight in graph[current].items():
            if neighbour not in visited:
                total_cost=cost+weight
                frontier.put((total_cost,neighbour,path+[current]))
    return None


g = {
    'A': {'B': 3, 'D': 1},
    'B': {'C': 1, 'D': 3},
    'C': {'E': 2},
    'D': {'E': 4},
    'E': {}
}

start = 'A'
goal = 'E'
print(ucs(g,start,goal))

