def solution(citations):
    citations.sort(reverse = True)
    n = len(citations)
    h = min(citations[0], n)
    
    while h >= 0:
        if citations[h - 1] >= h:
            return h
        else:
            h -= 1
            
    return 0