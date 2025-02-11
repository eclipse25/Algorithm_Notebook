from collections import defaultdict, deque

def solution(n, wires):
    answer = n
    conn = defaultdict(list)
    for wire in wires:
        conn[wire[0]].append(wire[1])
        conn[wire[1]].append(wire[0])
    
    for v1, v2 in wires:
        visited = [False] * (n + 1)
        visited[v1] = True
        queue = deque([v1])
        while queue:
            node = queue.popleft()
            for neighbor in conn[node]:
                if not visited[neighbor] and neighbor != v2:
                    visited[neighbor] = True
                    queue.append(neighbor)
        conn1 = sum(visited)
        conn2 = n - conn1
        answer = min(answer, abs(conn1 - conn2))
        
    return answer