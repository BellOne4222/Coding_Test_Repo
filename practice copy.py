n = int(input())
building = 0

heights = []
for i in range(n):
    x,y = map(int,input().split())
    heights.append(y)
heights.append(0)

cnts = []
cnts.append(0)
for h in heights:
    height = h
    while cnts[-1] > h:
        if cnts[-1] != height:
            building += 1
            height = cnts[-1]
        cnts.pop()
    cnts.append(h)   
print(building)