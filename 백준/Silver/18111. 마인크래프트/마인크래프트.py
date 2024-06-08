import sys
from collections import Counter

n, m, b = map(int, sys.stdin.readline().split())
ground = []
for _ in range(n):
    heights = list(map(int, sys.stdin.readline().split()))
    for height in heights:
        ground.append(height)
counts = Counter(ground)

highest, lowest = max(ground), min(ground)
min_time = float('inf')
target_height = 0
for i in range(lowest, highest + 1):
    remove_count, add_count = 0, 0
    for height, count in counts.items():
        if height > i:
            remove_count += (height - i) * count
        elif height < i:
            add_count += (i - height) * count

    if add_count <= b + remove_count:
        time = 2 * remove_count + add_count
        if time <= min_time or (time == min_time and i > target_height):
            min_time = time
            target_height = i

print(min_time, target_height)