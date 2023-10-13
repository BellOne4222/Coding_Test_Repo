import sys
from collections import Counter


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    clothes = []
    for _ in range(n):
        name, kind = sys.stdin.readline().split()
        clothes.append(kind)
    
    clothes = Counter(clothes) # Counter 사용해서 각 종류에 대한 개수 구현
    # Counter("headgear" : 2, "eyewear" : 1)

    case = 1
    for i in clothes:
        case *= clothes[i] + 1 # 각 종류에 대한 항목을 사용하거나 미사용 경우 -> hat 사용, turban 사용, 안쓰는 경우
    
    print(case - 1) # 모두 벗는 경우(알몸) 제거