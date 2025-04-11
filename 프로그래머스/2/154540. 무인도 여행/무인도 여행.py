from collections import deque

def solution(maps):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    answer = []
    lenx = len(maps[0])
    leny = len(maps)
    visited = [[False] * lenx for _ in range(leny)]
    
    for y in range(leny):
        for x in range(lenx):
            if maps[y][x] != 'X' and not visited[y][x]:
                visited[y][x] = True
                num = int(maps[y][x])
                queue = deque([(y, x)])
                while queue:
                    node = queue.popleft()
                    for dir in dirs:
                        new_y = node[0] + dir[0]
                        new_x = node[1] + dir[1]
                        if new_x < 0 or lenx <= new_x:
                            continue
                        if new_y < 0 or leny <= new_y:
                            continue
                        if maps[new_y][new_x] != 'X' and not visited[new_y][new_x]:
                            queue.append((new_y, new_x))
                            num += int(maps[new_y][new_x])
                            visited[new_y][new_x] = True
                answer.append(num)        
                
    answer.sort()
    if not answer:
        answer = [-1]
    return answer