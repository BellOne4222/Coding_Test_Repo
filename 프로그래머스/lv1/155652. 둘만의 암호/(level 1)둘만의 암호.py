def solution(s, skip, index):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    allow_alphabet = ''
    for i in alphabet:
        if i not in skip: # skip에 있는 알파벳을 제외한 알파벳 문자열 만들어주기
            allow_alphabet += i

    result = ''
    for k in s:
        before_index = allow_alphabet.index(k)
        after_index = (before_index + index) % len(allow_alphabet) # 알파벳 리스트의 길이로 나눈 나머지를 통해서 z의 인덱스 보다 크면(z의 인덱스를 넘어갈 경우) 다시 a부터 시작할 수 있게 구현
        result += allow_alphabet[after_index]
    return result
        
        
        
            
    