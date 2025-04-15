import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

inf = float('inf')
dist = [[inf] * (n + 1) for _ in range(n + 1)]

# 시작과 도착 노드가 같은 경우
for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    dist[start][end] = min(dist[start][end], cost)

# 플로이드 워셜: k > i > j 순서가 지켜져야 한다.
for k in range(1, n + 1):     #중간 노드
    for i in range(1, n + 1):    #시작 노드
        for j in range(1, n + 1):    #도착 노드
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(0 if dist[i][j] == inf else dist[i][j], end=' ')
    print()