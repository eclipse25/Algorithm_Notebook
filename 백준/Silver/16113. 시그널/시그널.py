n = int(input())
sig = input()
k = len(sig)//5
de = [sig[(n * k):(n * k) + k] for n in range(5)]

idx = []
blk = [1] * k

for i in range(k):
  flg = 0
  for j in range(5):
    if de[j][i] == '#':
      flg = 1
  if flg == 0:
    blk[i] = 0

for i in range(k):
  if i == 0 and blk[i] == 1 or blk[i - 1] == 0 and blk[i] == 1:
    idx.append(i)

for i in idx:
  if i == k - 1 or blk[i + 1] == 0:
    print(1, end='')
  elif de[0][i + 1] == '.':
    print(4, end='')
  elif de[2][i] == '.':
    print(7, end='')
  elif all(de[j][i + 1] == '.' for j in range(1, 4)):
    print(0, end='')
  elif all(de[j][i + 2] == '#' for j in range(1, 4)):
    if de[3][i] == '.' and de[1][i] == '.':
      print(3, end='')
    elif all(de[j][i] == '#' for j in range(1, 4)):
      print(8, end='')
    else:
      print(9, end='')
  else:
    if de[1][i + 2] == '#':
      print(2, end='')
    elif de[3][i] == '#':
      print(6, end='')
    else:
      print(5, end='')
print()