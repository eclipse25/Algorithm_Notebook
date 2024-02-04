import sys
from collections import deque

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    p, c = map(int, sys.stdin.readline().split())
    graph[p].append(c)
    graph[c].append(p)

visited = [False] * (n + 1)
count = [-1] * (n + 1)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    count[start] = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                count[i] = count[v] + 1
                queue.append(i)
                visited[i] = True
              
bfs(a)
print(count[b])