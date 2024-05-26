import sys

def backtrack(n, current_row, cols, used_cols, answer):
    def is_valid(row, col):
        for r in range(row):
            if cols[r] == col or abs(cols[r] - col) == abs(r - row):
                return False
        return True

    if current_row == n:
        answer[0] += 1
        return

    for col in range(n):
        if col in used_cols:
            continue
        if is_valid(current_row, col):
            cols[current_row] = col
            used_cols.add(col)
            backtrack(n, current_row + 1, cols, used_cols, answer)
            used_cols.remove(col)

n = int(sys.stdin.readline())
cols = [-1] * n
used_cols = set()
answer = [0]
backtrack(n, 0, cols, used_cols, answer)
print(answer[0])