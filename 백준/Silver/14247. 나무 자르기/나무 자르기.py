import sys

# 나무의 개수 n을 입력 받음
n = int(sys.stdin.readline())

# 첫날 나무의 길이들을 리스트 h에 저장
h = list(map(int, sys.stdin.readline().split()))

# 나무가 하루에 자라는 양을 리스트 a에 저장
a = list(map(int, sys.stdin.readline().split()))

# h와 a를 각각 h[i]와 a[i]로 짝을 지어 h를 업데이트 (각각 나무의 초기 길이와 하루 성장량을 하나의 리스트로 묶음)
for i in range(n):
    cur = h[i]
    h[i] = [cur, a[i]]

# 하루 성장량을 기준으로 나무들을 오름차순으로 정렬 (성장량이 작은 나무부터 자르기 위해 정렬)
h.sort(key = lambda x:x[1])

# 첫 번째 나무를 잘라서 얻는 나무의 양을 total에 저장 (첫날 나무는 성장이 없으므로 처음 높이를 더함)
total = h[0][0]

# 첫 번째 나무는 잘라서 0이 되었으므로 높이를 0으로 설정
h[0][0] = 0

# 두 번째 나무부터 n번째 나무까지 잘라서 얻을 수 있는 나무의 양을 계산
for j in range(1, n):
    # 현재 나무의 높이 + (해당 나무가 지금까지 자란 양)을 더함
    # j번째 나무는 j일째에 자르므로 h[j][1] * j만큼 나무가 자라난다.
    total += (h[j][0] + (h[j][1] * j))

# 최종적으로 얻을 수 있는 나무의 양을 출력
print(total)
