import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
rel = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    rel[a].append(b)
    rel[b].append(a)

kb_nums = [0]
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    visited[i] = True
    queue = deque([i])
    steps = [0] * (n + 1)
    while queue:
        element = queue.popleft()
        if rel[element]:
            for friend in rel[element]:
                if not visited[friend]:
                    visited[friend] = True
                    steps[friend] = steps[element] + 1
                    queue.append(friend)
    kb_nums.append(sum(steps))

print(kb_nums.index(min(kb_nums[1:])))