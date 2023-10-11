# 2644 촌수계산 - dfs 실버2
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

# dfs로도 풀 수는 있지만 공통된 가장 가까운 조상보다 더 위의 노드를 지나갈 수 있으므로 
# 이런 경우 올라간 만큼 횟수를 빼주는 처리를 해주어야 한다. 