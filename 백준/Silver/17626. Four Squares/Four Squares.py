import sys

n = int(sys.stdin.readline())
dp = [4] * (n + 1)
dp[0], dp[1] = 0, 1

for i in range(2, n + 1):
    k = 1
    while k * k <= i:
        dp[i] = min(dp[i], dp[i - k * k] + 1)
        k += 1

print(dp[n])