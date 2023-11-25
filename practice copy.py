my_cards = [3, 6, 7, 2]
target = 13
need_card_lst = []
my_cards.sort()
need_1 = 0
need_2 = 0
left = 0
right = len(my_cards) - 1 
while True:
    if my_cards[left] + my_cards[right] > target:
        need_card_lst.append(target - my_cards[left])
        right += 1
    elif my_cards[left] + my_cards[right] < target:
        left += 1
        need_card_lst.append(target - my_cards[left])
    elif my_cards[left] + my_cards[right] == target:
        flag = True
        need_1, need_2 = my_cards[left], my_cards[right]
        break
    flag = False

print(need_card_lst)

