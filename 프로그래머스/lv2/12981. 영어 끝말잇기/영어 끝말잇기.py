def solution(n, words):
    word = [words[0]] # 먼저 끝말잇기 첫번째 단어를 word에 저장(비교하기 위해)
    first_fail = 0 # 첫 번째 탈락한 사람 번호
    first_failer_turn = 0 # 첫 번째 탈락한 사람의 차례
    
    for i in range(1, len(words)): # 첫번째 단어는 word 안에 넣었으므로 1부터 반복 시작
        # 중복 검사
        if words[i] not in word: # 중복 검사를 위해 word 안에 없으면 통과
            # 단어가 이어지는지 검사
            if words[i][0] == word[-1][-1]: # 앞 사람의 단어의 마지막 알파벳과 지금 단어의 첫 알파벳이 같으면 통과
                word.append(words[i])
            else: # 알파벳이 다르면 탈락
                first_fail = i%n + 1 # 탈락한 사람 번호는 단어의 번호와 전체 인원 수로 나눈 나머지 + 1
                first_failer_turn = i//n+1 # 탈락한 사람이 몇번째 차례에 탈락 했는지는 단어의 번호를 전체 인원수 +1 로 나눈 몫
                break
        else: # word안에 있으면 중복이므로 탈락
            first_fail = i%n + 1
            first_failer_turn = i//n+1
            break
    
    result = [first_fail, first_failer_turn] # 결과 반환
    return result