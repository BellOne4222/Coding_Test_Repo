# 1차 코드에서 자른 배열의 합을 받는 배열을 먼저 set 처리를 해서 시간복잡도 조금 개선

from collections import deque
import itertools
import sys

sys.setrecursionlimit(1000000)  # 기본 재귀 깊이는 1000이므로 얕아서 재귀깊이를 10**6으로 깊이 만들어 시간 초과 해결

def solution(elements):
    arr = deque(elements)
    sums = set()  # 중복을 제거하기 위해 set 사용
    n = len(elements)
    for i in range(1, n + 1):  # 길이가 1부터 배열의 길이까지 증가하며 크기만큼의 합을 구함
        for j in range(n):
            sum_arr = sum(itertools.islice(arr, 0, i))  # islice를 이용해서 deque slice
            sums.add(sum_arr)  # 해당 크기만큼 자른 배열의 합을 sums에 저장
            a = arr.popleft()  # 맨 앞 배열 원소를 빼서 배열 맨 뒤에 넣기(원형 배열 구현)
            arr.append(a)

    return len(sums)  # 결과 배열의 길이 반환