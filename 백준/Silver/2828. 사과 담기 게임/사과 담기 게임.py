n,m = map(int,input().split())

apple = int(input())

basket = [j+1 for j in range(m)]

move = 0

for i in range(apple):
    drop = int(input())
    if drop in basket:
        continue
    else:
        while True:
            if basket[-1] < drop:
                basket = [k + 1 for k in basket]
                move += 1
            else:
                basket = [k - 1 for k in basket]
                move += 1
            
            if drop in basket:
                break
print(move)