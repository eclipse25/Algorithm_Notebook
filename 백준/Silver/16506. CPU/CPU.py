import sys
t = int(sys.stdin.readline())

for _ in range(t):
  ascode = list(sys.stdin.readline().split())
  mccode = [0] * 16
  opcode, rD, rA, rB = ascode[0], ascode[1], ascode[2], ascode[3]

  if opcode[0:3] == "SUB":
    mccode[0:4] = "0001"
  elif opcode[0:3] == "MOV":
    mccode[0:4] = "0010"
  elif opcode[0:3] == "AND":
    mccode[0:4] = "0011"
  elif opcode[0:2] == "OR":
    mccode[0:4] = "0100"
  elif opcode[0:3] == "NOT":
    mccode[0:4] = "0101"
  elif opcode[0:4] == "MULT":
    mccode[0:4] = "0110"
  elif opcode[0:5] == "LSFTL":
    mccode[0:4] = "0111"
  elif opcode[0:5] == "LSFTR":
    mccode[0:4] = "1000"
  elif opcode[0:5] == "ASFTR":
    mccode[0:4] = "1001"
  elif opcode[0:2] == "RL":
    mccode[0:4] = "1010"
  elif opcode[0:2] == "RR":
    mccode[0:4] = "1011"
  
  if opcode[-1] == "C":
    mccode[4] = "1"
    mccode[12:] = bin(int(rB))[2:].zfill(4)
  else:
    mccode[12:15] = bin(int(rB))[2:].zfill(3)

  mccode[6:9] = bin(int(rD))[2:].zfill(3)
  mccode[9:12] = bin(int(rA))[2:].zfill(3)
  
  for i in range(len(mccode)):
    print(mccode[i], end='')
  print()