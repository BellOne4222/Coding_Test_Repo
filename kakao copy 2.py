# 주사위 -> 1~n개, 1~6의 6개의 번호 중복 가능

# a,b 주사위 개수 반반

# 굴려서 나온 점수를 모두 합하여 큰쪽이 이김 비기면 무승부

# a의 승리할 확률이 높아질 수 있는 주사위?

from collections import deque

def compare(dice_1, dice_2):

    dice_1_win = 0
    dice_1_draw = 0
    dice_2_win = 0
    dice_2_draw = 0

    for i in range(len(dice_1)):
        for j in range(len(dice_2)):
            if dice_1[i] > dice_2[j]:
                dice_1_win += 1
            elif dice_1[i] == dice_2[j]:
                dice_1_draw += 1
                dice_2_draw += 1
            else:
                dice_2_win += 1

    total_dice_1 = (dice_1_win * 3) + (dice_1_draw * 1)
    total_dice_2 = (dice_2_win * 3) + (dice_2_draw * 1)

    if total_dice_1 > total_dice_2:
        more_win = dice_1
    elif total_dice_1 < total_dice_2:
        more_win = dice_2

    return more_win


dice = [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]

choiced_dice_idx_lst = []
choiced_dice_sum_lst = []

idx = 0
while True:
    choiced_dice_sum_lst.append(dice[idx])
    idx += 1
    if len(choiced_dice_sum_lst) == len(dice) // 2:
        break

choiced_dice_sum_lst.sort(key = lambda x : sum(x))
    
for i in range(len(dice) // 2, len(dice)):
    winner = compare(dice[i], choiced_dice_sum_lst[0])
    if winner != choiced_dice_sum_lst[0]:
        choiced_dice_sum_lst[0] = dice[i]
        continue
    winner = compare(dice[i], choiced_dice_sum_lst[1])
    if winner != choiced_dice_sum_lst[1]:
        choiced_dice_sum_lst[1] = dice[i]
    
for j in choiced_dice_sum_lst:
    choiced_dice_idx_lst.append(dice.index(j)+1)
    
choiced_dice_idx_lst.sort()

print(choiced_dice_idx_lst)