# 이분(이진) 탐색, 매개변수 탐색
# 특정한 개수를 만족하면서 최대한 긴 길이로 잘리도록 하는 랜선의 길이를 찾는다.

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
