import sys

n, k = map(int, sys.stdin.readline().split())
scores = list(map(int, sys.stdin.readline().split()))
start, end = 0, sum(scores)

while start <= end:
    current_sum, group = 0, 0
    mid = (start + end) // 2
    for score in scores:
        current_sum += score
        if current_sum >= mid:
            current_sum = 0
            group += 1
    if group >= k:
        start = mid + 1
    else:
        end = mid - 1

print(end)