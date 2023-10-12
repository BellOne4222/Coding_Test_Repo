# https://imzzan.tistory.com/31 참고

import sys
import heapq

T = int(input())  # 테스트 케이스의 수를 입력받음

for _ in range(T):  # 각 테스트 케이스에 대해 반복
    k = int(input())  # 현재 테스트 케이스의 연산 개수를 입력받음
    maxhq = []  # 최대 힙을 나타내는 리스트
    minhq = []  # 최소 힙을 나타내는 리스트
    done = [0] * k  # 삭제된 항목을 추적하기 위한 리스트

    for i in range(k):  # 각 연산에 대해 반복
        a, b = sys.stdin.readline().split()  # 연산 유형과 숫자를 입력받음

        if a == 'I':  # 만약 연산 유형이 'I'라면 (삽입)
            heapq.heappush(maxhq, ((-1) * int(b), i))  # 최대 힙에 값을 음수로 넣어 삽입
            heapq.heappush(minhq, (int(b), i))  # 최소 힙에 값을 그대로 삽입

        elif a == 'D':  # 만약 연산 유형이 'D'라면 (삭제)
            if b == '-1':  # 최솟값 삭제
                while minhq:
                    if done[minhq[0][1]] == 1:  # 이미 삭제된 값이면 무시
                        heapq.heappop(minhq)
                    else:
                        break
                if minhq:
                    min = minhq[0][1]  # 삭제할 값의 인덱스
                    done[min] = 1  # 삭제 표시
                    heapq.heappop(minhq)  # 최소 힙에서 삭제

            elif b == '1':  # 최댓값 삭제
                while maxhq:
                    if done[maxhq[0][1]] == 1:  # 이미 삭제된 값이면 무시
                        heapq.heappop(maxhq)
                    else:
                        break
                if maxhq:
                    max = maxhq[0][1]  # 삭제할 값의 인덱스
                    done[max] = 1  # 삭제 표시
                    heapq.heappop(maxhq)  # 최대 힙에서 삭제

    # 아직 삭제되지 않은 값 중 최댓값과 최솟값을 찾음
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

    if minhq:  # 최소 힙에 값이 남아있으면 최댓값과 최솟값 출력
        print((-1) * maxhq[0][0], minhq[0][0])
    else:  # 최소 힙이 비어있으면 "EMPTY" 출력
        print("EMPTY")


# 최대힙과 최소힙 두 개를 따로 만들어서 최댓값은 최대힙을 이용하여 구하고 최솟값은 최소힙을 이용하여 구했다.

# 최대힙은 앞에서 푼 문제에서 했던 것처럼 값을 넣어줄 때  -1 을 곱해주어서 구현했다. 

# 값을 push 해줄 때는 (입력값, i번째) 쌍으로 넣어주었다. 최소힙에서 최솟값은 바로 뺄 수 있지만 최댓값은 바로 뺄 수 없고, 최대힙도 최댓값은 바로 뺄 수 있지만 최솟값을 바로 뺄 수 없다. 그래서 done 리스트를 만들어주었다.  pop이 최소힙 또는 최대힙에서 발생하면 i값을 인덱스로 갖는 done 리스트의 값을 1로 바꿔준다.

# 예를 들어 입력값이 D 1 이면 최대힙의 [0]번째 값이 최대값이 되는데 이 값을 pop하기 전에 이미 최소힙에서 pop된 값인지 확인을 먼저 해줘야한다. 그래서 done[maxhq[0][1]]의 값이 1이면 이미 pop된 값이기 때문에 while문을 통해 최대힙에서도 계속 pop을 해준다. while문을 빠져 나왔을 때 maxhq안에 값이 존재하면 [0]번째 값을 pop 해주고 done 리스트 값도 1로 바꿔주면 된다. 

# 마지막에 최소힙 또는 최대힙이 비어있으면 EMPTY를 출력해주고, 그렇지 않으면 최소힙과 최대힙에서 각각 [0]번째 값을 뽑아낸 후 최대힙에서 나온 값에는 -1을 곱해준 뒤 출력해주면 된다. 





