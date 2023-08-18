# 참고 : https://velog.io/@sugenius77/Python%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AA%A8%EC%9D%8C%EC%82%AC%EC%A0%84
# DFS
# word_list에 A, AA, AAA, AAAA, AAAAA을 넣으면서 DFS를 돌다가
# cnt = 5일 때 되돌아가면 AAAAE, AAAAI, AAAAO, AAAAU를 넣다가
# AAAE, AAAEA, AAAEI ... 를 넣게 된다. 이런 식으로 완전 탐색 진행
# 우리가 찾는 word의 순서는 word_list에서 word의 인덱스 + 1


def solution(word):
    answer = 0
    word_list = []
    words = 'AEIOU'
    
    def dfs(cnt, w):
        if cnt == 5:
            return 
        for i in range(len(words)):
            word_list.append(w + words[i])
            dfs(cnt+1, w + words[i])
            
    dfs(0,"")
    
    return word_list.index(word)+1