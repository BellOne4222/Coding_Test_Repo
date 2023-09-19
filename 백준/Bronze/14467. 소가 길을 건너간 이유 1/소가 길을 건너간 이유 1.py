n = int(input())

road = [-1] * 11
accross = 0

for i in range(n):
    cow, location = map(int,input().split())
    if road[cow] == -1:
        road[cow] = location
    elif road[cow] != location:
        accross += 1
        road[cow] = location
    

print(accross)
            
            
    
    
        
        
        
        
        