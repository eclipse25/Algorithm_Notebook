import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())
truth = list(map(int, input().split()))
truth = truth[1:]

# 사람 간의 연결 그래프 (같은 파티에 있는 사람들끼리 연결)
adj = defaultdict(list)
parties = []  # 파티별 참가자 목록 저장

for _ in range(m):
    data = list(map(int, input().split()))
    party = data[1:]
    parties.append(party)

    # 같은 파티에 있는 사람들끼리 양방향 연결
    for i in range(len(party)):
        for j in range(i + 1, len(party)):
            a, b = party[i], party[j]
            adj[a].append(b)
            adj[b].append(a)

# 진실을 아는 사람들을 시작으로 BFS 탐색해서 전파
visited = [False] * (n + 1)

queue = deque()
for person in truth:
    visited[person] = True
    queue.append(person)

while queue:
    current = queue.popleft()
    for neighbor in adj[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)

# 각 파티에 대해 진실 아는 사람 없는 파티만 카운트
answer = 0
for party in parties:
    if all(not visited[person] for person in party):
        answer += 1

print(answer)
