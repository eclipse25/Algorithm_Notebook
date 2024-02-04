n = int(input())
for i in range(n):
  a, b = map(int,input().split())
  b_fac = 1
  a_fac = 1
  b_min_a_fac =1
  for j in range(1, b+1):
    b_fac *= j
  for j in range(1, a+1):
    a_fac *= j
  for j in range(1, b-a+1):
    b_min_a_fac *= j
  r = b_fac/(a_fac*b_min_a_fac)
  print(int(r))