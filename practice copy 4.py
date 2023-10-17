import sys

n = int(sys.stdin.readline().rstrip())
p = ""

for i in range((2*n)+1):
    if i%2 == 0:
        p += "I"
    else:
        p += "O"

m = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()
p_cnt = 0
for i in range(m-len(p)+1):
    compare = s[i:i+len(p)] 
    if compare == p:
        p_cnt += 1
    
    

print(p_cnt)
