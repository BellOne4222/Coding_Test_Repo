def dfs(n, cnt):
    global ans
    if ans >= (cnt + (N - n) * 2):  # 남은 계란들을 모두 깨더라도 현재 최대값을 넘지 못할 경우 탐색 중지
        return

    if n == N:  # 모든 계란을 손에 들고 부딪히기를 완료한 경우
        ans = max(ans, cnt)  # 현재 깨진 계란의 개수가 최대값보다 큰지 확인하고 업데이트
        return

    if arr[n][0] <= 0:  # 현재 들고 있는 계란이 이미 깨져있는 경우, 다음 계란으로 넘어감
        dfs(n + 1, cnt)
    else:  # 현재 계란이 깨지지 않았다면, 다른 계란들과 부딪혀보기
        flag = False  # 현재 계란으로 다른 계란을 치지 않은 경우를 체크
        for j in range(N):  # 모든 계란을 대상으로 부딪혀보기
            if n == j or arr[j][0] <= 0:  # 자기 자신이거나 이미 깨진 계란은 제외
                continue
            flag = True
            arr[n][0] -= arr[j][1]  # 서로 부딪힘
            arr[j][0] -= arr[n][1]
            dfs(n + 1, cnt + int(arr[n][0] <= 0) + int(arr[j][0] <= 0))  # 다음 계란으로 넘어가며 깨진 계란 수 업데이트
            arr[n][0] += arr[j][1]  # 원래 상태로 복구
            arr[j][0] += arr[n][1]
        if not flag:  # 현재 계란으로 다른 계란을 치지 않았다면, 다음 계란으로 넘어감
            dfs(n + 1, cnt)

N = int(input())  # 계란의 수
arr = [list(map(int, input().split())) for _ in range(N)]  # 계란의 내구도와 무게 정보

ans = 0  # 깨진 계란의 최대 개수
dfs(0, 0)  # 탐색 시작
print(ans)  # 결과 출력