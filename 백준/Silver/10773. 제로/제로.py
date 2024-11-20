import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    r = int(sys.stdin.readline())
    if r == 0:
        stack.pop()
    else:
        stack.append(r)

print(sum(stack))
