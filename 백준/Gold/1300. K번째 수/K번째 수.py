#참고 : https://hongcoding.tistory.com/13
# 문제 이해가 어려워서 풀이 참고
# 사용자로부터 정수를 입력 받아 변수 n에 저장합니다.
n = int(input())

# 사용자로부터 또 다른 정수를 입력 받아 변수 k에 저장합니다.
k = int(input())

# 이진 탐색 함수를 정의합니다.
def binary_search(target, start, end):
    while(start <= end):
        # 현재 범위의 중간값을 계산합니다.
        mid = (start + end) // 2

        # cnt 변수를 초기화합니다.
        cnt = 0

        # 1부터 n까지의 수에 대해 반복합니다.
        for i in range(1, n+1):
            # mid를 i로 나눈 몫과 n 중 작은 값을 cnt에 더합니다.
            cnt += min(mid // i, n)

        # cnt가 목표 값(target) 이상이면, 범위의 끝을 mid-1로 갱신합니다.
        if cnt >= target:
            end = mid - 1
        # 그렇지 않으면, 범위의 시작을 mid+1로 갱신합니다.
        else:
            start = mid + 1

    # while 루프를 벗어날 때, start에는 목표 값 이상의 최소 mid 값이 저장됩니다.
    return start

# binary_search 함수를 호출하고 결과를 출력합니다.
print(binary_search(k, 1, n * n))