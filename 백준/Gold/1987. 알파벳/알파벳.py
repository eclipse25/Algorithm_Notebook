import sys

r, c = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_count = 0

# DP 상태 저장: (y, x) 위치에서 어떤 bitmask로 왔는지
visited_states = [[set() for _ in range(c)] for _ in range(r)]

def dfs(x, y, bitmask, count):
    global max_count

    if bitmask in visited_states[y][x]:
        return  # 이미 같은 상태로 탐색했으므로 스킵
    visited_states[y][x].add(bitmask)

    max_count = max(max_count, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < c and 0 <= ny < r:
            char = board[ny][nx]
            bit = 1 << (ord(char) - ord('A'))
            if not (bitmask & bit):  # 해당 알파벳을 방문한 적 없다면
                dfs(nx, ny, bitmask | bit, count + 1)

start_char = board[0][0]
start_bit = 1 << (ord(start_char) - ord('A'))

dfs(0, 0, start_bit, 1)
print(max_count)
