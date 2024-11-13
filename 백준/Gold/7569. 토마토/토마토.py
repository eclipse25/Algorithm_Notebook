import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

coord = []
riped = []
total_tomatoes = 0

for i in range(h):
    floor = []
    for j in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        floor.append(row)
        for k in range(m):
            if row[k] == 1:
                riped.append((i, j, k))
                total_tomatoes += 1
            elif row[k] == 0:
                total_tomatoes += 1
    coord.append(floor)

directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

def bfs(graph, start):
    if len(riped) == total_tomatoes:
        return 0
    queue = deque(start)
    days = -1
    
    while queue:
        days += 1
        for _ in range(len(queue)):
            tomato = queue.popleft()
            x, y, z = tomato
            
            for dx, dy, dz in directions:
                nx, ny, nz = x + dx, y + dy, z + dz
                
                if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                    if graph[nx][ny][nz] == 0:
                        graph[nx][ny][nz] = 1
                        queue.append((nx, ny, nz))

    for layer in graph:
        for row in layer:
            if 0 in row:
                return -1
    
    return days

result = bfs(coord, riped)
print(result)
