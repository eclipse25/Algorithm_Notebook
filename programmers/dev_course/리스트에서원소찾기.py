def solution(L, x):
    answer = []
    for i in range(len(L)):
        if x == L[i]:
            answer.append(i)
    if len(answer) == 0:
        answer = [-1]
    return answer