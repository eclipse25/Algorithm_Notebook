import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
coord = [list(map(int, input().split())) for _ in range(n)]

# 방향: 북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

count = 0

while True:
    # 1. 현재 칸이 청소되지 않았으면 청소
    if coord[r][c] == 0:
        coord[r][c] = 2
        count += 1

    found = False # 청소할 곳이 있는지 찾음
    for _ in range(4):
        # 반시계 방향 회전
        d = (d + 3) % 4
        ny = r + dy[d]
        nx = c + dx[d]
        if coord[ny][nx] == 0:
            r, c = ny, nx
            found = True
            break

    if not found:
        # 후진
        back_d = (d + 2) % 4
        ny = r + dy[back_d]
        nx = c + dx[back_d]
        if coord[ny][nx] == 1:
            break
        else:
            r, c = ny, nx

print(count)
