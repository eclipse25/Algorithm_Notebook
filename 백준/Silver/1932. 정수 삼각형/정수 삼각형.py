import sys
from pprint import pprint

n = int(sys.stdin.readline())

triangle = []
for _ in range(n):
    triangle.append(list(map(int, sys.stdin.readline().split())))

dp = [[0] * (i + 1) for i in range(n)]
dp[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(0, i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][0] + triangle[i][j]
        elif j == i:
            dp[i][j] = dp[i - 1][i - 1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

print(max(dp[n - 1]))