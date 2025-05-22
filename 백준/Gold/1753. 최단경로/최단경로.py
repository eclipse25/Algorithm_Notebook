import sys
import heapq

nv, ne = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline().strip())

graph = {v + 1: [] for v in range(nv)}
for i in range(ne):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

distance = {v: float('inf') for v in graph}
distance[start] = 0
queue = [(0, start)]

while queue:
    dist, node = heapq.heappop(queue)
    if dist > distance[node]:
        continue
    for neighbor, weight in graph[node]:
        new_dist = distance[node] + weight
        if new_dist < distance[neighbor]:
            distance[neighbor] = new_dist
            heapq.heappush(queue, (distance[neighbor], neighbor))

for v in range(1, nv + 1):
    dist = distance[v]
    if dist != float('inf'):
        print(dist)
    else:
        print("INF")