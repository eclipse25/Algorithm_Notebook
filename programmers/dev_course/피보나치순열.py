def solution(x):
    answer = 0
    def fib(n):
        if n <= 1:
            return n
        else:
            return fib(n-2) + fib(n-1)
    answer = fib(x)
    return answer