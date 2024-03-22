from collections import deque

def solution(progresses, speeds):
    answer = []
    
    pr = deque(progresses)
    sp = deque(speeds)
    
    while(pr):
        for i in range(len(pr)):
            pr[i] += sp[i]
        
        count = 0
        
        while(pr and pr[0] >= 100):
            pr.popleft()
            sp.popleft()
            count += 1
            
        if count != 0:
            answer.append(count)
            
    return answer