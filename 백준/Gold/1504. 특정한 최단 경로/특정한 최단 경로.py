import sys
import heapq

n, e = map(int, sys.stdin.readline().split())
graph = {v + 1: [] for v in range(n)}

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(start):
    distance = {i + 1: float('inf') for i in range(n)}
    distance[start] = 0
    queue = [(0, start)]
    while queue:
        dist, current = heapq.heappop(queue)
        if dist > distance[current]:
            continue
        for weight, neighbor in graph[current]:
            new_dist = dist + weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(queue, (new_dist, neighbor))
    return distance

dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[n]
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[n]

answer = min(path1, path2)
print(answer if answer != float('inf') else -1)
