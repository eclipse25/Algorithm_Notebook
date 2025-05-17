import sys

n, s = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
answer = 0

def dfs(index, current_sum, count):
    global answer
    if index == n:
        if current_sum == s and count > 0:
            answer += 1
        return
    
    dfs(index + 1, current_sum + numbers[index], count + 1)
    dfs(index + 1, current_sum, count)

dfs(0, 0, 0)
print(answer)