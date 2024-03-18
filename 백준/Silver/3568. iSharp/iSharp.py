import sys
i = list(sys.stdin.readline().replace(";","").split())

for j in range(1, len(i)):
  i[j] = i[j].replace(",", "")

  op = len(i[j])
  for n in range(0, len(i[j])):
    if i[j][n] in ['[','*','&']:
      op = n
      break

  pr = i[0]
  addt = i[j][op:][::-1]
  while(addt):
    
    if addt[0] == ']':
      pr = pr + "[]"
      addt = addt[2:]
    else:
      pr = pr + addt[0]
      addt = addt[1:]
    
  pr += f" {i[j][:op]};"
  
  print(pr)
