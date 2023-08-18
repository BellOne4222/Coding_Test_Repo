# 1번 테스트 케이스 빼고 다 성공해서 반례를 찾아 봤더니  A = [3, 3, 3, 3], B = [3, 3, 21, 3] 이 반례 같은 경우 최소 경우의수가 내가 설정해 놓은 배열의 길이의 합보다 클 때까지 보다 더 많으므로, 중간에 -1을 반환해버려서 fail
# cnt 횟수를 배열의 합의 2배로 늘려줘서 해결

from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sm_1 = sum(queue1)
    sm_2 = sum(queue2)
    all_sm = sm_1 + sm_2
    target = int(all_sm / 2)
    change = 0
    all_queue = queue1+ queue2
    cnt = len(all_queue)
    p = 0 # pop 횟수
    a = 0 # apeend 횟수
    result = 0
    
    while cnt > 0:
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
    return -1
        
            
        