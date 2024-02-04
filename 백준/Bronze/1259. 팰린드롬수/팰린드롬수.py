while(True):
  n = input()
  if n == '0': break
  ispal = 1
  for i in range(len(n)):
    if n[i] != n[len(n)-1-i]:
      ispal = 0
  print('yes' if ispal == 1 else 'no')