# 14361. 숫자가 같은 배수


# 자연수 N이 있다. N의 10진법 표기(단, 0으로 시작하지 않도록 표기해야 함)에서 나타나는 숫자들을 재배열하여 N보다 큰 N의 배수(즉 2N, 3N, …, k•N, …) 를 만들 수 있는지 판단하는 프로그램을 작성하라.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스는 하나의 줄로 이루어진다. 각 줄에는 자연수 N (1 ≤N ≤ 106) 이 공백 하나를 사이로 두고 주어진다.
 

# [출력]
# 각 테스트 케이스마다, 주어진 자연수에 나타난 숫자들을 재배열하여 더 큰 배수를 만들 수 있다면 ‘possible’, 불가능하다면 ‘impossible’을 출력한다.

T = int(input())

for test_case in range(1, T+1):
    N = input()
    nums = sorted(list(N))
    res = False # 숫자가 같은지 체크한다
    k = 2
    
    while True:
        # 2부터 곱해서 자릿수 넘어가면 false
        # 곱한 것들을 정렬한 원소가 원래 원소와 같으면 참
        num = int(N) * k # num의 배수 2 ~
        
        # 원래 입력한 숫자의 길이보다, 곱한 결과의 길이가 길다면 자릿수가 늘어난거니까 종료
        if len(str(num)) > len(N):
            break
         # 배수를 문자열로 만들어 리스트로 만든걸 정렬, 그게 원래 숫자와 같으면
        if sorted(list(str(num))) == nums:
            res = True
            break
        k += 1
        
    if res:
        ans = "possible"
    else:
        ans = "impossible"
     
    print("#{} {}".format(test_case, ans))