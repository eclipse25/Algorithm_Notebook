import sys

t = int(sys.stdin.readline())
for _ in range(t):
    clothes = {}
    n = int(sys.stdin.readline())
    for _ in range(n):
        name, category = sys.stdin.readline().split()
        clothes[category] = clothes.get(category, 0) + 1
    count = 1
    for value in clothes.values():
        count *= (value + 1)
    print(count - 1)
