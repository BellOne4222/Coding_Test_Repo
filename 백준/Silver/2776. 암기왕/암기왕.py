t = int(input())

for _ in range(t):
    n = int(input())

    diary_1 = set(map(int,input().split()))

    m = int(input())

    diary_2 = list(map(int,input().split()))

    for i in range(len(diary_2)):
        if diary_2[i] in diary_1:
            print(1)
        else:
            print(0)
