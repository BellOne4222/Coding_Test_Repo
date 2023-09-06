from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    grade = deque()
    for _ in range(n):
        grade.append(list(map(int,input().split())))
    end = grade[-1]
    while True:
        standard = grade.popleft()
        for l in grade:
            if standard[0] < l[0] and standard[1] < l[1]:
                del grade[l]
        grade.append(standard)
                
        if standard == end:
            break
    print(len(grade))