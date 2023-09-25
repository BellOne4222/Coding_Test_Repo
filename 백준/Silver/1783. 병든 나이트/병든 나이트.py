# 그리디

n, m = map(int, input().split())

if n == 1:
    print(1)

elif n == 2:
    print(min(4, (m+1)//2))
elif m <= 6: # m이 6이하
    print(min(4, m))
else: # n이 3이상이고 m이 7 이상일 때
    print(m-2)

