# 입력으로 킹(K), 돌(stone), 이동 횟수(move)를 받습니다.
king, stone, move = input().split()

# 킹(K)과 돌(stone)의 위치를 문자열로부터 리스트로 변환하고, 이동 횟수(move)를 정수로 변환합니다.
king = list(king)   # 킹의 초기 위치 ['C', '1']
stone = list(stone) # 돌의 초기 위치 ['B', '1']
move = int(move)    # 이동 횟수 3

# 체스판 열의 알파벳 표기와 숫자 표기를 정의합니다.
col_alpha = ["A", "B", "C", "D", "E", "F", "G", "H"]
col = dict()  # 숫자를 알파벳으로 변환하는 딕셔너리
for j in range(1, 9):
    col[j] = col_alpha[j - 1]
col_rev = {v: k for k, v in col.items()}  # 알파벳을 숫자로 변환하는 딕셔너리
row = [i for i in range(1, 9)]

# 이동 방향을 정의하는 딕셔너리를 생성합니다.
moving = {
    'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1],
    'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]
}

# 주어진 이동 횟수만큼 반복하여 이동합니다.
for i in range(move):
    locate = input()  # 이동 방향을 입력 받습니다.
    nx = col_rev[king[0]] + moving[locate][0]  # 킹의 새로운 x 좌표 계산
    ny = int(king[1]) + moving[locate][1]      # 킹의 새로운 y 좌표 계산

    # 새로운 위치가 체스판 내에 있으면 이동합니다.
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        # 킹의 새로운 위치가 돌의 위치와 같다면
        if col[nx] == stone[0] and ny == int(stone[1]):
            s_nx = col_rev[stone[0]] + moving[locate][0]  # 돌의 새로운 x 좌표 계산
            s_ny = int(stone[1]) + moving[locate][1]       # 돌의 새로운 y 좌표 계산

            # 새로운 돌의 위치가 체스판 내에 있으면 킹과 돌을 함께 이동시킵니다.
            if 1 <= s_nx <= 8 and 1 <= s_ny <= 8:
                king[0], king[1] = col[nx], ny
                stone[0], stone[1] = col[s_nx], s_ny
        else:
            king[0], king[1] = col[nx], ny

# 킹과 돌의 최종 위치를 문자열로 변환합니다.
king[0] = str(king[0])
king[1] = str(king[1])
stone[0] = str(stone[0])
stone[1] = str(stone[1])

# 최종 킹과 돌의 위치를 출력합니다.
print(''.join(king))
print(''.join(stone))