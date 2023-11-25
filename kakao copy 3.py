# 1~n 사이 수의 카드 동전 coin개

# 1. 카드 n / 3장 가지기
# 2. 1라운드 부터 시작, 각 라운드 시작 할때 카드 2장 뽑기, if len(카드 뭉치) == 0: 게임 종료, 뽑은 카드는 카드 한장 당 동전 하나 소모해서 가지거나,동전을 소모하지 않고 버리기
# 3. 카드에 적힌 수의 합 == n+1이 되도록 카드 2장을 내고 다음 라운드 진행 가능, if 카드 두장 못내면 : 게임 종료

def make_need_card_lst(my_hand, target):
    need_cards_lst = []
    for i in my_hand:
        need_cards_lst.append(target - i)
    
    return need_cards_lst

def make_target(my_cards,target):
    my_cards.sort()
    need_1 = 0
    need_2 = 0
    left = 0
    right = len(my_cards) - 1 
    while left < right:
        if my_cards[left] + my_cards[right] > target:
            right += 1
        elif my_cards[left] + my_cards[right] < target:
            left += 1
        elif my_cards[left] + my_cards[right] == target:
            flag = True
            need_1, need_2 = my_cards[left], my_cards[right]
            return flag, need_1, need_2
    flag = False
    return flag, need_1, need_2
     
    

coin = 4
cards = [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]
n = len(cards)

hand = [] # 내 손패 [3, 6, 7, 2]

for i in range(n//3):
    card = cards.pop(0)
    hand.append(card)

# cards : [1, 10, 5, 9, 8, 12, 11, 4]

target = n + 1 # 13

round = 0

while len(cards) > 0:
    round += 1
    
    # 카드 뽑기
    new_cards = []
    for i in range(2):
        card = cards.pop(0)
        new_cards.append(card)
    
    need_card_lst = make_need_card_lst(hand, target)
    
    # 현재 손패로 타겟값 만들 수 있는지 검사
    flag, need_card_1, need_card_2 = make_target(hand,target)
    
    # 만들 수 있으면 코인 안쓰고 카드 버리기
    if flag:
        hand.remove(need_card_1)
        hand.remove(need_card_2)
        
        for new_card in new_cards:
            if new_card in need_card_lst:
                hand.append(new_card)
                coin -= 1
    # 만들 수 없으면 만들 수 있는 카드를 뽑기
    else:
        cnt = 0
        for new_card in new_cards:
            if new_card in need_card_lst:
                hand.append(new_card)
                coin -= 1
                need_card_lst.remove(new_card)
                cnt += 1
        # 뽑아서도 타겟값을 만들 수가 없으면 게임 종료
        if cnt == 0:
            break

print(round)
            
        
        
    
    
    
    