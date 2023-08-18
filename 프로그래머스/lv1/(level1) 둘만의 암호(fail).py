from string import ascii_lowercase # 알파벳 리스트 사용하기 위한 라이브러리

def solution(s, skip, index):
    alphabet = list(ascii_lowercase) # 알파벳 리스트 출력, 대문자 리스트는 ascii_uppercase
    for i in alphabet: # 알파벳 리스트에서 skip에 있는 알파벳들을 빼서 사용할 수 있는 알파벳 리스트 생성
        if i in skip:
            alphabet.remove(i)
    alphabet_index = [j for j in range(1, len(alphabet)+1)]
    alphabet_to_index = dict(zip(alphabet, alphabet_index))
    index_to_alphabet = dict(zip(alphabet_index, alphabet))
    
    result = ''
    for k in s:
        change = 0
        change = (int(alphabet_to_index[k]) + index) 
        if change > len(alphabet_index):
            change = (change - len(alphabet_index)) % len(alphabet) 
            print(change)
        result += index_to_alphabet[change]
    
    return result
        
        
        
            
    