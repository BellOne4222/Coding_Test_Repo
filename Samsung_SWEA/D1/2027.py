# 2027 대각선 출력하기

for i in range(5): # 2중 for문 이용해서 반복 횟수가 같을 때 #출력, 나머지는 + 출력하는 방식
    for j in range(5):
        if i == j:
            print("#",end ="")
        else:
            print("+",end ="")
    print()