# 이것이 취업을 위한 코딩테스트다 p.381 못생긴수

n = 10
ugly = [0] * n # 못생긴 수를 담기위한 dp 테이블
ugly[0] = 1 # 첫 번째 못생긴 수는 1

# 2배, 3배, 5배를 위한 인덱스
idx2 = idx3 = idx5 = 0
# 처음에 곱셈값을 초기화
next2, next3, next5 = 2,3,5

# 1부터 n까지 못생긴 수를 찾기
for i in range(1,n):
    # 가능한 곱셈 결과 중에서 가장 작은 수를 선택
    ugly[i] = min(next2, next3, next5)

    # 인덱스에 따라서 곱셈 결과를 증가
    if ugly[i] == next2:
        idx2 += 1
        next2 = ugly[idx2] * 2
    if ugly[i] == next3:
        idx3 += 1
        next3 = ugly[idx3] * 3
    if ugly[i] == next5:
        idx5 += 1
        next5 = ugly[idx5] * 5

print(ugly[n-1])
    