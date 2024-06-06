import sys

n, m = map(int, sys.stdin.readline().split())
memo = {}
for i in range(n):
    site, password = sys.stdin.readline().split()
    memo[site] = password

for _ in range(m):
    site = sys.stdin.readline().rstrip()
    print(memo[site])