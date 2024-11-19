import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

queue = deque([i + 1 for i in range(n)])
seq = []
while queue:
    for _ in range(k - 1):
        queue.append(queue.popleft())
    seq.append(queue.popleft())

print(f"<{', '.join(map(str, seq))}>")