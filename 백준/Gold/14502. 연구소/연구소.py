import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

empty, virus = [], []

for y in range(n):
    for x in range(m):
        if grid[y][x] == 0:
            empty.append((y, x))
        elif grid[y][x] == 2:
            virus.append((y, x))

max_safe = 0

for walls in combinations(empty, 3):
    # 깊은 복사
    temp = [row[:] for row in grid]

    for wy, wx in walls:
        temp[wy][wx] = 1

    queue = deque(virus)
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and temp[ny][nx] == 0:
                temp[ny][nx] = 2
                queue.append((ny, nx))

    safe = sum(row.count(0) for row in temp)
    max_safe = max(max_safe, safe)

print(max_safe)