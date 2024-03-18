s, n = map(int, input().split())
ln = len(str(n))
width = (s + 3) * ln
height = 2 * s + 3
pr = [[' '] * width for _ in range(height)]

for i in range(ln):
  for k in range(s):
    if str(n)[i] not in ['1', '4']:
      pr[0][(s + 3) * i + (k + 1)] = '-'

    if str(n)[i] not in ['1', '7', '0']:
      pr[s + 1][(s + 3) * i + (k + 1)] = '-'

    if str(n)[i] not in ['1', '4', '7']:
      pr[2 * s + 2][(s + 3) * i + (k + 1)] = '-'

    if str(n)[i] not in ['1', '2', '3', '7']:
      pr[k + 1][(s + 3) * i] = '|'

    if str(n)[i] in ['2', '6', '8', '0']:
      pr[s + 2 + k][(s + 3) * i] = '|'

    if str(n)[i] not in ['5', '6']:
      pr[k + 1][(s + 3) * i + s + 1] = '|'

    if str(n)[i] not in ['2']:
      pr[s + 2 + k][(s + 3) * i + s + 1] = '|'

for m in range(len(pr)):
  for n in range(len(pr[0])):
    print(pr[m][n], end='')
  print()