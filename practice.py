t = int(input())

n = int(input())

diary_1 = list(map(int,input().split()))

m = int(input())

diary_2 = list(map(int,input().split()))

for i in range(m):
    if diary_2[i] in diary_1:
        print(1)
    else:
        print(0)