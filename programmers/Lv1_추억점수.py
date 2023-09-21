def solution(name, yearning, photo):

    answer = []

    for i in range(len(photo)):
        w = 0
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                w += yearning[name.index(photo[i][j])]
            else:
                continue
        answer.append(w)

    return answer
