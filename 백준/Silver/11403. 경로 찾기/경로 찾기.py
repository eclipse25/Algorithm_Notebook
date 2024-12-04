import sys
from collections import deque

n = int(sys.stdin.readline())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

graph = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            graph[i].append(j)

for i in range(n):
    visited = [0 for _ in range(n)]
    queue = deque(graph[i])
    for v in graph[i]:
        visited[v] = 1
    while queue:
        node = queue.popleft()
        for k in graph[node]:
            if not visited[k]:
                visited[k] = 1
                queue.append(k)
    print(' '.join(list(map(str, visited))))