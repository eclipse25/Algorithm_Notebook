import sys
from itertools import combinations

input = sys.stdin.readline

# 입력 받기
n, k = map(int, input().split())
houses = [tuple(map(int, input().split())) for _ in range(n)]

# 결과값: 가능한 모든 조합 중 최소 최대 거리
min_max_distance = float('inf')

# 가능한 모든 K개의 대피소 조합 탐색
for shelters in combinations(houses, k):
    max_distance = 0
    for hx, hy in houses:
        # 현재 집에서 가장 가까운 대피소까지 거리 계산
        min_distance = float('inf')
        for sx, sy in shelters:
            distance = abs(hx - sx) + abs(hy - sy)
            min_distance = min(min_distance, distance)
        # 이 집에서 가장 가까운 대피소까지의 거리 중 최댓값 갱신
        max_distance = max(max_distance, min_distance)

    # 조합 중 최솟값 갱신
    min_max_distance = min(min_max_distance, max_distance)

print(min_max_distance)
