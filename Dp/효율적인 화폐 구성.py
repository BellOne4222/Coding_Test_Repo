# 이것이 취업을 위한 코딩테스트다 p226 효율적인 화폐 구성
# 바텀업 사용

n,m = map(int, input().split())

# N개의 화폐 단위 정보를 입력 받기
array = []
for i in range(n):
    array.append(int(input()))

# 10001은 10000까지 만들 수 있어서 절대 만들 수 없는 10001로 리스트 초기화
d = [10001] * (m+1)

d[0] = 0

for i in range(n):
    for j in range(array[i], m+1):
        # (i-k)원을 만드는 방법이 존재하는 경우
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
