# 참고 : https://moondol-ai.tistory.com/423
# A=1, E=?, I=1563 이렇게 보면 A와 I 간의 차이는 1562이기 때문에 A와 E 간의 차이는 아마 그 절반인 781이 아닐까 추측
# 각 자릿수가 바뀌는 규칙은 (x 5) + 1 이다. 이를 각 자릿수에 적용하면 단어 수가 총 5개이므로 4개까지 반복하면 된다(781에 해당).
# 코드에서 answer = len(word) 로 초기화한 이유는 딕셔너리 char에서 A를 0으로 두었기 때문이다. 하지만 AAAAA=5이므로 길이로 초기값을 정한 것이다.



def solution(word):
    char = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    answer = len(word) # A를 0으로 두었기 때문에 길이로 초기화 필요
    re = (((5 + 1) * 5 + 1) * 5 + 1) * 5 + 1 # 781
    for i in word:
        answer += re * char[i] # 첫 문자가 무슨 글자로 시작하는지
        re = (re - 1) // 5
    return answer