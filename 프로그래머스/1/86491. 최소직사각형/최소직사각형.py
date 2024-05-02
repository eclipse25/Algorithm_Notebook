def solution(sizes):
    sh, lg = 0, 0
    for a, b in sizes:
        sh = max(sh, min(a, b))
        lg = max(lg, max(a, b))
    answer = sh * lg
    return answer