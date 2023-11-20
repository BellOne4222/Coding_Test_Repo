from collections import deque

def bfs(begin, target, words, changes):
    change = 0
    q = deque()
    q.append([begin, 0])    # [단어, 깊이]
    visited = [False] * (len(words))    # 방문 노드 여부 확인 리스트
    while q:
        word, depth = q.popleft()
        if word == target:
            change = depth
            break        
        for i in range(len(words)):
            check = 0
            if not visited[i]:    # 만약 확인 안 한 단어라면
                # 그 단어가 words 속 단어와 다를 때 한 자씩 비교해서 더하기
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        check += 1

                if check == 1:   # 만약 다른 글자 개수가 1개라면
                    q.append([words[i], depth+1])
                    visited[i] = True

    return change

def solution(begin, target, words):
    if target in words:
        change = bfs(begin,target,words,0)
    else:
        change = 0
        
    return change