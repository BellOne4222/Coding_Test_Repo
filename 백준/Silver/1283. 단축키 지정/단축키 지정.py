n = int(input())
keys = []
for l in range(n):
    
    flag = False
    option = list(input().split())
    for i in range(len(option)):
        if option[i][0].lower() not in keys and option[i][0].upper() not in keys:
            keys.append(option[i][0])
            flag = True
            option[i] = "[" + option[i][0] + "]" + option[i][1:]
            break
    if not flag:
        for j in range(len(option)):
            flag = False
            for k in range(len(option[j])):
                #check = option[j][k].upper()
                if option[j][k].lower() not in keys and option[j][k].upper() not in keys:
                    keys.append(option[j][k])
                    if k != len(option[j])-1:
                        option[j] = option[j][:k] +"[" + option[j][k] + "]" + option[j][k+1:]
                    else:
                        option[j] = option[j][:k] +"[" + option[j][k] + "]"
                    flag = True
                    break
            if flag:
                break
    print(' '.join(option))
    
        
                
                
        