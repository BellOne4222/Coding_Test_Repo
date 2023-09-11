# n = int(input())
n = 4

road = [2, 3, 1]
# for _ in range(n-1):
#     road = list(map(int,input().split()))
    

city = [5, 2, 4, 1]
# for _ in range(n):
#     city = list(map(int,input().split()))

oil_price = city[0]
distance = road[0] * oil_price  
    
for i in range(1,n-1):
    if city[i] < oil_price:
        oil_price = city[i]
        distance += (road[i] * oil_price)
    else:
        distance += (road[i] * oil_price)
print(distance)