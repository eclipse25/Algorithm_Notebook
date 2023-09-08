def solution(wallpaper):
    row = len(wallpaper[0])
    column = len(wallpaper)
    print(row, column)
    li_y, li_x = [], []

    for j in range(column):
        for i in range(row):
            if wallpaper[j][i] == '#':
                li_y.append(j)
                li_x.append(i)

    answer = []
    answer.append(min(li_y))
    answer.append(min(li_x))
    answer.append(max(li_y)+1)
    answer.append(max(li_x)+1)

    return answer
