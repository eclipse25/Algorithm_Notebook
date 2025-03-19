def solution(targets):
    targets.sort(key=lambda x: x[1], reverse=True)
    answer = 0
    
    while targets:
        answer += 1
        item = targets.pop()
        while targets:
            if targets[-1][0] < item[1]:
                targets.pop()
            else:
                break
        
    return answer