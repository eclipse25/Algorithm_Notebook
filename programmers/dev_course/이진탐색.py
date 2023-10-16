def solution(L, x):
    
    def binsearch(L, x, lower, upper):
        if lower > upper:
            return -1
        
        mid = (lower + upper) // 2
        if x == L[mid]:
            return mid
        elif x > L[mid]:
            return binsearch(L, x, mid + 1, upper)
        else:
            return binsearch(L, x, lower, mid - 1)
    
    answer = binsearch(L, x, 0, len(L) - 1)
    
    return answer