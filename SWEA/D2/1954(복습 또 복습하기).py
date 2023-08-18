# 1954 달팽이 숫자
# https://velog.io/@94applekoo/SWEA-2564.-%EB%8B%AC%ED%8C%BD%EC%9D%B4-%EC%88%AB%EC%9E%90-Python - 참고
# https://www.youtube.com/watch?v=rw2gQg9

# 1. 배열의 초기 좌표 잡기 
# 2. 움직이는 방향대로 i와 j의 증감값 파악하기(cnt += 1하면서)
# 3. 범위 밖으로 벗어나면 방향 바꾸기
# 4. 12에서 범위 내이지만 더 갈 수 없으므로 오른쪽 방향으로 맨 처음 증감값으로 돌아가서 다시 계산

# (1) 범위 이내
# (2) arr 값이 0인 경우 # (1),(2) 인 경우에만 다음 위치를 적을 수 있고, 넘는다면 else
# else 방향 전환
# n^2 보다 작은 범위 내에서 cnt 증가

# 3. 코드 설계
# 초기 : i = 0, j = 0, cnt = 1, arr[i][j] = cnt, cnt += 1
# while cnt <= N * N
# 다음 위치 계산 = next_i, next_j 
# di, dj i와 j의 변화값을 리스트로 생성
# di = [0,1,0,-1], dj = [1,0,-1,0]
# 12칸에서 더 갈곳이 없을때 증감값을 맨 처음으로 돌아간다
# next_i = i + di[dr] nj = j+dj[dr]  # [dr] : 방향
# if 0 <= nj < N and 0 <= nj < N and arr[ni][nj] == 0
# i,j = ni, nj  arr[i][j] = cnt cnt+=1
# else dr = (dr + 1) % 4 # 배열의 범위를 넘을 때, 즉 4일때 다시 0으로 돌아오려면 % 4처리

# 1번 코드
T = int(input())
di =[0,1,0,-1] # i와 j의 증감값으로 리스트 생성
dj = [1,0,-1,0]
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)] # N * N의 0으로 이루어진 2차원 배열 생성, listconprehension
    
    i, j, cnt, dr = 0, 0, 1, 0  # 초기화, i,j의 초기 위치와 cnt로 위치의 번호 부여, dr은 direction으로 방향을 나타냄
    arr[i][j] = cnt # cnt로 그 칸의 번호 부여
    cnt += 1 # 칸은 갈수록 1씩 증가
    
    while cnt <= N*N: # 2차월 배열 이내일때 반복
        next_i, next_j = i + di[dr], j + dj[dr]  # 다음 좌표
        if 0 <= next_i< N and 0 <= next_j <= N and arr[next_i][next_j] == 0: # 다음 i,j의 좌표가 범위 이내이고, 칸의 값이 0이라면 = 아직 cnt를 적지 않은 상태라면
            i, j = next_i, next_j # i,j를 다음 좌표로 이동
            arr[i][j] = cnt
            cnt += 1
        else:
            dr = (dr+1) % 4 # 계속 순환해서 돌아야하기때문에 dr에 1을 더해주고, 순환값의 첫번째로 돌아온다. , 방향전환
    
    print(f'#{test_case}')
    for lst in arr:
        print(*lst)


# 2번 코드(1번 코드 보완)
def isValid(row, col):
    if (row >= 0 and row < n and col >= 0 and col < n): # row, col의 조건은 0보다 크고 N보다 작은 범위
        return True
    else:
        return False


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    snail = [[0]*n for _ in range(n)] # 0으로 채워진 N*N 2차원 배열 생성

    # rd: row of direction, cd: column of direction
    # right, down, left, up, i와 j의 증감값 리스트로 생성
    rd = [0, 1, 0, -1] 
    cd = [1, 0, -1, 0]

    # cr: current row, cc: current column
    cr, cc = 0, -1
    direction = 0 # 0:right, 1:down, 2:left, 3:up

    i = 1
    while (i <= n*n):
        cr += rd[direction]
        cc += cd[direction]

        while(isValid(cr, cc) and snail[cr][cc] == 0):
            snail[cr][cc] = i
            cr += rd[direction]
            cc += cd[direction]
            i += 1

        # 범위를 벗어났으므로 진행된 방향 반대로 한칸 이동(이동하기 전으로 다시 돌아감)
        cr -= rd[direction]
        cc -= cd[direction]

        # 다음 방향으로 넘어가는데, 우-하-좌-상 4가지 방향으로 반복해서 순환되므로 % 연산 사용
        direction = (direction + 1) % 4

    print(f'#{test_case}')
    for row in snail:
        print(*row) # *붙이면 [] 없이 출력

# 나선형 순회 알고리즘은 사전에 이미 여기에서 다룬 적이 있다.

# 링크의 레퍼런스 코드에서 작성한 대로 right, down, left, up 각 방향별 인덱스 좌표 이동을 배열에 저장 후 활용하는 방식으로 구현했다.

# 링크에서는 나선형 순회를 하며 배열의 값을 읽어야했다면, 이번 문제에서는 나선형 순회를 하며 순회 순서대로 숫자 값을 1부터 행렬 크기까지 넣어줘야한다. 따라서 기존 코드와 크게 달라지는 부분은 없다.

