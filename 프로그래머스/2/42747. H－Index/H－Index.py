def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)
    
    for h in range(n, 0, -1):
        if citations[h - 1] >= h:
            return h
    return 0
