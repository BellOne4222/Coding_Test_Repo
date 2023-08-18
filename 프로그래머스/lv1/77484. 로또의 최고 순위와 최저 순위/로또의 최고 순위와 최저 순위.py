def solution(lottos, win_nums):
    lotto = sorted(lottos)
    win_num = sorted(win_nums)
    high_count = 0
    low_count = 0
    ranks = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6} # 맞춘 개수:등수
    for i in lotto:
        if i in win_num:
            high_count += 1
            low_count += 1
        elif i == 0:
            high_count += 1
    
    result = [ranks[high_count], ranks[low_count]]
    return result
            