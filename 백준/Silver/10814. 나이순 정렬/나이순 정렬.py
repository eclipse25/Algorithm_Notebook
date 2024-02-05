n = int(input())
members = []
for i in range(n):
  a, b = input().split()
  members.append([int(a),b])
members.sort(key = lambda x: x[0])
for i in range(n):
  print(members[i][0],members[i][1])