n = int(input())

cost = 1000 - n

coin = 0

coins = [500,100,50,10,5,1]
idx = 0

while True:
    if cost >= coins[idx]:
        coin += cost//coins[idx]
        cost %= coins[idx]
        idx += 1
    else:
        idx += 1
    if cost == 0:
        break
        
print(coin)
    