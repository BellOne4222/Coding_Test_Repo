# 6190. 정곤이의 단조 증가하는 수

# 정곤이는 자신이 엄청난 수학자임을 증명하기 위해, 어떤 규칙 만족하는 수를 찾아보기로 했다.

# 그 규칙은 단조 증가하는 수인데, 각 숫자의 자릿수가 단순하게 증가하는 수를 말한다.

# 어떤 k자리 수 X = d1d2…dk 가 d1 ≤ d2 ≤ … ≤ dk 를 만족하면 단조 증가하는 수이다.

# 예를 들어 111566, 233359는 단조 증가하는 수이고, 12343, 999888은 단조 증가하는 수가 아니다.

# 양의 정수 N 개 A1, …, AN이 주어진다.

#  1 ≤ i < j ≤ N 인 두 i, j에 대해, Ai x Aj값이 단조 증가하는 수인 것들을 구하고 그 중의 최댓값을 출력하는 프로그램을 작성하라.


# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1 ≤N ≤ 1,000) 이 주어진다.

# 두 번째 줄에는 N개의 정수 A1, …, AN(1 ≤ Ai ≤ 30,000) 이 공백 하나로 구분되어 주어진다.


# [출력]

# 각 테스트 케이스마다 단조 증가하는 수인 Ai x Aj중에서 그 최댓값을 출력한다.

# 만약 Ai x Aj중에서 단조 증가하는 수가 없다면 -1을 출력한다.

# 내가 쓴 답

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    danjo = []

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            A = nums[i] * nums[j]
            a = []
            for k in str(A):
                a.append(k)
            cnt = 0
            for l in range(len(a)):
                if a[l] <= a[l+1]:
                    cnt += 1
                if cnt == len(a) - 1:
                    ans = ''.join(a)
                    danjo.append(ans)
    
    print("#{} {}".format(test_case, max(danjo)))

# 참고 코드

T = int(input())
 
for test_case in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    max_result = -1 # 단조 값 곱의 최대값
    for i in range(N - 1): # N개에서 2개 뽑아서 하는 조합, 여기 범위에서 몇개 뽑는지 결정(N-2까지 이므로 2개)
        for j in range(i + 1, N):
            check = str(nums[i] * nums[j]) # 단조값 곱
            for k in range(len(check) - 1): # 두 개씩 검사하니까 범위를 전체 - 검사하는 숫자 수
                if check[k] > check[k + 1]: # 단조가 아니면 반복 종료
                    break
            else:
                if max_result < int(check): # 곱의 최댓값을 갱신
                    max_result = int(check)
    print("#{} {}".format(test_case+1, max_result))



            


