import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
visited = [False] * 100001
queue = deque([n])
t, flg = 0, False
if n == k:
    flg = True
while n <= 100000 and not flg:
    t += 1
    new_queue = deque([])
    for i in range(len(queue)):
        new = queue.popleft()
        visited[new] = True
        for j in [new + 1, new - 1, new * 2]:
            if j > 100000 or j < 0:
                continue
            if not visited[j]:
                visited[j] = True
                new_queue.append(j)
            if j == k:
                flg = True
                break
    queue = new_queue
print(t)