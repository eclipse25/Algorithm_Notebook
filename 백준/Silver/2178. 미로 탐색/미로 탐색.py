import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
maze = [sys.stdin.readline()[0:-1] for _ in range(n)]
visited = [[False] * m for _ in range(n)]
count = [[0] * m for _ in range(n)]

def bfs(graph, visited, count):
  visited[0][0] = True
  count[0][0] = 1
  queue = deque([(0, 0)])
  while queue:
    v = queue.popleft()
    for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      nx, ny = v[0] + dx, v[1] + dy
      if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and maze[ny][nx] == '1':
        queue.append((nx, ny))
        visited[ny][nx] = True
        count[ny][nx] = count[v[1]][v[0]] + 1
        if ny == n - 1 and nx == m - 1:
          return count[ny][nx]

print(bfs(maze, visited, count))