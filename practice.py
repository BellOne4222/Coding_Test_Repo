n = int(input())

building = 0
heights = []

for i in range(n):
    x,y = map(int,input().split(" "))
    if y not in heights:
        heights.append(y)
        building += 1
    elif y == 0:
        heights = []
print(building)