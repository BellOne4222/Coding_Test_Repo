# 참고 : https://codingwonny.tistory.com/m/311

n, m = map(int, input().split())  # n: 작업의 개수, m: 기계의 대수
time = list(map(int, input().split()))  # 각 작업의 소요 시간 리스트

start = max(time)  # 이진 탐색의 시작 범위를 작업 중 가장 오래 걸리는 작업의 시간으로 설정
end = sum(time)    # 이진 탐색의 끝 범위를 모든 작업 시간의 합으로 설정

while start <= end:  # 시작 범위가 끝 범위를 넘지 않는 동안 반복
    mid = (start + end) // 2  # 중간값 계산

    total = 0  # 각 기계에 할당된 시간을 누적하는 변수
    count = 1  # 현재까지 사용한 기계의 수를 나타내는 변수

    for t in time:
        if total + t > mid:  # 현재 기계에 작업을 할당했을 때, 할당된 시간이 중간값을 넘어간다면
            count += 1  # 다음 기계로 작업을 할당하고
            total = 0    # 할당된 시간을 초기화
        total += t  # 현재 기계에 작업을 할당

    if count <= m:  # 현재 설정된 중간값으로 모든 작업을 할당했을 때 사용한 기계 수가 주어진 대수 이하라면
        ans = mid   # 가능한 최대 시간을 업데이트하고
        end = mid - 1  # 더 작은 중간값을 찾기 위해 끝 범위를 줄임
    else:
        start = mid + 1  # 그렇지 않으면 시작 범위를 늘려서 다시 탐색

print(ans)  # 가능한 최대 시간을 출력