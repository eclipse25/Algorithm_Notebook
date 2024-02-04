import sys
n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

def binary_search(arr, target):
  start, end = 0, max(arr)
  
  while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in arr:
      if i > mid:
        sum += i - mid

    if sum >= target:
      start = mid + 1
    else:
      end = mid - 1
      
  return end

print(binary_search(trees, m))