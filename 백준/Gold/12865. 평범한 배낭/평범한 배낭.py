import sys

n, k = map(int, sys.stdin.readline().split())
things = []

for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    things.append((w, v))

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    w, v = things[i - 1]
    for j in range(1, k + 1):
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[n][k])