import heapq

def dijkstra(graph, start):
    dist = {v: float('inf') for v in graph}
    prev = {v: None for v in graph}
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        current_dist, u = heapq.heappop(heap)
        if current_dist > dist[u]:
            continue
        for v, weight in graph[u]:
            new_dist = dist[u] + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(heap, (new_dist, v))

    return dist, prev

def reconstruct_path(prev, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = prev[current]
    path.reverse()
    if path[0] == start:
        return path
    return []

graph = {
    'A': [('B', 5), ('C', 1)],
    'B': [('A', 5), ('C', 2), ('D', 1)],
    'C': [('A', 1), ('B', 2), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

start_vertex = 'A'
distances, previous = dijkstra(graph, start_vertex)

print("Найкоротші відстані:")
print(distances)

print("\nНайкоротші шляхи від вершини A:")
for vertex in graph:
    path = reconstruct_path(previous, start_vertex, vertex)
    print(f"{vertex}: {path}")
