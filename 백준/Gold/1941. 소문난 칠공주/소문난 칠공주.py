import sys
from itertools import combinations
from collections import deque

grid = [list(sys.stdin.readline().strip()) for _ in range(5)]
coord = []
for i in range(5):
    for j in range(5):
        coord.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

for case in combinations(coord, 7):
    s_count = 0
    for y, x in case:
        if grid[y][x] == 'S':
            s_count += 1
    if s_count < 4:
        continue

    visited = [[False] * 5 for _ in range(5)]
    visited[case[0][0]][case[0][1]] = True
    queue = deque([case[0]])
    count = 1

    while queue:
        node = queue.popleft()
        for i in range(4):
            new_y = node[0] + dy[i]
            new_x = node[1] + dx[i]
            if (new_y, new_x) in case and not visited[new_y][new_x]:
                visited[new_y][new_x] = True
                queue.append((new_y, new_x))
                count += 1
    
    if count == 7:
        answer += 1

print(answer)