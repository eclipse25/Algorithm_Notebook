k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

def binary_search(arr, target):
  left, right = 1, max(arr)
  while left <= right:
    mid = (left + right) // 2

    count = 0
    for i in arr:
      count += i // mid

    if count < target:
      right = mid - 1
    else:
      left = mid + 1

  return right

print(binary_search(lines, n))