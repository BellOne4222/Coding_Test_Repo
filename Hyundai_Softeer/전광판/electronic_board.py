# 문제 : https://softeer.ai/practice/formCodeEditor.do
# 전광판
# 참고 : https://www.youtube.com/watch?v=ADp_WInjFBg
# 자릿수 맞추는 부분을 못하겠어서 이부분을 참고했습니다.

import sys
input = sys.stdin.readline 

# 딕셔너리에 각 숫자에 대한 정보 저장

board = {
    
    '0' : '1110111',
    '1' : '0010010',
    '2' : '1011101',
    '3' : '1011011',
    '4' : '0111010', 
    '5' : '1101011',
    '6' : '1101111',
    '7' : '1110010',
    '8' : '1111111',
    '9' : '1111011',
    ' ' : '0000000' # 공백은 다꺼져있는거를 표현현
}


t = int(input())
for _ in range(t):
    a, b = map(str,input().split())
    
    
    # 자릿수 맞추기(각 숫자 길이를 5에서 빼서 그 공간을 공백으로 채운 후에 숫자를 넣어서 자릿수 맞추기기)
    a = (5 - len(a)) * ' ' + a
    b = (5 - len(b)) * ' ' + b
    

    ans = 0

    # 5개의 자릿수에서 7개의 전구를 비교 하여 각 전구가 다를때마다 ans += 1 해서 경우의 수 반환환
    for i in range(5):
        for j in range(7):
            if(board[a[i]][j] != board[b[i]][j]):
                ans += 1
                
    print(ans)


