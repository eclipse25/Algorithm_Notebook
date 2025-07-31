import sys

table = []
n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    table.append(list(map(int, sys.stdin.readline().split())))

dpt = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        dpt[i][j] = (
            dpt[i - 1][j] + dpt[i][j - 1] - dpt[i - 1][j - 1] + table[i - 1][j - 1]
        )

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    answer = dpt[x2][y2] - dpt[x1 - 1][y2] - dpt[x2][y1 - 1] + dpt[x1 - 1][y1 - 1]
    print(answer)