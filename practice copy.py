import sys
input = sys.stdin.readline  # 입력을 더 빠르게 받기 위해 sys.stdin.readline 사용
N, M, H = map(int, input().split())  # 학생 수(N), 최대 블록 수(M), 탑의 목표 높이(H) 입력
block_list = [[0] + list(map(int, input().split())) for _ in range(N)]  # 각 학생별 블록 높이 입력, 맨 앞에 0 추가(블록을 사용하지 않는 경우 고려)

dp_table = [[0]*(H+1) for _ in range(N+1)]  # dp_table[i][h]: i번째 학생까지 고려했을 때 높이 h를 만들 수 있는 경우의 수
dp_table[0][0] = 1  # 초기 조건, 0번째 학생(사실상 아무도 없는 상태)까지 고려했을 때 높이 0을 만드는 경우의 수는 1

for i in range(N) :  # 모든 학생에 대해 반복
  for h in range(H+1) :  # 가능한 모든 높이에 대해 반복
    if dp_table[i][h] :  # 현재 i번째 학생까지 고려하여 높이 h를 만들 수 있는 경우가 있다면,
      for j in block_list[i] :  # 해당 학생이 가진 모든 블록(높이)에 대해 반복
        if h + j <= H :  # 현재 블록을 추가했을 때 탑의 높이가 H를 넘지 않는다면,
          # dp_table[i+1][h+j]를 업데이트: i+1번째 학생까지 고려한 상태에서 높이 h+j를 만들 수 있는 경우의 수를 증가
          dp_table[i+1][h + j] = (dp_table[i][h] + dp_table[i+1][h + j] )  # 모듈로 연산 적용

print(dp_table[-1][-1] % 10007)  # 모든 학생을 고려한 후, 높이 H를 만들 수 있는 경우의 수 출력, 10007로 나눈 나머지
