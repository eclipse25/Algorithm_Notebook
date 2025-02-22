def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    cnt = 0
    for l in lost_set:
        if l - 1 in reserve_set:
            reserve_set.remove(l - 1)
        elif l + 1 in reserve_set:
            reserve_set.remove(l + 1)
        else:
            cnt += 1
    
    answer = n - cnt
    return answer