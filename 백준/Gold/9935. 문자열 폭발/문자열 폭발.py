import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

stack = []
l = len(b)

for chr in a:
    stack.append(chr)
    if len(stack) >= l and ''.join(stack[-l:]) == b:
        del stack[-l:]

if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack))