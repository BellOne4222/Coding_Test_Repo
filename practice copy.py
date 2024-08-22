import sys

n = int(sys.stdin.readline())

h = list(map(int, sys.stdin.readline().split()))

a = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    cur = h[i]
    h[i] = [cur, a[i]]


h.sort(key = lambda x:x[1])

total = h[0][0]
h[0][0] = 0

for j in range(1,n):
    
    for k in range(n):
        h[k][0] = h[k][0] + h[k][1]
    total += h[j][0]

print(total)
    