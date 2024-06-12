import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
campus, start = [], (0, 0)
visited = [[False] * m for _ in range(n)]
for i in range(n):
    campus.append(sys.stdin.readline())
    for j in range(m):
        if campus[i][j] == 'I':
            start = (i, j)
            visited[i][j] = True
        elif campus[i][j] == 'X':
            visited[i][j] = True

queue = deque([start])
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
count = 0
while queue:
    location = queue.popleft()
    for direction in directions:
        new_y = location[0] + direction[0]
        new_x = location[1] + direction[1]
        if 0 <= new_y < n and 0 <= new_x < m and not visited[new_y][new_x]:
            visited[new_y][new_x] = True
            queue.append((new_y, new_x))
            if campus[new_y][new_x] == 'P':
                count += 1

if count == 0:
    print('TT')
else:
    print(count)