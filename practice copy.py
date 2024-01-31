# 40.6점

n,	k,	enemy = 7,	3,	[4, 2, 4, 5, 3, 3, 1]

round = 0
    
most_common_enemy = sorted(enemy, reverse = True) #	[5, 4, 4, 3, 3, 2, 1] 
most_common_enemy = most_common_enemy[:k] # [5, 4, 4]  
    
for i in range(len(enemy)):
    if k != 0:
        if enemy[i] in most_common_enemy:
            k -= 1
            most_common_enemy.remove(enemy[i])
            round += 1
        else:
            n -= enemy[i]
            round += 1
                
    else:
        if n < enemy[i]:
            break
        n -= enemy[i]
        round += 1

print(round)