king, stone, move = input().split()
# king, stone, move = "C1", "B1", "3"
# locations = ["L","T","LB"]
king = list(king)
stone = list(stone)
move = int(move)
# ['A', '1'] ['A', '2'] 5

col_alpha = ["A","B","C","D","E","F","G","H"]
col = dict() # num to alpha
for j in range(1,9):
    col[j] = col_alpha[j-1]
col_rev = {v:k for k,v in col.items()} # alpha to num
row = [i for i in range(1,9)]
# {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}
# {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}

moving = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}

for i in range(move):
    locate = input()
    # locate = locations[i]
    nx = col_rev[king[0]] + moving[locate][0]
    ny = int(king[1]) + moving[locate][1]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        if col[nx] == stone[0] and ny == int(stone[1]):
            s_nx = col_rev[stone[0]] + moving[locate][0]
            s_ny = int(stone[1]) + moving[locate][1]
            if 1 <= s_nx <= 8 and 1 <= s_ny <= 8:
                king[0], king[1] = col[nx], ny
                stone[0], stone[1] = col[s_nx], s_ny
        else:
            king[0], king[1] = col[nx], ny

king[0] = str(king[0])
king[1] = str(king[1])

stone[0] = str(stone[0])
stone[1] = str(stone[1])

print(''.join(king))
print(''.join(stone))