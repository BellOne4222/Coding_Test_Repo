from collections import deque

# BFS를 수행하여 단어를 변환하는 함수
def bfs(begin, target, words, changes):
    change = 0
    q = deque()
    q.append([begin, 0]) 
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

# 최소 변환 과정을 찾는 함수
def solution(begin, target, words):
    if target in words:
        change = bfs(begin, target, words, 0)
    else:
        change = 0
        
    return change

# bfs 함수를 사용하여 BFS(Breadth-First Search)를 수행하여 변환 가능한 단어를 찾고, solution 함수에서는 target이 words에 있는지 여부를 확인하고 
# 그에 따라 변환 가능한지 여부를 결정합니다. BFS는 단어를 한 글자씩 바꿔가며 변환 가능한 단어를 찾아내는 데 사용됩니다. 최종적으로 변환 과정의 단계 수를 반환