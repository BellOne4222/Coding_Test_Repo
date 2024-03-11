import sys
input = sys.stdin.readline

# 입력 받기: 전구의 수 N, 현재 전구 상태, 목표 전구 상태
n = int(input())
light = list(map(int,input().rstrip("\n")))  # 현재 전구 상태 (0: 켜짐, 1: 꺼짐)
target = list(map(int,input().rstrip("\n")))  # 목표 전구 상태

# 전구 상태를 변경하는 함수
def change(light, target):
    count = 0  # 스위치를 누른 횟수
    for i in range(1, n):
        # 이전 전구 상태가 목표와 일치하면 넘어감 (탐욕적 선택)
        if light[i-1] == target[i-1]:
            continue
        
        # 이전 전구 상태가 목표와 다르면 스위치를 눌러 상태 변경
        count += 1
        for j in range(i-1, i+2):  # i-1, i, i+1 전구 상태 변경
            if j < n:  # 범위 확인
                light[j] = 1 - light[j]  # 상태 변경 (0 ↔ 1)

    # 최종 상태가 목표 상태와 같으면 횟수 반환, 아니면 큰 수(불가능을 나타냄) 반환
    return count if light == target else 1e9

# 첫 번째 스위치를 누르지 않은 경우의 최소 횟수 계산
ans = change(light[:], target)

# 첫 번째 스위치를 누른 경우의 상태 준비
light[0] = 1 - light[0]  # 첫 번째 전구 상태 변경
light[1] = 1 - light[1]  # 두 번째 전구 상태 변경

# 첫 번째 스위치를 누른 경우의 최소 횟수 계산 후, 두 경우 중 최소값 선택
ans = min(ans, change(light[:], target) + 1)

# 결과 출력: 가능한 경우 최소 횟수, 불가능한 경우 -1
print(ans if ans != 1e9 else -1)