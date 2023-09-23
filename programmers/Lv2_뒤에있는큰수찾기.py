# stack 이용 -> "https://yinq.tistory.com/187" (본인 블로그 아님)
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for idx, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            answer[stack.pop()] = number
        stack.append(idx)

    return answer


# 시간초과 코드
def solution(numbers):
    answer = []
    for i in range(len(numbers) - 1):
        bn = -1
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[i]:
                bn = numbers[j]
                break
        answer.append(bn)
    answer.append(-1)
    return answer
