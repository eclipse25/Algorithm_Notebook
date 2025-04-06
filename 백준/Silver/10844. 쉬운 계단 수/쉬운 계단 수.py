n = int(input())

# dp[i][j]는 길이가 i이고, 마지막 숫자가 j인 계단 수의 개수
dp = [[0] * 10 for _ in range(n + 1)]

# 길이가 1일 때는 0을 제외하고 1~9가 모두 계단 수
for j in range(1, 10):
    dp[1][j] = 1

# 1자리가 늘어날 때마다 이전 자리수의 마지막 숫자에서 -1 또는 +1한 수를 붙이면 됨
# 마지막 자릿수가 j인 수는 이전 자릿수의 j-1 또는 j+1에서 올 수 있음
for i in range(2, n + 1):
    for j in range(10):
        if j > 0:
            dp[i][j] += dp[i - 1][j - 1]
        if j < 9:
            dp[i][j] += dp[i - 1][j + 1]

# 정답을 1,000,000,000으로 나눈 나머지
print(sum(dp[n]) % 1000000000)