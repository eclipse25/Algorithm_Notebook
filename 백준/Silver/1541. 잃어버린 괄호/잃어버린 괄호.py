import sys

expression = sys.stdin.readline()[:-1]

numbers, operators = [], []
current_num = ''
for char in expression:
    if char.isdigit():
        current_num += char
    else:
        numbers.append(int(current_num))
        current_num = ''
        operators.append(char)
numbers.append(int(current_num))

min_val = numbers[0]
parentheses, temp = False, 0
for i in range(len(operators)):
    if not parentheses:
        if operators[i] == '+':
            min_val += numbers[i + 1]
        else:
            parentheses = True
            temp += numbers[i + 1]
    else:
        if operators[i] == '+':
            temp += numbers[i + 1]
        else:
            min_val -= temp
            temp = numbers[i + 1]
min_val -= temp
print(min_val)
