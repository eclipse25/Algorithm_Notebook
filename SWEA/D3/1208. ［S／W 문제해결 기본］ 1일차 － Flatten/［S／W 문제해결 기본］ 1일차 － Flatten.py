import heapq

for test_case in range(1, 11):
    dump_limit = int(input())
    heights = list(map(int, input().split()))
    min_heap = heights[:]
    max_heap = [-h for h in heights]
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)
    
    for _ in range(dump_limit):
        min_val = heapq.heappop(min_heap)
        max_val = -heapq.heappop(max_heap)

        if max_val - min_val <= 1:
            break

        min_val += 1
        max_val -= 1
        heapq.heappush(min_heap, min_val)
        heapq.heappush(max_heap, -max_val)
        
    print(f"#{test_case} {-heapq.heappop(max_heap) - heapq.heappop(min_heap)}")