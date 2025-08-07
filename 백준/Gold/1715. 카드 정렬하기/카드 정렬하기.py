import sys
import heapq

n = int(sys.stdin.readline())
cards = []
for _ in range(n):
    cards.append(int(sys.stdin.readline()))

heapq.heapify(cards)
count = 0
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    heapq.heappush(cards, a + b)
    count += a + b

print(count)