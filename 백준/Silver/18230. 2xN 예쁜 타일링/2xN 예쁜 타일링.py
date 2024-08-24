import sys
from collections import deque

# 입력받은 n, a, b 값을 통해 n은 바닥 크기, a는 2x1 타일 개수, b는 2x2 타일 개수
n, a, b = map(int, sys.stdin.readline().split())

# 2x1 타일의 예쁨 값을 입력받아 리스트로 저장하고, 내림차순으로 정렬
a_lst = list(map(int, sys.stdin.readline().split()))
# 2x2 타일의 예쁨 값을 입력받아 리스트로 저장하고, 내림차순으로 정렬
b_lst = list(map(int, sys.stdin.readline().split()))

# 타일의 예쁨 값이 높은 순서대로 사용하기 위해 리스트를 정렬
a_lst.sort(reverse=True)
b_lst.sort(reverse=True)

# 정렬된 리스트를 덱(deque)으로 변환해 빠르게 요소를 꺼낼 수 있도록 함
a_lst = deque(a_lst)
b_lst = deque(b_lst)

# 결과를 저장할 리스트 초기화
result = []

# 바닥을 2x2 타일로 채울 수 있는 최대 개수
cnt = n // 2
# 남은 1칸이 존재하는지 확인
remain_cnt = n % 2

# 남은 1칸이 있을 경우, 2x1 타일을 사용해 채움
if remain_cnt != 0 and a_lst:
    result.append(a_lst.popleft())  # 가장 큰 예쁨 값을 가진 2x1 타일을 사용

# 2x2 타일을 사용할 수 있는 경우 처리
if cnt != 0:
    for _ in range(cnt):
        # 2개의 2x1 타일과 1개의 2x2 타일 중 더 큰 예쁨 값을 선택
        if len(a_lst) > 1 and b_lst:
            tile_1 = a_lst[0] + a_lst[1]  # 가장 큰 두 개의 2x1 타일의 예쁨 값 합
            tile_2 = b_lst[0]  # 가장 큰 2x2 타일의 예쁨 값
            
            if tile_1 > tile_2:
                # 2개의 2x1 타일을 선택해 바닥에 배치
                result.append(a_lst.popleft())
                result.append(a_lst.popleft())
            else:
                # 2x2 타일을 선택해 바닥에 배치
                result.append(b_lst.popleft())
        elif len(b_lst) > 0:
            # 만약 2x2 타일만 남아 있다면 이를 사용
            result.append(b_lst.popleft())
        elif len(a_lst) > 1:
            # 만약 2x1 타일만 남아 있다면 이를 사용
            result.append(a_lst.popleft())
            result.append(a_lst.popleft())

# 모든 타일을 배치한 후 예쁨 값의 합을 출력
print(sum(result))
