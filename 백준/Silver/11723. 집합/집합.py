import sys

m = int(sys.stdin.readline())
s = set()
for _ in range(m):
    line = sys.stdin.readline().rstrip()
    if line in ['all', 'empty']:
        if line == 'all':
            s = {i for i in range(1, 21)}
        else:
            s = set()
    else:
        command, num = line.split()
        x = int(num)
        if command == 'add':
            s.add(x)
        elif command == 'remove':
            s.discard(x)
        elif command == 'check':
            print(1) if x in s else print(0)
        else:
            s.add(x) if x not in s else s.remove(x)