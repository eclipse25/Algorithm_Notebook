def backtrack(n, m, numbers):
    if len(numbers) == m:
        print(' '.join(map(str, numbers)))
        return

    for i in range(1, n + 1):
        if len(numbers) == 0 or i >= numbers[-1]:
            numbers.append(i)
            backtrack(n, m, numbers)
            numbers.pop()

n, m = map(int,input().split())
numbers = []
backtrack(n, m, numbers)
