import sys
from collections import deque

n, w, l = map(int, sys.stdin.readline().split())
trucks = deque(map(int, sys.stdin.readline().split()))

queue = deque([0] * w)
time = 0
i = 0
weight = 0
while True:
    time += 1
    out = queue.popleft()
    weight -= out
    if trucks[i] + weight <= l:
        queue.append(trucks[i])
        weight += trucks[i]
        i += 1
    else:
        queue.append(0)
    
    if i >= n:
        break

print(time + w)