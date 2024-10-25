import sys

n = int(input())
fruits = list(map(int, sys.stdin.readline().split()))

left, right = 0, 0
max_count = 0
current = {}

while right < n:
    key= fruits[right]
    current[key] = current.get(key, 0) + 1

    if len(current) > 2:
        key = fruits[left]
        current[key] -= 1
        if current[key] <= 0:
            del current[key]
        left += 1

    max_count = max(max_count, sum(current.values()))
    right += 1

print(max_count)