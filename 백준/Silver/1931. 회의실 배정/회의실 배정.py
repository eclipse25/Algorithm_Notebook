import sys

n = int(sys.stdin.readline())
schedule = []
for _ in range(n):
    schedule.append(list(map(int, sys.stdin.readline().split())))

schedule.sort(key=lambda x: (x[1], x[0]))
count, end = 0, 0
for i in range(n):
    if schedule[i][0] >= end:
        count += 1
        end = schedule[i][1]

print(count)