import sys

cost = [[0, 0, 0]]
n = int(sys.stdin.readline().strip())

for i in range(1, n + 1):
    r, g, b = map(int, sys.stdin.readline().split())
    pre = cost[i - 1]
    new_cost = [r + min(pre[1], pre[2]), g + min(pre[0], pre[2]), b + min(pre[0], pre[1])]
    cost.append(new_cost)

print(min(cost[-1]))