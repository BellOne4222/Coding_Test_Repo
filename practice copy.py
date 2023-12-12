import sys

t = int(sys.stdin.readline())  # 테스트 케이스의 개수를 입력 받습니다.

for _ in range(t):  # 각 테스트 케이스를 처리합니다.
    n = int(sys.stdin.readline())  # n값을 입력 받습니다. n은 스티커의 열 개수입니다.
    
    sticker_table = []  # 스티커의 점수를 저장할 테이블을 초기화합니다.
    for _ in range(2):  # 스티커는 2행 n열로 주어집니다.
        stickers = list(map(int, sys.stdin.readline().split()))  # 스티커의 점수를 입력 받습니다.
        sticker_table.append(stickers)  # 입력받은 스티커의 점수를 테이블에 추가합니다.
    
    dp_table = [[0 for _ in range(len(sticker_table[0])+1)] for _ in range(3)] 
    # DP를 위한 테이블을 생성합니다. 스티커를 붙이는 경우의 수 중, 지그재그가 아닌 열을 건너 뛰는 경우의 수를 위해서 행과 열 하나씩 더 추가해 초기화합니다.
    
    dp_table[1][1] = sticker_table[0][0]  # 초기값이 없기 때문에 sticker_table의 첫 번째 열 값을 dp_table에 추가합니다.
    dp_table[2][1] = sticker_table[1][0]  # 두 번째 행의 첫 번째 열 값을 dp_table에 추가합니다.
    
    for i in range(2, n+1):  # 이전 열의 최대값 또는 이전 이전 열의 최대값을 비교하여 현재 스티커 점수와 합산하여 dp_table을 초기화합니다(열마다 최대값을 추가합니다).
        dp_table[0][i-1] = max(dp_table[1][i-2], dp_table[2][i-2]) 
        dp_table[1][i] = max(dp_table[0][i-1], dp_table[2][i-1]) + sticker_table[0][i-1]
        dp_table[2][i] = max(dp_table[0][i-1], dp_table[1][i-1]) + sticker_table[1][i-1]
    
    # dp_table은 스티커를 선택하는 경우의 점수를 담은 테이블입니다.
    # [0, 0, 50, 100, 200, 0], 
    # [0, 50, 40, 200, 140, 250], 
    # [0, 30, 100, 120, 210, 260]
    
    # 마지막 열에서 스티커 점수의 최대값을 출력합니다.
    print(max(dp_table[1][n], dp_table[2][n]))  # 스티커 점수 중에서 최대값을 출력합니다.