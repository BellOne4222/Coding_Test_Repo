import sys

N,M = map(int,sys.stdin.readline().split())

A_lst = list(map(int, sys.stdin.readline().split()))
left = 0
right = 1
case = 0



while right <= N and left <= right:
    compare = sum(A_lst[left:right])
    if compare == M:
        case += 1
        right += 1
    elif compare < M:
        right += 1   
    else:
        left += 1

print(case)