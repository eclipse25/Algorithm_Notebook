import sys
from itertools import permutations


k = int(sys.stdin.readline())
operators = list(sys.stdin.readline().split())
cases = []


def add_case(numbers):
    for i, operator in enumerate(operators):
        if operator == ">":
            if numbers[i] < numbers[i + 1]:
                return
        else:
            if numbers[i] > numbers[i + 1]:
                return
    cases.append("".join(map(str, numbers)))


for comb in list(permutations(range(0, 10), k + 1)):
    add_case(comb)

cases.sort()
print(cases[-1])
print(cases[0])
