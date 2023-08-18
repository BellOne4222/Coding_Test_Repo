# 1928. Base64 Decoder

from collections import defaultdict
T = int(input())
dic = defaultdict(int)
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(ord('A'), ord('Z')+1):
    dic[chr(i)] = i-65
for i in range(ord('a'), ord('z')+1):
    dic[chr(i)] = i-65-6
dic.update({'0':52, '1':53, '2':54, '3':55, '4':56, '5':57, '6':58, '7':59, '8':60, '9':61, '+':62, '/':63})

for test_case in range(1, T + 1):
    string = input()
    temp = ""
    for s in string:
        temp += "".join(format(dic[s], 'b').zfill(6))
    ans = ""
    for i in range(0, len(temp), 8):
        ans += chr(int(temp[i:i + 8], 2))

    print(f"#{test_case} {ans}")


# A-Z, a-z, 0-9, +, /를 딕셔너리에 Encoding 합니다.

# 입력받은 문자열의 문자들을 하나씩 2진수로 변환 시키고 zfill()로 6자리를 만들었습니다.

# Encoding 된 암호를 다시 8비트씩 끊어서 2진수를 문자로 변경합니다 (여기서 문자에 해당하는 변수는 Based64 Decoder 암호 표가 아닌 기본 ascii 값을 이용, 이것을 빨리 알아내지 못해 시간이 지체되었네요)

# 결과 및 정리
# 지금 SSAFY를 대비해서 SWEA D2 정답률 높은 것부터 푸는데 이 문제는 생각보다 어려워서 구글링하면서 풀었습니다.

# 오늘 새롭게 알게 된 소소한 지식들입니다.

# 0010011 같은 문자열 타입의 2진수를 10진수로 바꾸는 방법: int(0010011, 2)

# 자리수를 0으로 채워 길이를 맞추는 방법: zfill()

# base64 라이브러리 이용해서 푸는법
# from base64 import b64decode 
# T = int(input())
# for t in range(1, T + 1):
#     data = input()
#     ans = b64decode(data).decode('UTF-8')
#     print(f'#{t} {ans}')