import sys

n = int(sys.stdin.readline())

meetings = []

for _ in range(n):
    meeting = list(map(int, sys.stdin.readline().split()))
    meetings.append(meeting)

# 회의의 시작 시간을 기준으로 정렬합니다.
meetings.sort(key=lambda x: x[0])

dp_table = [0] * n  # 각 회의까지의 최대 인원을 저장할 DP 테이블

for i in range(n):
    start, end, person = meetings[i][0], meetings[i][1], meetings[i][2]
    dp_table[i] = person  # 초기값으로 각 회의의 인원을 넣어줍니다.

    for j in range(i):
        if meetings[j][1] <= start:  # 이전 회의가 현재 회의 시작 시간보다 끝나는 시간이 작거나 같은 경우
            dp_table[i] = max(dp_table[i], dp_table[j] + person)  # 현재 회의까지의 최대 인원을 구합니다.

print(max(dp_table))  # 최대 인원을 출력합니다.