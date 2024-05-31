import sys

n, k = map(int, sys.stdin.readline().split())
values = []
for _ in range(n):
    values.append(int(sys.stdin.readline()))

num = 0
for i in range(n-1, -1, -1):
    if k >= values[i]:
        num += k // values[i]
        k = k % values[i]
    if k == 0:
        break

print(num)