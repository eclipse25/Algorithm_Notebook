import sys
import heapq

n = int(sys.stdin.readline())
array = []
heapq.heapify(array)
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if array:
            print(heapq.heappop(array) * -1)
        else:
            print(0)
    else:
        heapq.heappush(array, x * -1)