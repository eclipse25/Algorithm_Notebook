import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

city = []

for _ in range(n):
    city.append(list(map(int, sys.stdin.readline().split())))

stores = []
houses = []
for y in range(n):
    for x in range(n):
        if city[y][x] == 2:
            stores.append((y, x))
        elif city[y][x] == 1:
            houses.append((y, x))

min_distance = float('inf')
for comb in combinations(stores, m):
    total = 0
    for hx, hy in houses:
        dist = min(abs(hx - sx) + abs(hy - sy) for sx, sy in comb)
        total += dist
        if total >= min_distance:  # 가지치기
            break
    min_distance = min(min_distance, total)

print(min_distance)