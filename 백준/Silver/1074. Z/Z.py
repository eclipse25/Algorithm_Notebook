import sys

n, r, c = map(int, sys.stdin.readline().split())

def order(val, r, c, n):
    new_n = 2 ** (n - 1)
    if n == 0:
        return val
    rv = True if r >= new_n else False
    cv = True if c >= new_n else False

    if not rv and cv:
        val += 4 ** (n - 1)
    elif rv and not cv:
        val += 4 ** (n - 1) * 2
    elif rv and cv:
        val += 4 ** (n - 1) * 3

    return order(val, r % new_n, c % new_n, n - 1)

print(order(0, r, c, n))