# https://takeu.tistory.com/263 참고
# 최대 힙과 최소 힙 만들어서 구현

from heapq import heappush, heappop  # heapq 모듈에서 heappush와 heappop 함수를 임포트합니다.
import sys
input = sys.stdin.readline  # 입력을 더 빠르게 처리하기 위해 sys.stdin.readline을 input 함수로 사용합니다.

n = int(input())  # 문제의 개수 n을 입력으로 받습니다.
min_h, max_h = [], []  # 최소 힙과 최대 힙을 초기화합니다.
d = {}  # 문제 번호를 키로 가지는 딕셔너리를 초기화합니다. 문제 번호를 추적하려고 사용합니다.

# n번 반복하여 문제의 정보를 입력받고 최소 힙과 최대 힙에 추가합니다.
for _ in range(n):
    p, l = map(int, input().split())  # 문제 번호 p와 난이도 l을 입력으로 받습니다.
    heappush(min_h, [l, p])  # 최소 힙에 [난이도, 문제 번호]를 추가합니다.
    heappush(max_h, [-l, -p])  # 최대 힙에 [-난이도, -문제 번호]를 추가합니다. (음수를 사용하여 최대 힙을 구현)
    d[p] = True  # 문제 번호 p를 딕셔너리에 추가하여 추적합니다.

M = int(input())  # 수행할 작업의 개수 M을 입력으로 받습니다.
for _ in range(M):
    command = input().split()  # 공백으로 분리된 작업을 입력으로 받습니다.

    if command[0] == 'recommend':
        if command[1] == '1':
            # "recommend 1" 작업: 가장 어려운 문제 번호를 출력합니다.
            while not d[-max_h[0][1]]:
                heappop(max_h)  # 딕셔너리에 표시되지 않은 문제는 최대 힙에서 제거합니다.
            print(-max_h[0][1])  # 최대 힙의 가장 난이도가 높은 문제 번호를 출력합니다.
        else:
            # "recommend -1" 작업: 가장 쉬운 문제 번호를 출력합니다.
            while not d[min_h[0][1]]:
                heappop(min_h)  # 딕셔너리에 표시되지 않은 문제는 최소 힙에서 제거합니다.
            print(min_h[0][1])  # 최소 힙의 가장 난이도가 낮은 문제 번호를 출력합니다.

    elif command[0] == 'add':
        p, l = int(command[1]), int(command[2])
        while not d[-max_h[0][1]]:
            heappop(max_h)  # 딕셔너리에 표시되지 않은 문제는 최대 힙에서 제거합니다.
        while not d[min_h[0][1]]:
            heappop(min_h)  # 딕셔너리에 표시되지 않은 문제는 최소 힙에서 제거합니다.
        d[p] = True  # 문제 번호 p를 딕셔너리에 추가하여 추적합니다.
        heappush(max_h, [-l, -p])  # 최대 힙에 [난이도, -문제 번호]를 추가합니다.
        heappush(min_h, [l, p])  # 최소 힙에 [난이도, 문제 번호]를 추가합니다.

    else:
        # "solved" 작업: 문제 번호 P를 딕셔너리에서 제거하여 추척을 해제합니다.
        d[int(command[1])] = False