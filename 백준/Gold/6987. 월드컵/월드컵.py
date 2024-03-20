def backtrack(index, wins, draws, loses, matches):
  if index == len(matches):
    return True
  t1, t2 = matches[index]

  if wins[t1] > 0 and loses[t2] > 0:
    wins[t1] -= 1
    loses[t2] -= 1
    if backtrack(index + 1, wins, draws, loses, matches):
      return True
    else:
      wins[t1] += 1
      loses[t2] += 1
    
  if draws[t1] > 0 and draws[t2] > 0:
    draws[t1] -= 1
    draws[t2] -= 1
    if backtrack(index + 1, wins, draws, loses, matches):
      return True
    else:
      draws[t1] += 1
      draws[t2] += 1
      
  if loses[t1] > 0 and wins[t2] > 0:
    loses[t1] -= 1
    wins[t2] -= 1
    if backtrack(index + 1, wins, draws, loses, matches):
      return True
    else:
      loses[t1] += 1
      wins[t2] += 1
      
  return False


ans = [1, 1, 1, 1]

for n in range(4):
  res = [[0] * 3 for _ in range(6)]
  a = list(map(int, input().split()))

  if sum(a) != 30:
    ans[n] = 0
    continue

  wins = [a[i*3] for i in range(6)]
  draws = [a[i*3+1] for i in range(6)]
  loses = [a[i*3+2] for i in range(6)]
  
  matches = [(i, j) for i in range(6) for j in range(i+1, 6)]

  if not backtrack(0, wins, draws, loses, matches):
    ans[n] = 0

print(*ans)