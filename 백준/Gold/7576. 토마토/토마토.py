import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
box = []
for _ in range(n):
    box.append(list(map(int, sys.stdin.readline().split())))

ripe = [[False] * m for _ in range(n)]
starts = []
for y in range(n):
    for x in range(m):
        if box[y][x] == 1:
            starts.append((y, x))
            ripe[y][x] = True
        elif box[y][x] == -1:
            ripe[y][x] = True

directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
days = 0
queue = deque(starts)
while queue:
    new = deque([])
    for _ in range(len(queue)):
        tomato = queue.popleft()
        for direction in directions:
            new_y = tomato[0] + direction[0]
            new_x = tomato[1] + direction[1]
            if 0 <= new_x < m and 0 <= new_y < n:
                if not ripe[new_y][new_x]:
                    new.append((new_y, new_x))
                    ripe[new_y][new_x] = True
    if new:
        days += 1
        queue = queue + new

all_ripe = True
for y in range(n):
    for x in range(m):
        if box[y][x] == 0 and not ripe[y][x]:
            all_ripe = False
            break

if all_ripe:
    print(days)
else:
    print(-1)