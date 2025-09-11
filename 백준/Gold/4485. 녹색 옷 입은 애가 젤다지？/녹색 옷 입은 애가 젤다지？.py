import sys
import heapq

i = 1
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    heap = [(grid[0][0], 0, 0)]
    cost = [[float("inf")] * n for _ in range(n)]
    cost[0][0] = grid[0][0]

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while heap:
        node = heapq.heappop(heap)
        if node[0] > cost[node[1]][node[2]]:
            continue
        for y, x in dirs:
            new_y, new_x = node[1] + y, node[2] + x
            if 0 <= new_y < n and 0 <= new_x < n:
                if cost[new_y][new_x] > cost[node[1]][node[2]] + grid[new_y][new_x]:
                    cost[new_y][new_x] = cost[node[1]][node[2]] + grid[new_y][new_x]
                    heapq.heappush(heap, (cost[new_y][new_x], new_y, new_x))

    print(f"Problem {i}:", cost[n - 1][n - 1])
    i += 1
