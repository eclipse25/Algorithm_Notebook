def solution(players, callings):
    pton = {}
    ntop = {}
    answer = []

    for i in range(len(players)):
        pton[players[i]] = i
        ntop[i] = players[i]

    for i in range(len(callings)):
        a = pton[callings[i]]  # a는 불린사람 기존등수
        b = ntop[a-1]  # b는 기존등수 앞에 있던 사람
        ntop[a-1] = callings[i]  # 기존등수-1로 불린사람 옮김
        ntop[a] = b  # 기존등수로 앞에있던 사람 옮김
        pton[b] = a
        pton[callings[i]] = a-1

    for i in range(len(players)):
        answer.append(ntop[i])

    return answer
