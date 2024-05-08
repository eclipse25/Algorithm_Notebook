from itertools import permutations
def solution(k, dungeons):
    n = len(dungeons)
    order = [i for i in range(n)]
    perms = permutations(order, n)
    answer = 0
    
    for perm in perms:
        left_k = k
        count = 0
        for i in range(len(perm)):
            if left_k >= dungeons[perm[i]][0]:
                count += 1
                left_k -= dungeons[perm[i]][1]
        if count > answer:
            answer = count
    
    return answer