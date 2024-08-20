import sys 

# 첫 번째 줄에서 수열 A의 크기 N을 입력받습니다.
n = int(sys.stdin.readline())

# 두 번째 줄에서 수열 A의 요소들을 입력받아 리스트 a에 저장합니다.
# 입력된 수열은 공백으로 구분되어 있으므로 split() 함수를 사용하고,
# map()을 통해 각 요소를 정수형으로 변환합니다.
a = list(map(int, sys.stdin.readline().split()))

# dp_table 배열을 1로 초기화합니다.
# dp_table[i]는 수열 a[i]를 마지막 원소로 가지는 가장 긴 감소하는 부분 수열의 길이를 저장합니다.
# 여기서 [1] * 1001은 초기값을 모두 1로 설정하고, 충분히 큰 크기(1001)를 가지는 배열을 만듭니다.
dp_table = [1] * 1001

# 이중 루프를 사용하여 각 수열의 원소에 대해 감소하는 부분 수열을 찾습니다.
for i in range(n):
    # 현재 위치 i보다 앞의 모든 위치 j를 순회하며
    # a[j]가 a[i]보다 크면, a[j]를 끝으로 하는 감소하는 부분 수열에 a[i]를 추가할 수 있습니다.
    for j in range(i):
        if a[i] < a[j]:
            # dp_table[i]를 갱신하여, 현재 원소를 포함한 감소하는 부분 수열의 최대 길이를 저장합니다.
            dp_table[i] = max(dp_table[i], dp_table[j] + 1)

# dp_table 배열에서 가장 큰 값을 출력합니다.
# 이는 전체 수열에서 가능한 가장 긴 감소하는 부분 수열의 길이를 의미합니다.
print(max(dp_table))
