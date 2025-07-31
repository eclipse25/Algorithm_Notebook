import sys

a, b, c = map(int, sys.stdin.readline().split())


def mod_pow(a, b, c):
    if b == 1:
        return a % c
    half = mod_pow(a, b // 2, c)
    if b % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c


print(mod_pow(a, b, c))
