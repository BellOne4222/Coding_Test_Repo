# deque를 쓰는 문제여서 deque를 사용해서 각 큐의 합을 구해 주고 두 큐의 합을 더한 all_sm의 반을 target으로 설정해서 두 큐 각각의 합이 target에 도착하면 종료하는 로직
# 각 큐의 합을 비교하며 더 큰쪽에서 popleft를 한걸 작은 큐에 append하며 target값에 맞추는 방식 사용
# 중간에 pop횟수와 append 횟수를 받아서 둘다 1이 될때마다 result +=1 처리를 하여 결과 반환
# 총 시도 횟수는 두 큐의 길이 합의 2배로 여유롭게 설정(1번 테케 반례 때문에)
# 총 시도 횟수에도 target값에 못가면 -1 반환

from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sm_1 = sum(queue1)
    sm_2 = sum(queue2)
    all_sm = sm_1 + sm_2
    target = int(all_sm / 2) # target값은 전체 큐의 원소 합의 절반
    change = 0 # 큰쪽에서 popleft한 원소를 받는 변수
    all_queue = queue1 + queue2 
    cnt = len(all_queue) * 2 # 총 시도 횟수 = 큐 두개의 길이의 합의 2배
    p = 0  # pop 횟수
    a = 0  # append 횟수
    result = 0

    while cnt > 0: # 총 시도 횟수가 0일 될때 까지 반복
        if p == 1 and a == 1:
            result += 1
            p = 0
            a = 0

        if sm_1 == target and sm_2 == target:
            return result
        
        if sm_1 > sm_2:
            change = queue1.popleft()
            p += 1
            queue2.append(change)
            a += 1
            sm_1 -= change
            sm_2 += change
            cnt -= 1
        elif sm_1 < sm_2:
            change = queue2.popleft()
            p += 1
            queue1.append(change)
            a += 1
            sm_1 += change
            sm_2 -= change
            cnt -= 1
        

    return -1  # 조건을 만족하는 경우가 없을 때 -1 반환

