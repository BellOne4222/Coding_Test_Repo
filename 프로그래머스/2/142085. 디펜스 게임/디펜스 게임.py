# 참고 : https://magentino.tistory.com/51

from heapq import heappush, heappop

def solution(n, k, enemy):
    round = len(enemy)  # 라운드의 총 개수를 구함
    if k >= round:  # 사용 가능한 무적권의 횟수가 라운드의 총 개수 이상인 경우 모든 라운드를 막을 수 있음
        return round

    q = []  # 우선순위 큐를 사용할 heap 생성
    
    for i in range(round):
        heappush(q, enemy[i])  # 현재 라운드의 적 수를 heap에 추가
        if len(q) > k:  # heap의 크기가 사용 가능한 무적권의 횟수보다 크면
            last_enemy = heappop(q)  # 가장 낮은 적 수를 가진 라운드를 제거
            if last_enemy > n:  # 남은 병사 수보다 해당 라운드의 적 수가 많은 경우
                return i  # 현재 라운드에서 게임 종료
            n -= last_enemy  # 현재 라운드를 성공적으로 막았으므로 남은 병사 수 업데이트
        
    return round  # 모든 라운드를 성공적으로 막았으므로 라운드의 총 개수를 반환

# 현재까지의 round중 가장 enemy가 많았던 k개에 무적권을 쓰는 것이 항상 가장 최선의 전략임을 알 수 있다. 
# 따라서 그리디하게 가장 많은 enemy를 저장하며 문제를 풀이하면 된다. 이 경우 priority queue, heap를 쓰는 게 좋다.

# 1. round 개수보다 무적권의 개수 k가 같거나 더 많다면 모든 경우에 무적권을 사용할 수 있으므로, round의 길이를 반환한다.
# 2. priority queue에 초반 k의 enemy를 저장한다.
# 3. k를 넘어선다면, i번째 round의 enemy[i-1]를 priority queue에 저장하고, 하나를 pop한다. 그리고 그 pop한 enemy를 남은 병사 수 n에서 차감한다. 
# 만약 차감하는 데 실패한다면(즉 차가 0보다 작아진다면) 최선의 경우에도 더 이상 게임을 진행하는 것이 불가능하므로, i-1를 리턴한다.

