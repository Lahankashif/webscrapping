import heapq
def dijkstra(graph, start, end):
    shortest_paths = {start: (0, [])}
    list = [(0, start, [])]
    while list:
        (cost, current, path) = heapq.heappop(list)
        if current == end:
            return (cost, path + [current])  
        for neighbor, edge_cost in graph[current].items():
            old_cost = shortest_paths.get(neighbor, (float('inf'), []))[0]
            new_cost = cost + edge_cost
            if new_cost < old_cost:
                shortest_paths[neighbor] = (new_cost, path + [current])
                heapq.heappush(list, (new_cost, neighbor, path + [current]))  
graph = {
    'A': {'B': 3, 'D': 8},
    'B': {'A': 3, 'D': 5, 'E': 6},
    'D': {'A': 8, 'B': 5, 'E': 3, 'F': 2},
    'E': {'B': 6, 'D': 3, 'F': 1, 'C': 9},
    'F': {'D': 2, 'E': 1, 'C': 3},
    'C': {'E': 9, 'F': 3, 'C': 0}
}
start_node = 'A'
end_node = 'C'
result = dijkstra(graph, start_node, end_node)

if result:
    cost, path = result
    print(f"The shortest path from {start_node} to {end_node} with a cost of {cost} is {path}")
else:
    print(f"There is no path from {start_node} to {end_node}")