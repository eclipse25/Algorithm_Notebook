import sys
n = int(sys.stdin.readline())
A = []
for i in range(n):
  A.append([int(sys.stdin.readline()), i])

A_sorted = sorted(A)
max_diff = 0
for i in range(len(A)):
  max_diff = max(max_diff, A_sorted[i][1] - i)
print(max_diff + 1)