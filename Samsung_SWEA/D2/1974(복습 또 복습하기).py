# 1974 스도쿠 검증

# 스도쿠 검증 함수 생성
def checkSudoku(M):
    for i in range(9):
        row_num = [0] * 10
        col_num = [0] * 10
        for j in range(9):
            # 가로 검사
            row = M[i][j]
            # 세로 검사
            col = M[j][i]

            # 이미 사용된 숫자라면, 0을 리턴
            if row_num[row]:
                return 0
            if col_num[col]:
                return 0
            
            # 아니라면, row_num과 col_num의 각 숫자 위치를 1로 변경
            row_num[row] = 1
            col_num[col] = 1

            # 3x3 행렬 검사
            if i % 3 == 0 and j % 3 == 0:
                square = [0] * 10
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        num = M[r][c]
                        if square[num]:
                            return 0
                        square[num] = 1
    
    # 반복문이 정상적으로 다 수행된다면, 올바른 스도쿠이므로 1을 리턴
    return 1

# 테스트 케이스 개수 T 입력
T = int(input())
for tc in range(1, T+1):
    # 검사를 위한 행렬 입력
    mat = [list(map(int, input().split())) for _ in range(9)]

    # checkSudoku() 함수를 사용해서 return 값을 result에 저장
    result = checkSudoku(mat)

    # 결과 출력
    print('#{} {}'.format(tc, result))




import sys

maps=[list(map(int,[p for p in sys.stdin.readline().split()])) for _ in range(9)]

#가로
def hori():
    ans=0
    for i in range(9):
        nums = list(range(1, 10))
        cnt = 0
        for j in range(9):
            if maps[i][j] in nums:
                nums.remove(maps[i][j])
                cnt+=1
            else:
                return False
        if cnt==9:
            ans+=1
    if ans==9:
        #print('가로','True')
        return True
    return False

#세로
def verti():
    ans=0
    for i in range(9):
        nums = list(range(1, 10))
        cnt=0
        for j in range(9):
            if maps[j][i] in nums:
                nums.remove(maps[j][i])
                cnt+=1
            else:
                return False
        if cnt==9:
            ans+=1
    if ans == 9:
        #print('세로', 'True')
        return True
    return False

#3x3
def bythree():
    ans=0
#     그리고 각 시작점 (0,0),(3,0),(6,0) 에 대해 검사를 해주어야 하므로 아래와 같이 구현합니다.

#                        (0,3),(3,3),(6,3)

#                        (0,6),(3,6),(6,6)

# 각각 x,y좌표가 3씩 증가해서 6까지만 증가하므로 2중포문을 만들어주었고 범위는 (0,7,3)으로 주었습니다.
    for x in range(0,7,3):
        for y in range(0,7,3):
            nums = list(range(1, 10))
            cnt=0
            for i in range(3): # 정사각형 구현
                for j in range(3):
                    if maps[i+x][j+y] in nums:
                        nums.remove(maps[i+x][j+y])
                        cnt+=1
            if cnt==9:
                ans+=1
    if ans==9:
        #print('3x3', 'True')
        return True
    return False

if hori() and verti() and bythree():
    print(1)
else:
    print(0)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t in range(1, T + 1):
    M=[[*map(int,input().split())]for _ in range(9)]
    c=1
    for i in range(9):
        if len(set(M[i]))<9:c=0
    M=[*zip(*M)]
    for j in range(9):
        if len(set(M[j]))<9:c=0
    for i in range(0,7,3):
        for j in range(0,7,3):
            if len(set(M[k][l]for k in range(i,i+3)for l in range(j,j+3)))<9:c=0
    print(f'#{t}',c)

# zip
# numbers = [1, 2, 3]
# >>> letters = ["A", "B", "C"]
# >>> for pair in zip(numbers, letters):
# ...     print(pair)
# ...
# (1, 'A')
# (2, 'B')
# (3, 'C')