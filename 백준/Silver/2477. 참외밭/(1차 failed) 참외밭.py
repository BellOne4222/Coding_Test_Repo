yellow_melon = int(input())

east = []
west = []
south = []
north = []

for i in range(6):
    direction, m = map(int,input().split())
    if direction == 1:
        west.append(m)
    elif direction == 2:
        north.append(m)
    elif direction == 3:
        south.append(m)
    else:
        east.append(m)

# [50] [60, 100] [30, 20] [160] 동,서,남,북 순

whole_num = east + west + south + north # [50, 60, 100, 30, 20, 160]

whole = []

whole.append(east)
whole.append(west)
whole.append(south)
whole.append(north)

top = max(whole_num)
side = 0
for k in range(len(whole)):
    if len(whole[k]) == 1 and sum(whole[k]) != top:
        side = whole[k][0]
        break

whole_square = top * side

part_square_top = 0
part_square_side = 0

for j in range(4):
    if len(whole[j]) == 2 and sum(whole[j]) != top:
        if whole[j][0] > whole[j][1]:
            part_square_side = whole[j][1]
        elif whole[j][0] < whole[j][1]:
            part_square_side = whole[j][0]
        else:
            part_square_side = whole[j][0]
    elif len(whole[j]) == 2 and sum(whole[j]) == top:
        if whole[j][0] > whole[j][1]:
            part_square_top = whole[j][1]
        elif whole[j][0] < whole[j][1]:
            part_square_top = whole[j][0]
        else:
            part_square_top = whole[j][0]

part_square = part_square_top * part_square_side

result = (whole_square - part_square) * yellow_melon

print(result)