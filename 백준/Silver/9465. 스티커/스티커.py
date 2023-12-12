import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    
    sticker_table = []
    for _ in range(2):
        stickers = list(map(int, sys.stdin.readline().split()))
        sticker_table.append(stickers)
    
    dp_table = [[0 for _ in range(len(sticker_table[0])+1)] for _ in range(3)] 
    # 스티커를 붙이는 경우의 수 중, 지그재그가 아닌 열을 건너 뛰는 경우의 수를 위해서 행과 열 하나씩 더 추가 해서 dp_table 초기화
    
    dp_table[1][1] = sticker_table[0][0] # 초기값이 없기 때문에 sticker_table의 첫 번째 열 값을 dp_table에 추가
    dp_table[2][1] = sticker_table[1][0]
    
    for i in range(2,n+1): # 이전 열의 최대값 or 이전 이전 열의 최대값을 비교해서 큰 값을 현재 스티커 점수와 합산하여 dp_table 초기화(열마다 최대값 추가)
        dp_table[0][i-1] = max(dp_table[1][i-2], dp_table[2][i-2]) 
        dp_table[1][i] = max(dp_table[0][i-1], dp_table[2][i-1]) + sticker_table[0][i-1]
        dp_table[2][i] = max(dp_table[0][i-1], dp_table[1][i-1]) + sticker_table[1][i-1]
    
    # dp_table
    # [0, 0, 50, 100, 200, 0], 
    # [0, 50, 40, 200, 140, 250], 
    # [0, 30, 100, 120, 210, 260]
    print(max(dp_table[1][n], dp_table[2][n])) # 260
    