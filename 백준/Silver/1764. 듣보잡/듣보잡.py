import sys

n, m = map(int, sys.stdin.readline().split())

dic = {}
count, name_list = 0, []
for _ in range(n + m):
    name = sys.stdin.readline()[:-1]
    dic[name] = dic.get(name, 0) + 1
    if dic[name] == 2:
        count += 1
        name_list.append(name)

name_list.sort()
print(count)
for i in range(len(name_list)):
    print(name_list[i])