T=1
for t in range(T):
    N=3
    d=[]
    while len(d)<N:
        d.extend(list(input().split()))
    d=''.join(d)
    print(d)
    for i in range(int(d)):
        if str(i) not in d:
            print(f'#{t+1} {i}')
            break