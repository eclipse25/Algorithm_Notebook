import sys
n, c = map(int, sys.stdin.readline().split())
house = [int(sys.stdin.readline()) for _ in range(n)]
house.sort()

def max_distance(arr, target):
  start, end = 1, arr[-1] - arr[0]
  while start <= end:
    mid = (start + end) // 2

    count = 1
    last = arr[0]
    for i in range(1, len(arr)):
      if arr[i] - last >= mid:
        last = arr[i]
        count += 1
    if count >= target:
      start = mid + 1
    else:
      end = mid - 1
      
  return end

print(max_distance(house, c))