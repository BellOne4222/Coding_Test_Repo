# 이것이 취업을 위한 코딩테스트다 p.377 퇴사
n = 7 # 전체 상담 개수

t = [] # 각 상담을 완료하는데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n+1) # [0, 0, 0, 0, 0, 0, 0, 0]
max_value = 0

schedule = [[3,10],[5,20],[1,10],[1,20],[2,15],[4,40],[2,200]]

for i in range(len(schedule)):
    t.append(schedule[i][0])
    p.append(schedule[i][1])
# [3, 5, 1, 1, 2, 4, 2] [10, 20, 10, 20, 15, 40, 200]

# 리스트를 거꾸로 확인
for i in range(n-1, -1, -1):
    time = t[i] + i # 소요시간(날짜 + 상담 걸리는 시간)

    # 상담이 기간안에 끝나는 경우
    if time <= n:
        # 현재까지 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)

