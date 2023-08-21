N = int(input())

stairs = [0]
for i in range(1, N+1):
    stairs.append(int(input()))
    
dp_table = [0] * (N+1)

dp_table[1] = stairs[1]
dp_table[2] = stairs[1] + stairs[2]

for j in range(3,N+1):
    dp_table[j] = max(stairs[j] + stairs[j-1] + dp_table[j-3], stairs[j] + dp_table[j-2])

print(dp_table[N])