def solution(s):
    s = s.split(" ") # 1. 문자열을 공백으로 분리하여 단어 배열을 만든다.
    for i in range(len(s)):
        s[i] = s[i][:1].upper() + s[i][1:].lower() # 2. 각 단어를 탐색하며 단어의 맨 앞글자는 대문자로 바꾸고, 나머지는 소문자로 바꾼다.
    answer = ' '.join(s) # 3. 다시 공백을 기준으로 조인하여 리턴한다.
    return answer




