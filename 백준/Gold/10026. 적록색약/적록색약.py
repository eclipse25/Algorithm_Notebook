import sys
from collections import deque

n = int(sys.stdin.readline())
picture = []
for _ in range(n):
    picture.append(sys.stdin.readline().strip())

m = len(picture[0])
visited1 = [[False] * m for _ in range(n)]
visited2 = [[False] * m for _ in range(n)]
directions = [(-1, 0), (1, 0),  (0, -1), (0, 1)]
count = [0, 0]
for i in range(n):
    for j in range(m):
        color = picture[i][j]
        if not visited1[i][j]:
            count[0] += 1
            visited1[i][j] = True
            queue = deque([(i, j)])
            while queue:
                current = queue.popleft()
                for direction in directions:
                    new_y = current[0] + direction[0]
                    new_x = current[1] + direction[1]
                    if 0 <= new_x < m and 0 <= new_y < n and not visited1[new_y][new_x]:
                        if picture[new_y][new_x] == color:
                            queue.append((new_y, new_x))
                            visited1[new_y][new_x] = True
        if not visited2[i][j]:
            count[1] += 1
            visited2[i][j] = True
            queue = deque([(i, j)])
            while queue:
                current = queue.popleft()
                for direction in directions:
                    new_y = current[0] + direction[0]
                    new_x = current[1] + direction[1]
                    if 0 <= new_x < m and 0 <= new_y < n and not visited2[new_y][new_x]:
                        if picture[new_y][new_x] == color or picture[new_y][new_x] in ['G', 'R'] and color in ['G', 'R']:
                            queue.append((new_y, new_x))
                            visited2[new_y][new_x] = True

print(count[0], count[1])