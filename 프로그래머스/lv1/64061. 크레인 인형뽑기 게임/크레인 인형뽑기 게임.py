def solution(board, moves):
    doll_board = [[] for _ in range(len(board[0]))]  # 0은 빈 공간이므로 0을 없애고 인형만 있는 칸만 냅둬서 인형만 있는 배열로 재생성
    for j in range(len(board)):
        for i in range(len(board[0])):
            if board[i][j] == 0: # 0인 칸은 없애기
                pass
            else:
                doll_board[j].append(board[i][j]) # 인형만 추가
    count = 0 # 인형이 없어진 횟수
    basket = [] # 인형을 넣을 바구니 배열
    for i in range(len(moves)):
        if len(doll_board[moves[i]-1]) == 0: # 각 번호의 열이 비어있을 경우 아무일도 일어나지 않는다고 했으므로 continue 처리
            continue
        else: 
            basket.append(doll_board[moves[i]-1][0]) # moves에 따라 뽑은 인형을 basket에 넣기
            del doll_board[moves[i]-1][0] # 인형 배열에 있는 뽑은 인형 제거
            
        if len(basket) >= 2 and basket[-1] == basket[-2]: # basket배열에 들어온 인형과 바로 전 인형이 같을 경우
            for i in range(2): # 인형 2개를 없애고
                basket.pop()
            count += 1 # 인형이 없어진 횟수 증가
    result = count * 2 # 인형이 터진 횟수 = 인형 뽑은 횟수 * 터진 인형 개수
    
    return result # 인형이 터진 개수 반환
        
        
        
        
        
            
    
    
            
    
        
            
    
        
            
            