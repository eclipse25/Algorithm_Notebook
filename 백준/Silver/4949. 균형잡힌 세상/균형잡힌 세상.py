while(True):
  str = input()
  if str == '.':
    break
  stack = []
  printed = 0
  for i in range(len(str)):
    if str[i] == '[' or str[i] == '(':
      stack.append(str[i])
    if str[i] == ']' or str[i] == ')':
      if len(stack) == 0:
        print('no')
        printed = 1
        break
      if str[i] == ']':
        if stack[-1] == '[':
            stack.pop()
        else:
          print('no')
          printed = 1
          break
      else:
        if stack[-1] == '(':
            stack.pop()
        else: 
          print('no')
          printed = 1
          break
  if printed == 1:
    continue
  elif len(stack) == 0:
    print('yes')
  else:
    print('no')