n = int(input())
str = []
for i in range(n):
  str.append(input())
  
str = list(set(str))
str.sort()
str.sort(key=lambda x: (len(x), x))
      
for i in range(len(str)):
  print(str[i])