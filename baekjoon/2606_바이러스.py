# 2606 바이러스 - dfs, bfs 실버3
import sys

n = int(sys.stdin.readline())
p = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]

for i in range(p):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

i = []
visited = [False] * (n + 1)

def dfs(graph, start, visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)

count = 0
for i in range(2, len(visited)):
    if visited[i] == True:
        count += 1

print(count)