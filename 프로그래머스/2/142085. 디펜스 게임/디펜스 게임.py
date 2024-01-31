# 참고 : https://magentino.tistory.com/51

from heapq import heappush, heappop

def solution(n, k, enemy):
    stage = len(enemy)  # 라운드의 총 개수를 구함
    if k >= stage:  # 사용 가능한 무적권의 횟수가 라운드의 총 개수 이상인 경우 모든 라운드를 막을 수 있음
        return stage

    q = []  # 우선순위 큐를 사용할 heap 생성
    
    for i in range(stage):
        heappush(q, enemy[i])  # 현재 라운드의 적 수를 heap에 추가
        if len(q) > k:  # heap의 크기가 사용 가능한 무적권의 횟수보다 크면
            last = heappop(q)  # 가장 낮은 적 수를 가진 라운드를 제거
            if last > n:  # 남은 병사 수보다 해당 라운드의 적 수가 많은 경우
                return i  # 현재 라운드에서 게임 종료
            n -= last  # 현재 라운드를 성공적으로 막았으므로 남은 병사 수 업데이트
        
    return stage  # 모든 라운드를 성공적으로 막았으므로 라운드의 총 개수를 반환