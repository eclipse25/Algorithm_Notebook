def solution(clothes):
    cl = {}
    for i in range(len(clothes)):
        cl[clothes[i][1]] = cl.get(clothes[i][1], 0) + 1
    
    answer = 1
    print(cl)
    for value in cl.values():
        answer *= (value + 1)
    print(answer, len(cl))
    answer -= 1
    
    return answer