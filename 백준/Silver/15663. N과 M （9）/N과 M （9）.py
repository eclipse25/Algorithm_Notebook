import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

numbers.sort()
seq = []
used = [False] * n

def backtrack():
    if len(seq) == m:
        print(' '.join(map(str, seq)))
        return
    
    prev = 0
    for i in range(n):
        if not used[i] and prev != numbers[i]:
            seq.append(numbers[i])
            used[i] = True
            backtrack()
            seq.pop()
            used[i] = False
            prev = numbers[i]

backtrack()