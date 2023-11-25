# 선물 주고 받은 기록 -> 다음 달 선물 가장 많이 받은 사람 예측

# if 두 사람이 선물을 주고 받은 기록: 더 많이 준 사람이 다음 달에 더 많이 받은 사람에게서 선물 1개 받는다
# if 두 사람이 선물을 주고 받은 기록 == 0 or 주고 받은 기록이 같다 : 선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물 1개 받는다
# 선물 지수 = 이번 달까지 자신이 친구들에게 준 선물의 수 - 받은 선물의 수
# if 두 사람의 선물 지수가 같다 : 다음 달에 선물을 주고 받지 않는다

# return 다음 달에 선물을 가장 많이 받을 친구의 받는 선물의 수

# friend = 친구들 이름
# gifts : 이번 달 까지 친구들이 주고 받은 선물의 기록

friends = ['joy', 'brad', 'alessandro', 'conan', 'david']
gifts = ['alessandro brad', 'alessandro joy', 'alessandro conan', 'david alessandro', 'alessandro david']

give_dict = {friend:[] for friend in friends}

given_dict = {friend:[] for friend in friends}
     
#{'muzi': ['frodo', 'frodo'], 'ryan': ['muzi', 'muzi', 'muzi'], 'frodo': ['muzi', 'ryan'], 'neo': ['muzi']}
#{'muzi': ['ryan', 'ryan', 'ryan', 'frodo', 'neo'], 'ryan': ['frodo'], 'frodo': ['muzi', 'muzi'], 'neo': []}

for i in range(len(gifts)):
    give_friend, given_friend = gifts[i].split(" ")
    give_dict[give_friend].append(given_friend)
    given_dict[given_friend].append(give_friend)
    
total_lst = [[0 for _ in range(len(friends))] for _ in range(len(friends))] # [[0, 0, 2, 0], [3, 0, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0]]
for friend in friends:
    for j in give_dict[friend]:
        total_lst[friends.index(friend)][friends.index(j)] = total_lst[friends.index(friend)][friends.index(j)] + 1
    

    
gift_point_dict = {friend:0 for friend in friends} # {'muzi': -3, 'ryan': 2, 'frodo': 0, 'neo': 1}
    
for friend in friends:
    give_point = len(give_dict[friend]) - len(given_dict[friend])
    gift_point_dict[friend] = give_point
    
    
next_month_given_lst = [0 for _ in range(len(friends))]


for k in range(len(friends)):
    for l in range(len(friends)):
        if k == l:
            continue
        elif total_lst[k][l] != 0:
            if total_lst[k][l] > total_lst[l][k]:
                next_month_given_lst[k] += 1
        elif total_lst[k][l] == 0 and total_lst[l][k] == 0 or total_lst[k][l] == total_lst[l][k]:
            if gift_point_dict[friends[k]] > gift_point_dict[friends[l]]:
                next_month_given_lst[k] += 1
            elif gift_point_dict[friends[k]] < gift_point_dict[friends[l]]:
                next_month_given_lst[l] += 1

print(next_month_given_lst)
                
                