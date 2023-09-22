n = int(input())

classroom = [[0 for _ in range(n)] for _ in range(n)]


# 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

dr = [-1,1,0,0]
dc = [0,0,-1,1]

students = [list(map(int, input().split())) for _ in range(n*n)]


# 자리 배치
for i in range(n*n):
    student = students[i]
    # 4 [2, 5, 1, 7]

    seat_info = []
        
    for r in range(n):
        for c in range(n):
            if classroom[r][c] == 0:
                prefer = 0 # 선호하는 사람 수
                empty = 0 # 빈 자리 수
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < n and 0 <= nc < n:
                        if classroom[nr][nc] in student[1:]:
                            prefer += 1
                        if classroom[nr][nc] == 0:
                            empty += 1
                seat_info.append([prefer, empty, r, c])
    seat_info.sort(key = lambda x:(-x[0],-x[1],x[2],x[3])) # 3가지 조건에 따라, 선호하는 학생 수, 주변 빈 자리수, 행 번호, 열번호 순으로 정렬
    classroom[seat_info[0][2]][seat_info[0][3]] = student[0]

# 만족도 조사
total_sum = 0

students.sort()



for r in range(n):
    for c in range(n):
        like = 0
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if classroom[nr][nc] in students[classroom[r][c]-1]:
                    like += 1
        if like == 0:
            total_sum += 0
        else:
            total_sum += (10 ** (like-1))

print(total_sum)