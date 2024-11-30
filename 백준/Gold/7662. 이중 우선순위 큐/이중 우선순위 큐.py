import sys
import heapq

for _ in range(int(sys.stdin.readline())):
    min_heap = []
    max_heap = []
    count = {}
    for i in range(int(sys.stdin.readline())):
        op = sys.stdin.readline().split()
        c, n = op[0], int(op[1])

        if c == "I":
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
            count[n] = count.get(n, 0) + 1
        else:
            if not min_heap or not max_heap:
                continue
            if n == -1:
                while min_heap and count.get(min_heap[0]) == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    count[min_heap[0]] -= 1
                    heapq.heappop(min_heap)
            else:
                while max_heap and count.get(-max_heap[0]) == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    count[-max_heap[0]] -= 1
                    heapq.heappop(max_heap)
    
    while min_heap and count.get(min_heap[0]) == 0:
        heapq.heappop(min_heap)
    while max_heap and count.get(-max_heap[0]) == 0:
        heapq.heappop(max_heap)

    if min_heap == []:
        print("EMPTY")
    else:
        print(-max_heap[0], min_heap[0])