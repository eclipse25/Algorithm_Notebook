def backtrack(current_op, numbers, operators):
    k = len(numbers)
    if current_op == k - 1:
        val[1] = max(val[0], val[1])
        val[2] = min(val[0], val[2])
        return

    # n-1개 연산자 대입
    for i in range(4):
        if operators[i] == 0:
            continue
        operators[i] -= 1
        temp = val[0]
        if i == 0:
            val[0] += numbers[current_op + 1]
        elif i == 1:
            val[0] -= numbers[current_op + 1]
        elif i == 2:
            val[0] *= numbers[current_op + 1]
        else:
            if numbers[current_op + 1] != 0:
                if val[0] < 0:
                    val[0] = -(-val[0] // numbers[current_op + 1])
                else:
                    val[0] //= numbers[current_op + 1]
        backtrack(current_op + 1, numbers, operators)
        val[0] = temp
        operators[i] += 1

n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
val = [numbers[0], -1000000000, 1000000000]  # current, max, min
backtrack(0, numbers, operators)
print(val[1])
print(val[2])