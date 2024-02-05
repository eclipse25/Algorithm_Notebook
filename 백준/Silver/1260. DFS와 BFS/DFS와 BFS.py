import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n + 1)]

for i in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

for i in graph:
    i.sort()

visited = [False] * (n + 1)
def dfs(graph, v, visited):
  visited[v] = True
  print(v, end = ' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end = ' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

dfs(graph, v, visited)
print()
visited = [False] * (n + 1)
bfs(graph, v, visited)