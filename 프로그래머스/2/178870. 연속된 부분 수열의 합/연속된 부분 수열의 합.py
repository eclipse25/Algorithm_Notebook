def solution(sequence, k):
    
    left, right = 0, 0
    s = sequence[0]
    answer = [0, len(sequence)]
    while right < len(sequence):
        if s == k:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            s -= sequence[left]
            left += 1
            
        if s < k:
            right += 1
            if right < len(sequence):
                s += sequence[right]
        if s > k:
            s -= sequence[left]
            left += 1
        
        if left > right:
            right += 1
            if right < len(sequence):
                s += sequence[right]
        
    
    
    return answer