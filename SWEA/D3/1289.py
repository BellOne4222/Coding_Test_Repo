# 1289 원재의 메모리 복구하기

T=int(input())

for test_case in range(1,T+1):
    nums = list(input())
    answer = 0 # 변경 횟수
    compare_nums = list(0 for i in range(len(nums))) # 0으로 채워진 input 리스트와 같은 길이의 리스트 생성해서 비교
    for i in range(len(compare_nums)):
        if int(nums[i]) != compare_nums[i]: # 두 리스트를 비교해보며 리스트[i] 값이 다르면
            for j in range(i , len(compare_nums)):
                compare_nums[j] = int(nums[i]) # 다른 부분을 0으로 변환
            answer += 1 # 변환한 횟수 증가
        else:
            continue

    print("#{} {}".format(test_case, answer))