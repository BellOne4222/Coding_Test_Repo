import sys

n = int(sys.stdin.readline())

problems = {} # 난이도 : 문제번호
reverse_problems = {} # 문제번호 : 난이도
problems_levels = []

for _ in range(n):
    p, l = map(int, sys.stdin.readline().split()) # 문제 번호, 난이도
    if l in problems:
        problems[l].append(p)
    else:
        problems[l] = [p]
    reverse_problems[p] = l
    problems_levels.append(l)

m = int(sys.stdin.readline())

for _ in range(m):
    operation = list(sys.stdin.readline().split())
    # 추천 문제 리스트에 난이도가 L인 문제 번호 P를 추가한다.
    if operation[0] == "add":
        if int(operation[2]) in problems:
            problems[int(operation[2])].append(int(operation[1]))
        else:
            problems[int(operation[2])] = [int(operation[1])]
        reverse_problems[int(operation[1])] = int(operation[2])
        problems_levels.append(int(operation[2]))
    elif operation[0] == "recommend":
        # 추천 문제 리스트에서 가장 어려운 문제의 번호를 출력한다.
        if operation[1] == "1":
            find = max(problems_levels)
            print(max(problems[find]))
        # x == -1인 경우 추천 문제 리스트에서 가장 쉬운 문제의 번호를 출력한다.
        else:
            find = min(problems_levels)
            print(min(problems[find]))  
    # solved인 경우 추천 문제 리스트에서 문제 번호 P를 제거한다.
    else:
        find = reverse_problems[int(operation[1])] # find = p의 난이도
        problems[find].remove(int(operation[1]))   
        del reverse_problems[int(operation[1])] # 문제번호에 해당하는 난이도 제거
        problems_levels.remove(find) # 문제 번호에 해당하는 난이도 제거