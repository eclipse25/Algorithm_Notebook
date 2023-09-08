def solution(n, m, section):

    start = section[0]
    answer = 1

    for i in range(1, len(section)):
        if section[i]-start+1 > m:
            answer += 1
            start = section[i]

    return answer
