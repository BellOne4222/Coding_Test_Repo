# 5431. 민석이의 과제 체크하기

# 민석이는 교수가 되었고, 이번에 처음으로 맡은 과목에 수강생이 N명이다.

# 민석이는 처음으로 과제를 내었다.

# 그리고 제출한 사람의 목록을 받았다.

# 수강생들은 1번에서 N번까지 번호가 매겨져 있고, 어떤 번호의 사람이 제출했는지에 대한 목록을 받은 것이다.

# 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력하는 프로그램을 작성하라.


# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 수강생의 수를 나타내는 정수 N(2≤N≤100)과 과제를 제출한 사람의 수를 나타내는 정수 K(1≤K≤N)가 공백으로 구분되어 주어진다.

# 두 번째 줄에는 과제를 제출한 사람의 번호 K개가 공백으로 구분되어 주어진다. 번호는 1이상 N이하의 정수이며 같은 번호가 두 번 이상 주어지는 경우는 없다.


# [출력]

# 각 테스트 케이스마다 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력한다.

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    
    did = list(map(int, input().split())) # 한 사람 번호
    did.sort() # 한 사람들 번호 정렬

    people = [i for i in range(1, N+1)] # n명의 번호 리스트 생성
    did_not = []
    for j in people: # 안한 사람들 번호를 안한 사람들 리스트에 넣기
        if j not in did:
            did_not.append(j)
    did_not.sort()
    did_not = list(map(str, did_not))
    did_not = ' '.join(did_not)
    
    print("#{} {}".format(test_case, did_not))

