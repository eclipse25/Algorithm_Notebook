def solution(answers):
    w1 = [1, 2, 3, 4, 5]
    w2 = [2, 1, 2, 3, 2, 4, 2, 5]
    w3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    correct_counts = [0, 0, 0]
    
    for i in range(len(answers)):
        asr = answers[i]
        if asr == w1[i % 5]:
            correct_counts[0] += 1
        if asr == w2[i % 8]:
            correct_counts[1] += 1
        if asr == w3[i % 10]:
            correct_counts[2] += 1
    
    max_count = max(correct_counts)
    answer = []
    for i in range(len(correct_counts)):
        if correct_counts[i] == max_count:
            answer.append(i + 1)
    return answer