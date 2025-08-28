import sys


def factorials(n: int):
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i
    return fact


n = int(sys.stdin.readline())
query = list(map(int, sys.stdin.readline().split()))
mode = query[0]

if mode == 1:
    k = query[1] - 1
    fact = factorials(n)
    available = list(range(1, n + 1))
    result = []
    for i in range(n, 0, -1):
        block = fact[i - 1]
        idx = k // block
        k %= block
        result.append(available.pop(idx))
    print(" ".join(list(map(str, result))))
else:
    fact = factorials(n)
    available = list(range(1, n + 1))
    rank0 = 0
    for i, x in enumerate(query[1:]):
        idx = available.index(x)
        rank0 += idx * fact[n - 1 - i]
        available.pop(idx)
    print(rank0 + 1)
