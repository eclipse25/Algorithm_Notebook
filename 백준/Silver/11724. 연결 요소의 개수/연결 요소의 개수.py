import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
queue = deque([])
cc_count = 0
for i in range(1, n + 1):
    if not visited[i]:
        queue.append(i)
        while queue:
            element = queue.popleft()
            visited[element] = True
            for neighbor in graph[element]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        cc_count += 1

print(cc_count)