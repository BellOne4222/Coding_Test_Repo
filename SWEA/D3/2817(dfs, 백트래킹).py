# 2817. 부분 수열의 합

# A1, A2, ... , AN의 N개의 자연수가 주어졌을 때, 최소 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수를 구하는 프로그램을 작성하시오.


# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 2개의 자연수 N(1 ≤ N ≤ 20)과 K(1 ≤ K ≤ 1000)가 주어진다.

# 두 번째 줄에는 N개의 자연수 수열 A가 주어진다. 수열의 원소인 N개의 자연수는 공백을 사이에 두고 주어지며, 1 이상 100 이하임이 보장된다.


# [출력]

# 각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 부분 수열의 합이 K가 되는 경우의 수를 출력한다.

# 가능한 모든 경우를 백트래킹으로 정답 도출'

# input 리스트의 숫자들에 인덱스 부여후 해당 숫자를 사용할꺼냐 안할꺼냐 선택하는 문제, 이진 트리(2의 50승 이하는 백트래킹 사용 가능)

def dfs(index, sum_num):
    global case
    if K < sum_num: # 가지치기(k 보다 숫자 합이 더 크면 더이상 진행할 필요없으므로 stop)
        return
    if index == N: # 종료 조건 : 리스트의 인덱스 값이 숫자의 개수(N)와 같아 질때 종료 
        if sum_num == K: # 숫자의 합이 K와 같으면 경우의 수 1 증가
            case += 1
        return
    
    dfs(index+1, sum_num + nums[index]) # 배열의 다음 숫자를 더하는 경우
    dfs(index+1, sum_num) # 배열의 다음 숫자를 안더하는 경우


T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    case = 0 # 경우의 수
    dfs(0,0)
    
    print("#{} {}".format(test_case, case))
    
    
                
    
                