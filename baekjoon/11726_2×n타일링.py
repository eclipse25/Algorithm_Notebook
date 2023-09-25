# DP, 실버3
n = int(input())
dp = [0] * (n + 2)
dp[1] = 1
dp[2] = 2
if n > 2:
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
print(dp[n])

# i-1번째에서 오른쪽에 한줄짜리 세로블럭 추가 +
# i-2번째에서 눕혀서 쌓인 블럭 두개(정사각형) 추가
