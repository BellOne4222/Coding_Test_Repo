n,m = map(int,input().split())

train = [[False for _ in range(20)] for _ in range(n)]

for i in range(m):
    operation = list(map(int,input().split()))
    if operation[0] == 1:
        if train[operation[1]][operation[2]] == False:
            train[operation[1]][operation[2]] = True
            
    elif operation[0] == 2:
        if train[operation[1]][operation[2]] == True:
            train[operation[1]][operation[2]] = False
        
    elif operation[0] == 3:
        for j in range(1,20):
            if j == 19:
                if train[operation[1]][j] == True:
                    train[operation[1]][j] == False
                
            elif train[operation[1]][j-1] == True:
                train[operation[1]][j] == True
                train[operation[1]][j-1] = False
                
            
    elif operation[0] == 4:
        for k in range(19):
            if k == 0:
                if train[operation[1]][k] == True:
                    train[operation[1]][k] = False
            if train[operation[1]][k+1] == True:
                train[operation[1]][k] == True
                train[operation[1]][k+1] = False
passed = []
passed.append(train[0])
for l in range(1,len(train)):
    if train[l] not in passed:
        passed.append(train[l])

print(len(passed))