from collections import deque

n = int(input())
sentence = deque()


for _ in range(n):
    cursor = 0
    l = list(input())
    for i in range(len(l)):

        # 왼쪽 화살표
        if l[i] == "<":
            cursor -= 1
            if cursor < 0:
                cursor = 0
        # 오른쪽 화살표
        elif l[i] == ">":
            cursor += 1
            if cursor > len(sentence):
                cursor = len(sentence)
        # 백스페이스
        elif l[i] == "-":
            cursor -= 1
            if sentence[cursor].isalnum():
                sentence.pop()

        # 대문자, 소문자, 숫자
        else:
            sentence.insert(cursor, l[i])
            cursor += 1
    
    sentence = list(sentence)
    print(''.join(map(str,sentence)))