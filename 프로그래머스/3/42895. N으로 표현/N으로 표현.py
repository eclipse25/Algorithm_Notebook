def solution(N, number):
    dp = [0, [N]]
    
    if N == number:
        return 1
    
    for i in range(2, 9):
        answer = -1
        dp.append([])
        dp[i].append(int(str(N) * i))
        
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].append(x + y)
                    dp[i].append(x - y)
                    dp[i].append(x * y)
                    if y != 0:
                        dp[i].append(x // y)
            
        dp[i] = list(set(dp[i]))
        
        if dp[i] and number in dp[i]:
            answer = i
            break
            
    return answer