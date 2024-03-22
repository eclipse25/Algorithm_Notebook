import heapq

def solution(operations):
    process = []
    heapq.heapify(process)
    
    for i in range(len(operations)):
        if operations[i][0] == 'I':
            num = int(list(operations[i].split())[1])
            heapq.heappush(process, num)
        else:
            if operations[i] == 'D 1' and process:
                max_heap = [-n for n in process]
                heapq.heapify(max_heap)
                heapq.heappop(max_heap)
                process = [-n for n in max_heap]
                heapq.heapify(process)
            
            elif process:
                heapq.heappop(process)
    
    if len(process) == 0:
        minv, maxv = 0, 0
    else:
        minv = process[0]
        maxv = max(process)
        
    answer = [maxv, minv]
    return answer