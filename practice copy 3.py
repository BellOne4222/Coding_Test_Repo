#동1 서2 남3 북4
whole = [] # 방향, 거리 저장 리스트
top = [] # 가로 길이들 리스트
side = [] # 세로 길이들 리스트
part = [] # B의 가로 세로 길이

n = int(input())

for i in range(6):
    direction,m = map(int,input().split()) # 방향, 거리 입력
    whole.append([direction,m])
    if whole[i][0] == 3 or whole[i][0] == 4: # 세로 저장
        top.append(whole[i][1])
    if whole[i][0] == 1 or whole[i][0] == 2: # 가로 저장
        side.append(whole[i][1])

for i in range(6):
    if whole[i][0] == whole[(i+2)%6][0]:
        part.append(whole[(i+1)%6][1])

yellow_melon = ((max(top)*max(side)) - (part[0]*part[1])) * n
print(yellow_melon)