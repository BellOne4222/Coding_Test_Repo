# pypy3에서는 통과되지만 python3에서는 시간초과

import sys

n = int(sys.stdin.readline())  # 입력으로 문제의 개수 n을 받습니다.

problems = {}  # 난이도를 키로, 해당 난이도의 문제 번호들을 값으로 가지는 사전
reverse_problems = {}  # 문제 번호를 키로, 해당 문제의 난이도를 값으로 가지는 사전
problems_levels = []  # 모든 문제의 난이도를 저장하는 리스트

# n번 반복하여 문제의 정보를 입력받고 저장합니다.
for _ in range(n):
    p, l = map(int, sys.stdin.readline().split())  # 문제 번호와 난이도를 입력으로 받습니다.
    
    # 난이도를 키로 가지는 problems 사전에 해당 문제 번호를 추가합니다.
    if l in problems:
        problems[l].append(p)
    else:
        problems[l] = [p]
    
    # reverse_problems 사전에 해당 문제 번호와 난이도를 추가합니다.
    reverse_problems[p] = l
    
    # problems_levels 리스트에 해당 난이도를 추가합니다.
    problems_levels.append(l)

m = int(sys.stdin.readline())  # 입력으로 수행할 작업의 개수 m을 받습니다.

# m번 반복하여 수행할 작업을 처리합니다.
for _ in range(m):
    operation = list(sys.stdin.readline().split())  # 공백으로 분리된 작업 정보를 입력으로 받습니다.
    
    if operation[0] == "add":
        # "add" 작업: 난이도가 L인 문제 번호 P를 추가합니다.
        if int(operation[2]) in problems:
            problems[int(operation[2])].append(int(operation[1]))
        else:
            problems[int(operation[2])] = [int(operation[1])]
        
        # reverse_problems 사전과 problems_levels 리스트를 업데이트합니다.
        reverse_problems[int(operation[1])] = int(operation[2])
        problems_levels.append(int(operation[2]))
    
    elif operation[0] == "recommend":
        # "recommend" 작업: 가장 어려운 또는 쉬운 문제의 번호를 출력합니다.
        if operation[1] == "1":
            # 가장 어려운 문제를 출력
            find = max(problems_levels)
            print(max(problems[find]))
        else:
            # 가장 쉬운 문제를 출력
            find = min(problems_levels)
            print(min(problems[find])) 
    
    else:
        # "solved" 작업: 문제 번호 P를 추천 문제 리스트에서 제거합니다.
        find = reverse_problems[int(operation[1])]  # 문제 P의 난이도를 찾습니다.
        problems[find].remove(int(operation[1]))  # 추천 문제 리스트에서 제거
        del reverse_problems[int(operation[1])]  # 문제 번호에 해당하는 난이도를 제거
        problems_levels.remove(find)  # 문제 번호에 해당하는 난이도를 제거