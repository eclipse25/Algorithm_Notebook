def solution(prices):
    answer = [0] * len(prices)
    stack = [0]
    time = {}
    
    if len(prices) == 1:
        return [0]
    
    for i in range(1, len(prices)):
        for index in stack:
            time[index] = time.get(index, 0) + 1
            
        while stack:
            if prices[i] >= prices[stack[-1]]:
                break
            else:
                stack.pop()
        stack.append(i)
                
    for key, value in time.items():
        answer[key] = value
            
    return answer