def solution(s):
    answer = False
    stack = []
    
    for str in s:
        if str == "(":
            stack.append(str)
        elif len(stack) > 0 and str == ")":
            stack.pop()
        elif len(stack) == 0 and str == ")":
            return False
    
    if len(stack) == 0:
        answer = True
    
    
    return answer