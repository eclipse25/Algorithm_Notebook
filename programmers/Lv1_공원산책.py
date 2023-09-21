def solution(park, routes):

    row = len(park[0])  # park 가로길이
    col = len(park)  # park 세로길이
    obs = []  # 장애물위치 리스트

    for i in range(col):
        for j in range(row):
            if park[i][j] == 'S':  # 초기 S위치
                lc = i
                lr = j
            elif park[i][j] == 'X':  # 장애물 위치
                obs.append([i, j])

    n = len(routes)

    for i in range(n):
        a, b = routes[i].split()
        b = int(b)
        if a == 'E':
            if 0 <= lr+b <= row-1:
                br = 0
                for j in range(lr+1, lr+b+1):
                    if [lc, j] in obs:
                        br = 1
                if br == 1:
                    continue
                lr += b
        elif a == 'W':
            if 0 <= lr-b <= row-1:
                br = 0
                for j in range(lr-b, lr):
                    if [lc, j] in obs:
                        br = 1
                if br == 1:
                    continue
                lr -= b
        elif a == 'N':
            if 0 <= lc-b <= col-1:
                br = 0
                for j in range(lc-b, lc):
                    if [j, lr] in obs:
                        br = 1
                if br == 1:
                    continue
                lc -= b
        else:
            if 0 <= lc+b <= col-1:
                br = 0
                for j in range(lc+1, lc+b+1):
                    if [j, lr] in obs:
                        br = 1
                if br == 1:
                    continue
                lc += b

    answer = []
    answer.append(lc)
    answer.append(lr)

    return answer
