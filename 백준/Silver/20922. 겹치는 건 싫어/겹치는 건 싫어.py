import sys

n, k = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

left, right = 0, 0
count = {}
answer = 0
while left < n and right < n:
    rv = numbers[right]

    if count.get(rv, 0) < k:
        count[rv] = count.get(rv, 0) + 1
        right += 1
        answer = max(answer, right - left)
    else:
        lv = numbers[left]
        count[lv] -= 1
        left += 1

print(answer)
