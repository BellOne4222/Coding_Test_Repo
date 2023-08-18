# heapq.heapify(scoville) # scoville을 힙으로 지정
# heapq.heappop(scoville) # scoville에서 가장 작은 원소를 pop
# heapq.heappush(scoville, new) # scoville에 섞은 스코빌 지수를 추가
# heap에서 [0]는 이진트리 방식이기 때문에 가장 작은 원소를 반환
import heapq

def solution(scoville, K):
    heapq.heapify(scoville) # scoville을 힙으로 지정
    mix = 0 # 섞은 횟수
    
    while scoville[0] <= K:
        if len(scoville) == 1:
            return -1
        if scoville[0] >= K:
            return mix
            
        a = heapq.heappop(scoville) # scoville에서 가장 작은 원소를 pop
        b = heapq.heappop(scoville)
        new = a + (b*2)
        heapq.heappush(scoville, new) # scoville에 섞은 스코빌 지수를 추가
        mix += 1 # 섞은 횟수 + 1
        
    return mix