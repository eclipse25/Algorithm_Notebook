import sys

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

cnt = 0
for i in range(n):
    left, right = 0, n - 1
    target = numbers[i]

    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        sum2 = numbers[left] + numbers[right]
        if sum2 == target:
            cnt += 1
            break
        elif sum2 < target:
            left += 1
        else:
            right -= 1
        
print(cnt)