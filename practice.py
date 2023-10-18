import sys
import heapq

n = int(sys.stdin.readline().rstrip())
cards = []
heapq.heapify(cards)
result = 0


for i in range(n): # [10, 20, 40]
    card = int(sys.stdin.readline().rstrip())
    heapq.heappush(cards,card)

flag = False
while len(cards) != 1:
    mixing = 0
    if not flag:
        for j in range(2):
            a = heapq.heappop(cards)
            mixing += a
        flag = True
    else:
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
        mixing += (a+b)
    
    result += mixing
    heapq.heappush(cards, mixing)
        




print(result)





