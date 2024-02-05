n, m = map(int, input().split())
board_input = []
li_paint = []

for i in range(n):
  board_input.append(input())

board_w = []
board_b = []
for i in range(4):
  board_w.append(['W','B','W','B','W','B','W','B'])
  board_w.append(['B','W','B','W','B','W','B','W'])
  board_b.append(['B','W','B','W','B','W','B','W'])
  board_b.append(['W','B','W','B','W','B','W','B'])
  
for i in range(m-7):
  for j in range(n-7):
    paint1 = 0
    paint2 = 0
    for k in range(j,j+8):
      for l in range(i,i+8):
        if board_input[k][l] != board_w[k-j][l-i]:
          paint1 += 1
        if board_input[k][l] != board_b[k-j][l-i]:
          paint2 += 1
    li_paint.append(min(paint1,paint2))
    
print(min(li_paint))