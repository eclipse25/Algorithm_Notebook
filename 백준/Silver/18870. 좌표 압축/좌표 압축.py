import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
numbers_sorted = sorted(set(numbers))

dic = {}
for i in range(len(numbers_sorted)):
    dic[numbers_sorted[i]] = i

for i in range(0, n - 1):
    print(dic[numbers[i]], end=' ')
print(dic[numbers[-1]])