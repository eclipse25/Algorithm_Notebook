import sys
from collections import deque

n = int(sys.stdin.readline())
map = []
for _ in range(n):
    map.append(sys.stdin.readline())

visited = [[False] * n for _ in range(n)]
complexes = 0
houses = []
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(n):
    for j in range(n):
        if map[i][j] == '1' and visited[i][j] == False:
            visited[i][j] = True
            queue = deque([(i, j)])
            house_count = 1
            while queue:
                element = queue.popleft()
                for direction in directions:
                    new_i = element[0] + direction[0]
                    new_j = element[1] + direction[1]
                    if new_i < 0 or new_i >= n or new_j < 0 or new_j >= n:
                        continue
                    if map[new_i][new_j] == '1' and visited[new_i][new_j] == False:
                        visited[new_i][new_j] = True
                        queue.append((new_i, new_j))
                        house_count += 1
                if not queue:
                    complexes += 1
                    houses.append(house_count)

print(complexes)
houses.sort()
for i in range(complexes):
    print(houses[i])