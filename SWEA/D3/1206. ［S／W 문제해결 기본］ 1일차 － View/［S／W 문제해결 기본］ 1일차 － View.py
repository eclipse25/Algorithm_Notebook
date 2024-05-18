for test_case in range(1, 11):
    n = int(input())
    height = list(map(int, input().split()))
    count = 0
    for i in range(2, n - 2):
        near = max(height[i - 2], height[i - 1], height[i + 1], height[i + 2])
        if height[i] > near:
            count += height[i] - near
    print(f"#{test_case} {count}")