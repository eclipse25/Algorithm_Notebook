def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(node):
        for neighbor in range(n):
            if computers[node][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                dfs(neighbor)
        
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)
    
    return answer