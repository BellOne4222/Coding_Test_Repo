import sys

M,N=map(int,input().split())

L=[[1 for j in range(M)] for i in range(M)]
day=[0 for i in range(2*M-1)]



for _ in range(N):
    z,o,t=map(int,sys.stdin.readline().rstrip().split())
    for i in range(z,z+o):
        day[i]+=1
    for i in range(z+o,2*M-1):
        day[i]+=2

#왼쪽꺼
for i in range(M-1,-1,-1):
    L[i][0]+=day[M-1-i]
#위쪽
for j in range(1,M):
    L[0][j]+=day[M-1+j]

#1열 이후라인
for j in range(1,M):
    for i in range(1,M):
        L[i][j]=L[i-1][j]

for i in L:
    print(*i)