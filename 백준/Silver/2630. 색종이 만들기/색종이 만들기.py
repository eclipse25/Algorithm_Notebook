import sys


def fractal(paper):
    global blue, white
    if len(paper) == 1:
        if paper[0][0] == 1:
            blue += 1
        else:
            white += 1
        return
    if all(num == 1 for row in paper for num in row):
        blue += 1
        return
    if all(num == 0 for row in paper for num in row):
        white += 1
        return

    new_n = len(paper) // 2
    new_papers = []
    for option in [0, new_n]:
        half_paper = paper[0 + option:new_n + option]
        for option2 in [0, new_n]:
            new_paper = []
            for i in range(len(half_paper)):
                new_paper.append(half_paper[i][0 + option2:new_n + option2])
            new_papers.append(new_paper)
    for new_paper in new_papers:
        fractal(new_paper)


n = int(sys.stdin.readline())
paper = []
for i in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))
blue, white = 0, 0
fractal(paper)
print(white)
print(blue)
