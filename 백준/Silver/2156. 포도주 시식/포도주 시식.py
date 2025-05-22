import sys

n = int(sys.stdin.readline())
amounts = [int(sys.stdin.readline()) for _ in range(n)]

if n == 1:
    print(amounts[0])
elif n == 2:
    print(amounts[0] + amounts[1])
else:
    dp = [
        amounts[0],
        amounts[0] + amounts[1],
        max(amounts[0] + amounts[1], amounts[0] + amounts[2], amounts[1] + amounts[2])
    ]
    for i in range(3, n):
        max_amount = max(
            dp[i - 1], 
            dp[i - 2] + amounts[i], 
            dp[i - 3] + amounts[i - 1] + amounts[i]
        )
        dp.append(max_amount)

    print(dp[n - 1])