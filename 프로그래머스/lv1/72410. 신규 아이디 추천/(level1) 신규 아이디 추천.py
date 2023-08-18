def solution(new_id):
    
    # step 1 : 소문자로 변환
    new_id = new_id.lower()
    
    # step 2 : 소문자, "-", "_", "." 제외 특수 문자 제거
    result = ''
    for i in new_id:
        if i.isalnum() or i in '-_.': # isalnum() : 영어 및 숫자이면 true 반환(문자 판별)
            result += i
    
    # step 3 : 마침표 2번 이상 연속된 부분을 하나의 마침표로 변환
    while '..' in result:
        result = result.replace('..', '.')
    
    # step 4 : new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거
    if result[0] == '.':
        result = result[1:] # 첫 번째로 만나는 . 제거
    elif result[-1] == '.':
        result = result[:-1]
        
    # step 5 : new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if len(result) == 0:
        result += 'a'
    
    # step 6 :  new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(result) >= 16:
        result = result[:15]
    if result[-1] == '.':
        result = result[:-1]
    
    # step 7 : new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    
    last = result[-1]
    
    if len(result) <= 2:
        while result:
            if len(result) == 3:
                break
            result += last
        
    
    return result
    
        

    
            