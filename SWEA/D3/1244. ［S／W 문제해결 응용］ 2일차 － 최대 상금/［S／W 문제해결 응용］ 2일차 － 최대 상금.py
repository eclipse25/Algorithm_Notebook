def backtrack(numbers, swap_count, ideal, memo, max_num):
    state = (tuple(numbers), swap_count)  # 가변 객체는 딕셔너리의 key로 사용불가
    if state in memo:
        return memo[state]

    if swap_count == 0:
        return int(''.join(numbers))

    if ''.join(numbers) == ideal:
        if swap_count % 2 == 0:
            max_num = max(max_num, int(''.join(numbers)))
            memo[state] = max_num
        else:
            if len(set(numbers)) == len(numbers):  # 중복된 숫자가 없는 경우
                # 마지막 두 자리를 교환
                numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
                max_num = max(max_num, int(''.join(numbers)))
                numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
            else:
                max_num = max(max_num, int(''.join(numbers)))
            memo[state] = max_num
        return max_num

    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            max_num = max(max_num, backtrack(numbers, swap_count - 1, ideal, memo, max_num))
            numbers[i], numbers[j] = numbers[j], numbers[i]

    memo[state] = max_num
    return max_num


T = int(input())
for test_case in range(1, T + 1):
    numbers, swap_count = input().split()
    numbers = list(numbers)
    swap_count = int(swap_count)
    ideal = ''.join(sorted(numbers, reverse=True))
    memo = {}
    max_num = backtrack(numbers, swap_count, ideal, memo, 0)
    print(f"#{test_case} {max_num}")