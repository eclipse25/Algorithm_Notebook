n = int(input())
dp = [[0, []] for _ in range(n + 1)]  # [연산 수, 경로]
dp[1] = [0, [1]]

for i in range(2, n + 1):
    min_ops, path = dp[i - 1][0], dp[i - 1][1]

    if i % 2 == 0 and dp[i // 2][0] < min_ops:
        min_ops, path = dp[i // 2][0], dp[i // 2][1]

    if i % 3 == 0 and dp[i // 3][0] < min_ops:
        min_ops, path = dp[i // 3][0], dp[i // 3][1]

    dp[i] = [min_ops + 1, path + [i]]

print(dp[n][0])
print(*reversed(dp[n][1]))
