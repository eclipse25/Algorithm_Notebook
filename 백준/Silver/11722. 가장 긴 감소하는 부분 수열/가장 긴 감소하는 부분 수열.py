n = int(input())
numbers = list(map(int, input().split()))

if n == 1:
    print(1)
else:
    dp = [1] * n
    for i in range(1, n):
      lar = [0]
      for j in range(0,i):
        if numbers[j] > numbers[i]:
          lar.append(dp[j])
      dp[i] = max(lar) + 1
    print(max(dp))