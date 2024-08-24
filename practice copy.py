import sys
from itertools import combinations
from collections import deque

n,a,b = map(int, sys.stdin.readline().split())

a_lst = list(map(int, sys.stdin.readline().split()))

b_lst = list(map(int, sys.stdin.readline().split()))

result = []

a_lst.sort(reverse=True)
b_lst.sort(reverse=True)

a_lst = deque(a_lst)
b_lst = deque(b_lst)

cnt = n // 2
no_cnt = n % 2

if n == 1:
    result.append(a_lst[0])
else:
    a_comb = list(combinations(a_lst,2))
    a_comb.sort(key = lambda x:sum(x), reverse=True)
    a_comb = deque(a_comb)
    for i in range(cnt):
        if sum(a_comb[0]) > b_lst[0]:
            result.append(sum(a_comb[0]))
            used_a = a_comb[0][0]
            used_b = a_comb[0][1]
            a_lst.rotate(2)
            for k in range(len(a_comb)):
                if used_a in a_comb[0] or used_b in a_comb[0]:
                    a_comb.rotate(1)
                else:
                    break
                
        else:
            result.append(b_lst[0])
            b_lst.rotate(1)

    if no_cnt != 0:
        for j in range(no_cnt):
            result.append(a_lst[j])
    
print(sum(result))
    
        
        
    
    