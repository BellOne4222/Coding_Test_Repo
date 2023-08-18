# 각 종류의 옷을 입을지 안입을지로 나누어서 생각

def solution(clothes):
    clothes_dict = dict()
    for name, kind in clothes:
        if kind in clothes_dict: # 각 종류의 옷 : 그 종류의 옷 개수 만큼 딕셔너리 생성
            clothes_dict[kind] += 1
        else:
            clothes_dict[kind] = 1
    
    # clothes_dict = {'headgear': 2, 'eyewear': 1}
    
    case = 1
    for kind in clothes_dict.keys():
        case *= clothes_dict[kind] + 1 # 1은 각 종류의 옷 중 아무것도 안 입는 경우 headgear에 해당하는 의상: yellow_hat, green_turban -> 각각 쓰는 경우(2) + 아무 것도 안쓰는 경우(1) = 3
        # 각 종류의 옷 개수에 1을 더한걸 case에 곱하면 옷을 입는 모든 경우의 수
    
    case -= 1 # 코니는 하루에 최소 한 개의 의상은 입으므로 아무것도 안 입은 경우 빼기
    return case


    
    
    
            

            
        
        
            
        