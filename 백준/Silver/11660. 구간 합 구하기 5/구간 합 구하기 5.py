import sys

table = []
n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    table.append(list(map(int, sys.stdin.readline().split())))

p_sum = [[0] * (n + 1) for _ in range(n + 1)] 

for i in range(1, n + 1):
    for j in range(1, n + 1):
        p_sum[i][j] = table[i - 1][j - 1] + p_sum[i - 1][j] + p_sum[i][j - 1] - p_sum[i - 1][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    answer = p_sum[x2][y2]
    if x1 > 1:
        answer -= p_sum[x1 - 1][y2]
    if y1 > 1:
        answer -= p_sum[x2][y1 - 1]
    if x1 > 1 and y1 > 1:
        answer += p_sum[x1 - 1][y1 - 1]

    print(answer)
