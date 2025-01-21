from collections import defaultdict
from collections import deque

def connected(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    if count == 1:
        return True
    return False

def solution(begin, target, words):
    if target not in words:
        return 0
    
    words = words + [begin]
    graph = defaultdict(list)
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if connected(words[i], words[j]):
                graph[words[i]].append(words[j])
                graph[words[j]].append(words[i])
                
    visited = { word: False for word in words}
    visited[begin] = True

    answer = 0
    queue = deque([begin])
    
    while queue:
        answer += 1
        new_queue = []
        while queue:
            word = queue.popleft()
            for neighbor in graph[word]:
                if not visited[neighbor]:
                    if neighbor == target:
                        return answer
                    visited[neighbor] = True
                    new_queue.append(neighbor)
        queue = deque(new_queue)
    
    return 0