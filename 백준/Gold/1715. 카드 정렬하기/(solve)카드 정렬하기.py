import sys
import heapq

n = int(sys.stdin.readline().rstrip())  # 입력에서 카드의 개수를 읽어옵니다.
cards = []  # 카드를 저장할 리스트
heapq.heapify(cards)  # cards 리스트를 최소 힙으로 만듭니다.
result = 0  # 결과 변수 (카드 섞는데 필요한 비용의 총합을 저장)

for i in range(n):
    card = int(sys.stdin.readline().rstrip())  # 카드의 가격을 읽어옵니다.
    heapq.heappush(cards, card)  # 카드의 가격을 최소 힙에 추가합니다.

flag = False  # 카드를 섞을 때 사용할 플래그 변수
while len(cards) != 1:
    mixing = 0  # 현재 섞인 카드의 가격을 저장할 변수
    if not flag:
        for j in range(2):
            a = heapq.heappop(cards)  # 가장 가격이 낮은 카드 2장을 꺼냅니다.
            mixing += a  # 두 장의 카드를 섞은 가격을 누적합니다.
        flag = True  # 플래그를 True로 설정하여 다음 루프에서 1장의 카드를 꺼내야 합니다.
    else:
        a = heapq.heappop(cards)  # 가장 가격이 낮은 카드 1장을 꺼냅니다.
        b = heapq.heappop(cards)  # 가장 가격이 낮은 카드 1장을 또 꺼냅니다.
        mixing += (a + b)  # 두 장의 카드를 섞은 가격을 누적합니다.
    
    result += mixing  # 섞은 카드의 가격을 결과에 더합니다.
    heapq.heappush(cards, mixing)  # 섞은 카드의 가격을 최소 힙에 추가합니다.

# 결과 출력: 모든 카드를 섞고 남은 한 장의 카드의 가격
print(result)