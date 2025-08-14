import sys

n, k = map(int, sys.stdin.readline().split())
time = []
for i in range(n):
    time.append(list(map(int, sys.stdin.readline().split())))

# 플로이드-워셜 -> 모든 노드 간의 최적 시간 계산 - n^3
for mid in range(n):  # 중간 노드
    for i in range(n):  # 출발 노드
        for j in range(n):  # 도착 노드
            time[i][j] = min(time[i][j], time[i][mid] + time[mid][j])

dp = [[-1] * n for _ in range(1 << n)]


# 경로 탐색
def dfs_mask(mask, node):
    # 모든 노드 방문
    if mask == (1 << n) - 1:
        return 0

    if dp[mask][node] != -1:
        return dp[mask][node]

    answer = float("inf")
    for i in range(n):
        # 방문하지 않은 노드인 경우
        if not (mask & (1 << i)):
            answer = min(answer, time[node][i] + dfs_mask(mask | (1 << i), i))

    dp[mask][node] = answer
    return answer


print(dfs_mask(1 << k, k))
