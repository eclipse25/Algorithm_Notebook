import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
prefix_sum, num_sum = [0], 0
for i in range(n):
    num_sum += numbers[i]
    prefix_sum.append(num_sum)

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    print(prefix_sum[end] - prefix_sum[start - 1])