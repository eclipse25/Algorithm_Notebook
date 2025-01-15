from collections import defaultdict

def solution(tickets):
    
    table = defaultdict(list)
    for a, b in tickets:
        table[a].append(b)
        
    for key in table.keys():
        table[key].sort(reverse=True)
    
    stack, path = ["ICN"], []
    while stack:
        while table[stack[-1]]:
            stack.append(table[stack[-1]].pop())
        path.append(stack.pop())
    
    answer = path[::-1]
    
    return answer