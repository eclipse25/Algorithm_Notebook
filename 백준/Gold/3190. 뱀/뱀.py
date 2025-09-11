import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())

# 0: 빈칸, 1: 사과, -1: 뱀 몸
board = [[0] * n for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1

l = int(input())
turns = {}  # time -> 'L' or 'D'
for _ in range(l):
    x, c = input().split()
    turns[int(x)] = c

# 시계 방향: R, D, L, U
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_idx = 0

snake = deque([(0, 0)])  # 머리부터 꼬리까지
board[0][0] = -1
y, x = 0, 0
time = 0

while True:
    time += 1
    dy, dx = dirs[dir_idx]
    ny, nx = y + dy, x + dx

    # 벽/자기몸 충돌
    if not (0 <= ny < n and 0 <= nx < n) or board[ny][nx] == -1:
        print(time)
        break

    # 사과면 꼬리 유지
    if board[ny][nx] == 1:
        board[ny][nx] = -1
        snake.appendleft((ny, nx))
    else:
        # 빈칸이면 한 칸 줄임
        tail_y, tail_x = snake.pop()
        board[tail_y][tail_x] = 0
        board[ny][nx] = -1
        snake.appendleft((ny, nx))

    y, x = ny, nx

    # X초가 끝난 뒤 회전
    if time in turns:
        if turns[time] == "D":  # 오른쪽
            dir_idx = (dir_idx + 1) % 4
        else:  # "L" 왼쪽
            dir_idx = (dir_idx - 1) % 4
