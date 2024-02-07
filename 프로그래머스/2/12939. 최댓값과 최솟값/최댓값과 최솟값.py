def solution(s):
    answer = ''
    li = list(map(int, s.split()))
    x = max(li)
    n = min(li)
    answer = f"{n} {x}"
    return answer