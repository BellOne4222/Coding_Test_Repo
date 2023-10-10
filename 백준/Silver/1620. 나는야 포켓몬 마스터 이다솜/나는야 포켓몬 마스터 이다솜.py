import sys

input = sys.stdin.readline

n,m = map(int,input().split())

pocketmon_dic = {}

for i in range(1,n+1):
    name = input().rstrip()
    pocketmon_dic[name] = i
    pocketmon_dic[i] = name


for j in range(m):
    what = input().rstrip()
    if what.isdigit():
        print(pocketmon_dic[int(what)])
    else:
        print(pocketmon_dic[what])
    
