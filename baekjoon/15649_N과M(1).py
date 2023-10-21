n, m = map(int, input().split())
sq = []


def backtracking():
    if len(sq) == m:
        print(' '.join(map(str, sq)))

    for i in range(1, n + 1):
        if i not in sq:
            sq.append(i)
            backtracking()
            sq.pop()


backtracking()
