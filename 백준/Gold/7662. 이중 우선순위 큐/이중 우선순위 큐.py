import sys
import heapq
T = int(input())
for _ in range(T):
    k = int(input())
    maxhq = []
    minhq = []
    done = [0]*k   # 삭제된건지 확인
    for i in range(k):
        a, b = sys.stdin.readline().split()
     
        if a == 'I':
            heapq.heappush(maxhq,((-1)*int(b),i))
            heapq.heappush(minhq,(int(b),i))
        
        elif a == 'D':
            if b == '-1':  # 최솟값
                while minhq:
                    if done[minhq[0][1]] == 1:
                        heapq.heappop(minhq)
                    else:
                        break
                if minhq:
                    min = minhq[0][1]
                    done[min] = 1
                    heapq.heappop(minhq)
                    
            elif b == '1':
                while maxhq:
                    if done[maxhq[0][1]] == 1:
                        heapq.heappop(maxhq)
                    else:
                        break
                if maxhq:
                    max = maxhq[0][1]
                    done[max] = 1
                    heapq.heappop(maxhq)
            
    while maxhq:
            if done[maxhq[0][1]] == 1:
                heapq.heappop(maxhq)
            else:
                break
    while minhq:
            if done[minhq[0][1]] == 1:
                heapq.heappop(minhq)
            else:
                break
    if minhq:
        print((-1)*maxhq[0][0], minhq[0][0])
    else:
        print("EMPTY")