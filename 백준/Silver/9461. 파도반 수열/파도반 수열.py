import sys

t = int(sys.stdin.readline())
dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for _ in range(t):
    n = int(sys.stdin.readline())
    if n <= len(dp) - 1:
        print(dp[n])
    else:
        for i in range(len(dp), n + 1):
            dp.append(dp[i - 5] + dp[i - 1])
        print(dp[n])