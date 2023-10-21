n, m = map(int, input().split())
sq = []


def backtracking(start):
    if len(sq) == m:
        print(' '.join(map(str, sq)))

    for i in range(start, n + 1):
        if i not in sq:
            sq.append(i)
            backtracking(i + 1)
            sq.pop()


backtracking(1)
