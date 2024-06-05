import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
mapping = []
y, x = -1, -1
for i in range(n):
    mapping.append(list(map(int, sys.stdin.readline().split())))
    if 2 in mapping[i]:
        y, x = i, mapping[i].index(2)

distance = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if mapping[i][j] == 0:
            distance[i][j] = 0

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
distance[y][x], current = 0, 0
queue = deque([(y, x)])
while queue:
    new_queue = deque([])
    current += 1
    for _ in range(len(queue)):
        point = queue.popleft()
        for direction in directions:
            new_y = point[0] + direction[0]
            new_x = point[1] + direction[1]
            if 0 <= new_x < m and 0 <= new_y < n:
                if distance[new_y][new_x] == -1 and mapping[new_y][new_x] != 0:
                    distance[new_y][new_x] = current
                    new_queue.append((new_y, new_x))
    queue = new_queue

for i in range(len(distance)):
    for j in range(len(distance[i])):
        print(distance[i][j], end=' ')
    print()