def solution(numbers, hand):
    key_pad = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]] # 키패드를 2차원 배열로 생성
    
    left_hand_start = key_pad[3][0] # 왼손 시작 좌표
    right_hand_start = key_pad[3][2] # 오른손 시작 좌표
    
    left_only = [1,4,7]
    right_only = [3,6,9]
    
    if numbers[0] in left_only:
        current = left_hand_start
    elif numbers[0] in right_only:
        current = right_hand_start
    else:
        if hand == "left":
            current = left_hand_start
        elif hand == "right":
            current = right_hand_start
    left_current = 0
    right_current = 0
    result = ''
    for number in numbers:
        if number in left_only:
            result += 'L'
            left_current = number
        elif number in right_only:
            result += 'R'
            right_current = number
        else: # 왼손 거리와 오른손 거리가 1로 같으므로, 오른손으로 5를 누릅니다. 경우 구현 실패...
            if abs(number - left_current) > abs(number - right_current):
                result += 'R'
                right_current = number
            elif abs(number - left_current) < abs(number - right_current):
                result += 'L'
                left_current = number
            else:
                if hand == "left":
                    result += 'L'
                    left_current = number
                elif hand == "right":
                    result += 'R'
                    right_current = number  
        print(result)
    return result
            
            
            
    
            
            
    
    