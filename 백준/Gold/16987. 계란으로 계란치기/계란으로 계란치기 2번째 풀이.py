def BackTracking(start):
    global Answer
    if start == N: # 모든 계란에 대해 시도해본 경우
        total = 0
        for i in range(N):
            if egg[i][0] <= 0: # 깨진 계란의 개수를 센다
                total += 1
        Answer = max(Answer, total) # 지금까지의 최대값과 비교하여 더 큰 값을 저장
        return

    if egg[start][0] <= 0: # 현재 든 계란이 이미 깨져있으면 다음 계란으로 넘어간다
        BackTracking(start + 1)
        return

    check = True
    for i in range(N):
        if i == start:
            continue
        if egg[i][0] > 0: # 깨지지 않은 다른 계란이 있는지 확인
            check = False
            break

    if check: # 모든 계란이 깨져있으면 현재 계란을 제외하고 종료
        Answer = max(Answer, N - 1) # 자기 자신을 제외한 모든 계란이 깨져있으므로 N-1
        return

    for i in range(N):
        if i == start or egg[i][0] <= 0: # 자기 자신이거나 이미 깨진 계란은 제외
            continue
        egg[start][0] -= egg[i][1] # 현재 계란으로 다른 계란을 친다
        egg[i][0] -= egg[start][1] # 상대 계란으로 현재 계란을 친다
        BackTracking(start + 1) # 다음 계란으로 넘어간다
        egg[start][0] += egg[i][1] # 원래 상태로 복구
        egg[i][0] += egg[start][1] # 원래 상태로 복구

N = int(input()) # 계란의 수
egg = [list(map(int, input().split())) for _ in range(N)] # 각 계란의 내구도와 무게
Answer = 0 # 깰 수 있는 계란의 최대 개수
BackTracking(0) # 백트래킹 시작

print(Answer) # 결과 출력