import sys

t = int(sys.stdin.readline())


for _ in range(t):
    dp_table = [0] * 101
    n = int(sys.stdin.readline())
    
    dp_table[1] = 1
    dp_table[2] = 1
    dp_table[3] = 1
    dp_table[4] = 2
    dp_table[5] = 2
    
    if n < 6:
        print(dp_table[n])
    else:
        for i in range(6, n+1):
            dp_table[i] = dp_table[i-5] + dp_table[i-1]

        print(dp_table[n])