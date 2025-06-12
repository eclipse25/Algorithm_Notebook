import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = [[1, [a[i]]] for i in range(n)]
for i in range(n):
    for j in range(0, i):
        if a[i] > a[j]:
            if dp[i][0] < dp[j][0] + 1:
                dp[i][0] = dp[j][0] + 1
                dp[i][1] = dp[j][1] + [a[i]]

dp.sort(key=lambda x:x[0], reverse=True)

print(dp[0][0])
print(' '.join(map(str, dp[0][1])))
