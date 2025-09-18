import sys
from collections import deque

n = int(sys.stdin.readline())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [-1] * (n + 1)
parent[0], parent[1] = 0, 0
queue = deque([1])
while queue:
    node = queue.popleft()
    for child in graph[node]:
        if parent[child] == -1:
            parent[child] = node
            queue.append(child)

for i in range(2, n + 1):
    print(parent[i])
