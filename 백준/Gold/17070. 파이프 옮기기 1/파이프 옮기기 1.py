import sys
import pprint

n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1

for i in range(n):
    for j in range(2, n):
        if grid[i][j] == 1:
            continue
        
        # 이동 후 가로 형태로 놓이는 경우 - 0
        if grid[i][j - 1] == 0:
            dp[i][j][0] += dp[i][j - 1][0]
            if i > 0:
                dp[i][j][0] += dp[i][j - 1][2]

        # 이동 후 세로 형태로 놓이는 경우 - 1
        if grid[i - 1][j] == 0:
            dp[i][j][1] += dp[i - 1][j][1]
            dp[i][j][1] += dp[i - 1][j][2]

        # 이동 후 대각선 형태로 놓이는 경우 - 2
        if i > 0 and sum([grid[i - 1][j - 1], grid[i - 1][j], grid[i][j - 1]]) == 0:
            dp[i][j][2] += dp[i - 1][j - 1][0]
            dp[i][j][2] += dp[i - 1][j - 1][1]
            dp[i][j][2] += dp[i - 1][j - 1][2]

print(sum(dp[n - 1][n - 1]))