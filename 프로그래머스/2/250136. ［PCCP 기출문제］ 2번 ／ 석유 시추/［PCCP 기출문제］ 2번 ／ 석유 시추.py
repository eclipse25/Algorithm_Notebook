from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    visited = [[False] * m for _ in range(n)]
    
    count = 0
    chunks = {}
    ch_x = {x: set() for x in range(m)}
    drts = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for x in range(m):
        for y in range(n):
            if land[y][x] == 1 and not visited[y][x]:
                visited[y][x] = True
                count += 1
                chunks[count] = 1
                ch_x[x].add(count)
                queue = deque([(y, x)])
                while queue:
                    center = queue.popleft()
                    for drt in drts:
                        new_x = center[1] + drt[1]
                        new_y = center[0] + drt[0]
                        if not 0 <= new_x < m or not 0 <= new_y < n:
                            continue
                        if land[new_y][new_x] == 1 and not visited[new_y][new_x]:
                            queue.append((new_y, new_x))
                            visited[new_y][new_x] = True
                            chunks[count] += 1
                            ch_x[new_x].add(count)

    answer = 0
    for key, value in ch_x.items():
        amount = 0
        for v in value:
            amount += chunks[v]
        answer = max(answer, amount)
    
    return answer