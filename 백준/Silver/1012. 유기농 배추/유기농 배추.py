import sys

def dfs(x, y, field, visited):
  # 스택 초기화 및 시작 노드 추가
  stack = [(x, y)]
  while stack:
    (x, y) = stack.pop()
    # 현재 위치를 방문 처리
    if visited[y][x] == False:
      visited[y][x] = True
      # 상하좌우 네 방향에 대해 탐색
      for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        # 필드 안에 있고, 방문하지 않았으며, 배추가 심어져 있는지 확인
        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and field[ny][nx] == 1:
          stack.append((nx, ny))


t = int(sys.stdin.readline()) 
for _ in range(t):
  # 배추밭의 가로길이 m, 세로길이 n, 배추 위치의 개수 k
  m, n, k = map(int, sys.stdin.readline().split())
  field = [[0] * m for _ in range(n)]  # 배추밭 초기화
  visited = [[False] * m for _ in range(n)]  # 방문 여부 체크 초기화

  # 배추 위치 입력 받기
  for _ in range(k):
    x, y = map(int,sys.stdin.readline().split())
    field[y][x] = 1  # 배추 위치를 1로 표시

  # 필요한 지렁이 수 초기화
  worms = 0

  for i in range(n):
    for j in range(m):
      if field[i][j] == 1 and not visited[i][j]:
        dfs(j, i, field,visited)
        worms += 1

  print(worms)