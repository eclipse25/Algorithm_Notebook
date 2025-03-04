def solution(n, times):
    left, right = 0, n * max(times)
    
    while left <= right:
        mid = (left + right) // 2
        # 그 시간(mid) 안에 심사 가능한 최대 인원 구하기
        max_people = sum(mid // time for time in times)
        if max_people >= n:
            right = mid - 1
        else:
            left = mid + 1

    return left