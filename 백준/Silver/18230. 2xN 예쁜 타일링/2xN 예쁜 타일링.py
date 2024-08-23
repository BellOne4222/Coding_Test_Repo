import sys
from collections import deque

n, a, b = map(int, sys.stdin.readline().split())

a_lst = list(map(int, sys.stdin.readline().split()))
b_lst = list(map(int, sys.stdin.readline().split()))

a_lst.sort(reverse=True)
b_lst.sort(reverse=True)

a_lst = deque(a_lst)
b_lst = deque(b_lst)

result = []

cnt = n // 2
remain_cnt = n % 2

# 남은 한 칸에 2x1 타일을 하나 채우는 경우
if remain_cnt != 0 and a_lst:
    result.append(a_lst.popleft())

# 2x2 타일과 2개의 2x1 타일을 비교하여 채우는 경우
if cnt != 0:
    for _ in range(cnt):
        if len(a_lst) > 1 and b_lst:
            tile_1 = a_lst[0] + a_lst[1]
            tile_2 = b_lst[0]
            
            if tile_1 > tile_2:
                result.append(a_lst.popleft())
                result.append(a_lst.popleft())
            else:
                result.append(b_lst.popleft())
        elif len(b_lst) > 0:
            result.append(b_lst.popleft())
        elif len(a_lst) > 1:
            result.append(a_lst.popleft())
            result.append(a_lst.popleft())

print(sum(result))
