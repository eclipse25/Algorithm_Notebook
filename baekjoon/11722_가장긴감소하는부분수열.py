# DP, 실버2
n = int(input())
numbers = list(map(int, input().split()))

if n == 1:
    print(1)
else:
    dp = [1] * n
    for i in range(1, n):
        lar = [0]
        for j in range(0, i):
            if numbers[j] > numbers[i]:
                lar.append(dp[j])  # 앞에있는 자신보다 큰값중
        dp[i] = max(lar) + 1
    print(max(dp))
# 앞에있는 자신보다 큰값 중
# 그 수까지 가장 감소하는 길이가 큰 수를 찾아 길이에 1을 더함
