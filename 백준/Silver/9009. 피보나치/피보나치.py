import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    fb = [0, 1]
    while fb[-1] <= n:
        fb.append(fb[-2] + fb[-1])
    fb.pop()
    k = n
    result = []

    while k > 0:
        if fb[-1] > k:
            fb.pop()
        else:
            k -= fb[-1]
            result.append(fb[-1])
            fb.pop()
    
    print(" ".join(map(str,reversed(result))))