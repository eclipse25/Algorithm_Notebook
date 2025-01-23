def solution(number, k):
    answer = ''
    stack = []
    for num in number:
        while stack and k > 0 and int(num) > int(stack[-1]):
            stack.pop()
            k -= 1
        stack.append(num)
        
    for _ in range(k):
        stack.pop()
        
    answer = "".join(stack)
    return answer