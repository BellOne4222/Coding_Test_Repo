import sys

n = int(sys.stdin.readline())

grapes = [0] * 10001

for i in range(1,n+1):
    grapes[i] = int(sys.stdin.readline())

dp_table = [0] * 10001

dp_table[1] = grapes[1]
dp_table[2] = grapes[2]
dp_table[3] = max((dp_table[1] + grapes[3]), (dp_table[2] + grapes[3]))

for j in range(4,n):
    cnt = 0
    for k in range(1,j):
        cnt += 1
        if cnt != 3:
            dp_table[j] += grapes[k]
        else:
            cnt = 0
    dp_table[j] += grapes[j]
        
        

print(dp_table[n-1])