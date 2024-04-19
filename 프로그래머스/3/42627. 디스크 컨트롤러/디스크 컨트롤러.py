import heapq

def solution(jobs):
    n = len(jobs)
    current_time, total_time, i = 0, 0, 0  # i는 작업의 인덱스
    waiting = []
    
    jobs.sort()
    
    while i < n or waiting:
        while i < n and jobs[i][0] <= current_time:
            heapq.heappush(waiting, [jobs[i][1], jobs[i][0]])
            i += 1
        if waiting:
            job = heapq.heappop(waiting)
            current_time += job[0]
            total_time += current_time - job[1]
        else:
            current_time = jobs[i][0]

    answer = total_time // len(jobs)
    return answer