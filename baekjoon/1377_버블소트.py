# 버블 소트에서 정렬이 완료될 때까지 돌아가는 pass(순회)의 수를 구하는 문제이다.
# 뒤에서 앞으로 이동하는 거리의 최댓값에 1을 더하면 답이 된다.
# 한 pass에서 한 원소가 왼쪽으로 이동할 수 있는 최대 거리가 한칸이기 때문이다.

import sys
n = int(sys.stdin.readline())
A = []
for i in range(n):
    A.append([int(sys.stdin.readline()), i])

A_sorted = sorted(A)
max_diff = 0
for i in range(len(A)):
    max_diff = max(max_diff, A_sorted[i][1] - i)
print(max_diff + 1)
