from collections import Counter

topping = [1, 2, 1, 3, 1, 4, 1, 2]	

answer = 0
chulsu = Counter(topping) 
brother = set()
    
for t in topping:
    chulsu[t] -= 1
    brother.add(t)
        
    if chulsu[t] == 0:
        chulsu.pop(t)
            
    if len(chulsu) == len(brother):
        answer += 1

print(answer)

        
    
    
    