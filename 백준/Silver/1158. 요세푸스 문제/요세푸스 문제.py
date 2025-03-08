from collections import deque

n, k = map(int, input().split())
queue = deque([i for i in range(1, n + 1)])

seq = []
while queue:
    for _ in range(k - 1):
        queue.append(queue.popleft())

    seq.append(queue.popleft())

print(f"<{', '.join(map(str, seq))}>")