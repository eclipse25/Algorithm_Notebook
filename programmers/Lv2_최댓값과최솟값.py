# Lv2라고 되어있지만 사실상 Lv0으로 추정
def solution(s):
    answer = ''
    li = list(map(int, s.split()))
    x = max(li)
    n = min(li)
    answer = f"{n} {x}"       # answer = str(n) + ' ' +str(x)
    return answer
