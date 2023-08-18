# https://bladejun.tistory.com/115
# 위 블로그에서 딕셔너리에 좌표값을 넣는 아이디어로 코드 수정해서 해결

def solution(numbers, hand):
    key_pad = {1: [0, 0], 2: [0, 1], 3: [0, 2], # 키패드를 숫자를 key, 그에 해당하는 좌표를 value로 딕셔너리 생성 
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    
    left_hand_location = key_pad['*'] # 왼손 시작 좌표
    right_hand_location = key_pad['#'] # 오른손 시작 좌표
    
    left_only = [1,4,7] # 왼손만 사용가능 한 곳
    right_only = [3,6,9] # 오른손만 사용가능 한 곳
    
    result = ''
    for number in numbers:
        current = key_pad[number] # 현재 위치 좌표 
        if number in left_only:
            result += 'L'
            left_hand_location  = current
        elif number in right_only:
            result += 'R'
            right_hand_location = current
        else:
            left_to_number = 0 # 왼쪽 위치에서 누르려는 버튼까지의 거리
            right_to_number = 0 # 오른쪽 위치에서 누르려는 버튼까지의 거리

            for i, j, k in zip(left_hand_location, right_hand_location, current): # 거리 계산
                left_to_number += abs(i-k)
                right_to_number += abs(j-k)

            # 왼손이 더 가까운 경우
            if left_to_number < right_to_number:
                result += 'L'
                left_hand_location = current
                
            # 오른손이 더 가까운 경우
            elif left_to_number > right_to_number:
                result += 'R'
                right_hand_location = current

            # 두 거리가 같은 경우
            else:
                # 왼손잡이 경우
                if hand == 'left':
                    result += 'L'
                    left_hand_location = current
                    
                # 오른손잡이 경우
                else:
                    result += 'R'
                    right_hand_location = current
    return result
            
            
            
    
            
            
    
    