import sys


def max_hist_area(h):
    stack = []
    best = 0
    for i in range(len(h) + 1):
        cur = h[i] if i < len(h) else 0  # sentinel
        while stack and h[stack[-1]] > cur:
            height = h[stack.pop()]
            left = stack[-1] + 1 if stack else 0
            width = i - left
            best = max(best, height * width)
        stack.append(i)
    return best


while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0:
        break

    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    heights = [0] * m
    best = 0

    for i in range(n):
        for j in range(m):
            heights[j] = heights[j] + 1 if matrix[i][j] else 0
        best = max(best, max_hist_area(heights))

    print(best)
