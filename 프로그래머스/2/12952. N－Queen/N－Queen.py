def backtrack(board, current_row, answer):
    if current_row == len(board):
        answer[0] += 1
        return
    
    for i in range(len(board)):
        board[current_row] = i
        is_valid = True
        for pre in range(current_row):
            if board[pre] == board[current_row] or \
            abs(board[pre] - board[current_row]) == current_row - pre:
                is_valid = False
                break
                
        if is_valid == True:
            backtrack(board, current_row + 1, answer)
                

def solution(n):
    board = [-1] * n  # 퀸은 무조건 다른 행에 존재하므로 1차원으로 표현 가능
    answer = [0]
    backtrack(board, 0, answer)
    return answer[0]