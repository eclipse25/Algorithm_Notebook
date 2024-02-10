import sys

t = int(sys.stdin.readline())
n = [int(sys.stdin.readline()) for _ in range(t)]

for i in n:
  if i == 0:
    print(1, 0)
    continue
  elif i == 1:
    print(0, 1)
    continue

  dp_0 = [1, 0]
  dp_1 = [0, 1]
  for j in range(2, i + 1):
    dp_0.append(dp_0[j - 1] + dp_0[j - 2])
    dp_1.append(dp_1[j - 1] + dp_1[j - 2])

  print(dp_0[i], dp_1[i])