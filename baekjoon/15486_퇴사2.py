# DP, 골드5
import sys
n = int(sys.stdin.readline())
end_day_dict = {}

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    end_day = i + a
    if end_day in end_day_dict:
        end_day_dict[end_day].append((i, b))
    else:
        end_day_dict[end_day] = [(i, b)]

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = dp[i - 1]
    if i in end_day_dict:
        for j, point in end_day_dict[i]:
            dp[i] = max(dp[i], dp[j] + point)
print(dp[n])
# 시간복잡도 해결 위해 딕셔너리 사용
