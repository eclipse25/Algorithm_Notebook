import heapq
import sys

n = int(input())
numbers = []
heapq.heapify(numbers)
for _ in range(n):
    number = int(sys.stdin.readline())
    if number == 0:
        if not numbers:
            print(0)
        else:
            print(heapq.heappop(numbers))
    else:
        heapq.heappush(numbers, number)