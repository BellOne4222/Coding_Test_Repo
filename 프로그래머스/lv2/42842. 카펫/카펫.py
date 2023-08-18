# 갈색 부분 세로길이를 중심 변수로 잡고 관련한 수식들을 여러개 만들어서 방정식의 풀이를 통해 구현

def solution(brown, yellow):
    
    # brown_row = 갈색 부분 가로, brown_col = 갈색 부분 세로, yellow_row = 노란색 부분 가로, yellow_col = 노란색 부분 세로

    # brown_col, brown_row = yellow_col + 2, yellow_row + 2

    # brown + yellow = brown_row * brown_col = (yellow_col + 2) * (yellow_row + 2)

    # yellow = yellow_col * yellow_row = (brown_row - 2) * (brown_col - 2)

    # brown = brown_col + brown_col + brown_row + brown_row - 4(겹치는 부분)
    
    for brown_col in range(1, brown//2 + 1): # brown_col은 가로보다 짧으므로 brown//2 보다 길 수 없다.
        brown_row = (brown - 2*brown_col + 4) // 2 # brown = brown_col + brown_col + brown_row + brown_row - 4(겹치는 부분)의 식 변환
        yellow_col, yellow_row = brown_col - 2, brown_row - 2 # brown_col, brown_row = yellow_col + 2, yellow_row + 2 식 변환
        
        # brown_col, brown_row = yellow_col + 2, yellow_row + 2
        # brown + yellow = brown_row * brown_col = (yellow_col + 2) * (yellow_row + 2) 두 개 식 변환
        if yellow == yellow_col * yellow_row and brown + yellow == brown_row * brown_col:
            return [brown_row, brown_col]
            
        
        
        
    
    