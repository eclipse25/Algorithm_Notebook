import sys
import heapq

t, n = map(int, sys.stdin.readline().split())
heap = []
for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    heapq.heappush(heap, [-c, a, b])

curr = 0
while curr < t:
    priority, index, last_time = heapq.heappop(heap)
    print(index)
    if last_time > 1:
        heapq.heappush(heap, [priority + 1, index, last_time - 1])
    curr += 1
