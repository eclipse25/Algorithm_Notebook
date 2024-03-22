def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        sliced = array[commands[i][0] - 1:commands[i][1]]
        sliced.sort()
        answer.append(sliced[commands[i][2] - 1])
    return answer