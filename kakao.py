import sys

n = int(sys.stdin.readline().rstrip())

a = list(map(int, sys.stdin.readline().split()))

left_dp_table = [0] * (n)
right_dp_table = [0] * (n)


# left 
for i in reversed(range(n)):
    cnt = 1
    num = []
    for j in range(i):
        if a[i] > a[j]:
            if a[j] not in num:
                num.append(a[j])
                cnt += 1
        else:
            continue
    
    left_dp_table[i] = max(cnt, left_dp_table[i])
        
        


# right
for k in range(n):
    compare = a[k]
    cnt = 1
    num = []
    for l in reversed(range(k,n)):
        com = a[l]
        if a[k] > a[l]:
            if a[l] not in num:
                num.append(a[l])
                cnt += 1
    
    right_dp_table[k] = max(cnt, right_dp_table[k])

left_max_idx = left_dp_table.index(max(left_dp_table))
right_max_idx = (n - 1 - right_dp_table.index(max(right_dp_table)))

print(left_dp_table[left_max_idx] + right_dp_table[right_max_idx])
    
