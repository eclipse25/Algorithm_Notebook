import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

numbers.sort()

def backtrack(index, current):
    if len(current) == m:
        print(' '.join(map(str, current)))
        return

    for i in range(index, n):
        if i > index and numbers[i] == numbers[i - 1]:
            continue
        current.append(numbers[i])
        backtrack(i, current)
        current.pop()

backtrack(0, [])
