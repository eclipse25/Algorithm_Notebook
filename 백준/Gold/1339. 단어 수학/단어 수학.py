import sys

n = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(n)]

weights = [0] * 26
for word in words:
    p = 1
    for chr in reversed(word):
        weights[ord(chr) - 65] += p
        p *= 10

weights.sort(reverse=True)
num = 9
answer = 0
for weight in weights:
    answer += num * weight
    num -= 1
    if weight == 0:
        break

print(answer)