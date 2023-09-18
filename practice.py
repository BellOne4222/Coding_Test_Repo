n = int(input())
m = int(input())

graph = [[0 for _ in range(n)] for _ in range(n)]

# 오른쪽, 아래쪽, 왼쪽, 위쪽 순서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 1은 그래프의 중간점이므로 그래프의 중간 위치를 1로 초기화
x = n // 2
y = n // 2

# 1은 이미 초기화 시켜줬고 다음 값은 2부터 시작
num = 1

# 한 바퀴 돌때마다(달팽이) 반복 횟수가 2씩 증가하기 때문에 반복 횟수를 받을 변수
repeat = 0

graph[x][y] = num

while True:
    for i in range(4):
        for _ in range(repeat):  # 특정 방향으로 한칸씩 이동하며 숫자 입력
            x += dx[i]
            y += dy[i]
            num += 1
            graph[x][y] = num
            if num == m:  # 찾을 번호의 인덱스 저장
                ans = [x+1, y+1]

    if x == y == 0:
        break
    x -= 1
    y -= 1
    repeat += 2

for j in range(n):
    print(*graph[j])
print(*ans)