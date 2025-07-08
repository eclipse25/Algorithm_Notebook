import sys

h, w = map(int, sys.stdin.readline().split())
blocks = list(map(int, sys.stdin.readline().split()))

left_max = [0] * w
right_max = [0] * w

left_max[0] = blocks[0]
for i in range(1, w):
    left_max[i] = max(left_max[i - 1], blocks[i])

right_max[-1] = blocks[-1]
for i in range(w - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], blocks[i])

answer = 0
for i in range(w):
    answer += min(left_max[i], right_max[i]) - blocks[i]

print(answer)
