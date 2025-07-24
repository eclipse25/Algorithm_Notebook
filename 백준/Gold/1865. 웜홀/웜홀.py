import sys

tc = int(sys.stdin.readline())

for case_num in range(tc):
    n, m, w = map(int, sys.stdin.readline().split())
    edges = []

    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, sys.stdin.readline().split())
        edges.append((s, e, -t))

    for i in range(1, n + 1):
        edges.append((0, i, 0))  # 가상 노드 0번 → 모든 노드

    dist = [float("inf")] * (n + 1)
    dist[0] = 0
    has_cycle = False

    for i in range(n + 1):
        updated = False
        for s, e, t in edges:
            if dist[s] != float("inf") and dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                updated = True
        if not updated:
            break
        if updated and i == n:
            has_cycle = True

    print("YES" if has_cycle else "NO")
