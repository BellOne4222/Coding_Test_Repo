# 1979 어디에 단어가 들어갈 수 있을까
# 1인칸일때 카운트 늘려가다가 칸 값이 0이나 마지막 칸 전에 도착할 때, K와 값이 똑같으면 ans 값 1 증가시켜서 ans 최종값 반환 

T = int(input())
for test_case in range(1, T + 1):
    N, K  = map(int,input().split()) # N, K 입력값 받기
    puzzle =[ list(map(int, input().split())) for _ in range(N)] # 2차원 배열로 이루어진 퍼즐 입력 받기, N 만큼 반복해서
    ans = 0
    
    
    for i in range(N):
        cnt = 0 
        # 행에서 ans 추적
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == N - 1:
                if cnt == K:
                    ans += 1
                cnt = 0

        # 열에서 ans 추적
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt +=1
            if puzzle[j][i] == 0 or j == N - 1:
                if cnt == K:
                    ans += 1
                cnt = 0
    print("#{} {}".format(test_case, ans))