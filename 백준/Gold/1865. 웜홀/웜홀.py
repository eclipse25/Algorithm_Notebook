import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []

    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    # dist 초기화 (임의의 한 정점에서 시작 - 1번)
    dist = [10**9] * (n + 1)
    dist[1] = 0

    has_cycle = False

    # 벨만-포드 n-1번
    for _ in range(n - 1):
        for s, e, t in edges:
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t

    # n번째에 또 갱신되면 → 음수 사이클 존재
    for s, e, t in edges:
        if dist[e] > dist[s] + t:
            has_cycle = True
            break

    print("YES" if has_cycle else "NO")
