import sys

n = int(sys.stdin.readline())  # 수열 A의 크기 N을 입력 받습니다.
numbers = list(map(int, sys.stdin.readline().split()))  # 수열 A를 이루는 숫자들을 리스트에 저장합니다.

dp_table = [1] * n  # 각 위치에서의 가장 긴 감소하는 부분 수열의 길이를 저장할 DP 테이블을 초기화합니다.

for i in range(1, n):  # 두 번째부터 마지막 숫자까지 탐색합니다.
    for j in range(i):  # i 이전의 위치를 확인합니다.
        if numbers[j] > numbers[i]:  # 만약 이전 위치의 숫자가 현재 위치의 숫자보다 크다면,
            dp_table[i] = max(dp_table[i], dp_table[j] + 1)  # 해당 위치에서의 부분 수열 길이를 업데이트합니다.

print(max(dp_table))  # 가장 긴 감소하는 부분 수열의 최대 길이를 출력합니다.