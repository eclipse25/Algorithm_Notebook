import sys
n, k = map(int, sys.stdin.readline().split())
level = [int(sys.stdin.readline()) for _ in range(n)]

def target_level(arr, k):
  start, end = min(arr), min(arr) + k

  while start <= end:
    mid = (start + end) // 2
    total_needed = sum(max(mid - x, 0) for x in arr)
    if total_needed > k:
      end = mid - 1
    else:
      start = mid + 1
  return end

print(target_level(level, k))